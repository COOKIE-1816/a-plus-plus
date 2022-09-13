"""
import Basic.error
import Basic.lexer
import Basic.token
"""


TT_EOF = "TT_EOF"

TT_INT = "TT_INT"
TT_FLOAT = "FLOAT"

TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"

TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"

class Token:
    def __init__(self, type_, value = None, pos_start = None, pos_end = None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos.end = pos_start.copy()

            self.pos_end.advance()
        
        if pos_end:
            self.pos_end = pos_end


    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        
        return f'{self.type}'


DIGITS = "0123456789"


def strings_with_arrows(text, pos_start, pos_end):
    result = ""


    idx_start = max(text.rfind("\n", 0, pos_start.idx), 0)
    idx_end = text.find("\n", idx_start + 1)

    if idx_end < 0:
        idx_end = len(text)
    

    i = 0
    line_count = pos_end.ln - pos_start.ln + 1

    for i in range(line_count):
        line = text[idx_start: idx_end]

        col_start = pos_start.col if i == 0 else 0
        col_end = pos_end.col if i == line_count - 1 else len(line) - 1


        result += line + "\n"
        result += " " * col_start + "^" * (col_end - col_start)


        idx_start = idx_end
        idx_end = text.find("\n", idx_start + 1)

        if idx_end < 0:
            idx_end = len(text)
        

        return result.replace("\t", "")


class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end

        self.error_name = error_name
        self.details = details
    

    def as_string(self):
        result = f'{self.error_name}: {self.details} <--- '

        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        result += "\n\n" + strings_with_arrows(self.pos_start.ftxt, self.pos_start, self.pos_end)

        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, "[err 001] Illegal Character", details)

class InvaildSyntaxError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, "[err 002] Invaild Syntax", details)


class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx

        self.ln = ln
        self.col = col

        self.fn = fn
        self.ftxt = ftxt
    

    def advance(self, current_char = None):
        self.idx += 1
        self.col += 1

        if current_char == "\n":
            self.ln += 1
            self.col = 0
        
        
        return self
    
    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)


class Lexer:
    def __init__(self, fn, text):
        self.text = text

        self.fn = fn

        self.pos = Position(-1, 0, 1, fn, text)
        self.current_char = None

        self.advance()
    

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in "\t":
                self.advance()
            
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())

            elif self.current_char == "+":
                tokens.append(Token(TT_PLUS, pos_start = self.pos))
                self.advance()
            elif self.current_char == "-":
                tokens.append(Token(TT_MINUS, pos_start = self.pos))
                self.advance()
            elif self.current_char == "*":
                tokens.append(Token(TT_MUL, pos_start = self.pos))
                self.advance()
            elif self.current_char == "/":
                tokens.append(Token(TT_DIV, pos_start = self.pos))
                self.advance()
            
            elif self.current_char == "(":
                tokens.append(Token(TT_LPAREN, pos_start = self.pos))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token(TT_RPAREN, pos_start = self.pos))
                self.advance()
            

            else:
                pos_start = self.pos.copy()

                char = self.current_char
                self.advance()

                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")
        
        tokens.append(Token(TT_EOF, pos_start = self.pos))
        return tokens, None
    
    def make_number(self):
        num_str = ""
        dot_count = 0

        pos_start = self.pos.copy()

        while self.current_char != None and self.current_char in DIGITS + ".":
            if self.current_char == ".":
                if dot_count == 1:
                    break
                
                dot_count += 1
                num_str += "."
            else:
                num_str += self.current_char
            
            self.advance()
        
        if dot_count == 0:
            return Token(TT_INT, int(num_str), pos_start, self.pos)
        else:
            return Token(TT_FLOAT, float(num_str), pos_start, self.pos)


class NumberNode:
    def __init__(self, tok):
        self.tok = tok
    
    def __repr__(self):
        return f'{self.tok}'

class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node
    
    def __repr__(self):
        return f'({self.left.node}, {self.op_tok}, {self.right_node})'


class ParseResult:
    def __init__(self):
        self.error, self.node = None


    def register(self, res):
        if isinstance(res, ParseResult):
            if res.error:
                self.error = res.error
            
            return res.node
        
        return res

    def success(self, node):
        self.node = node

        return self
    
    def failure(self, error):
        self.error = error

        return self

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = 1

        self.advance()
    

    def advance(self):
        self.tok_idx += 1
        
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        

        return self.current_tok


    def parse(self):
        res = self.expr()

        if not res.error and self.current_tok.type !=  TT_EOF:
            return res.failure()

        return res


    def factor(self):
        res = ParseResult()

        tok = self.current_tok

        if tok.type in (TT_INT, TT_FLOAT):
            res.register(self.advance())

            return res.success(NumberNode(tok))
        
        return res.failure(
            InvaildSyntaxError(
                tok.pos_start,
                tok.pos_end,

                "[err 003] Unexcepted INT or FLOAT absence")
        )

    def term(self):
        return self.bin_op(self.factor, (TT_MUL, TT_DIV))

    def expr(self):
        return self.bin_op(self.factor, (TT_PLUS, TT_MINUS))

    
    def bin_op(self, func, ops):
        res = ParseResult()
        left = res.register(func())

        if res.error:
            return res

        while self.current_tok.type in ops:
            op_tok = self.current_tok

            res.register(self.advance())

            right = res.register(func())

            if res.error:
                return res

            left = BinOpNode(left, op_tok, right)
        
        return res.success(left)
        


def run(fn, text):
    # Tokens generator
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    if error:
        return None, error


    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()


    return ast.node, ast.error