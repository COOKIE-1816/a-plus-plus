/*
          @@@@@@@@@@@		--- INFORMACE O SOUBORU ---
       #&&@@@.....@@@&&%	Název souboru			interpereter.c
       %@@@@@     &@@@@@	Cesta k souboru		    /interpereter
    *@@@@@           @@@	Verze souboru			1.0
    *@@@@@
    *@@@@@			        Produkt				    A++ interpereter
    *@@@@@			        Verze produktu          1, gen. 1.
    *@@@@@
    *@@@@@			        Tento soubor je považován za součást produktu, ve
    *@@@@@			        kterém se nachází. Licence k nalezení v koř. adr. produktu.
-------------------------------------------------------------------------------------------------
*/

#include "interpereter.h"

#include "methods/calc.h"
#include "methods/replace.h"

#include <stdio.h>
#include <string.h>


int interperet_str(char syntax[]) {
    syntax = a_plus_plus_replace(syntax, "\n", "", 0);
    syntax = a_plus_plus_replace(syntax, " ", "", 1);
};


/*
int interperet_function(char func[]) {};

int interperet_string(char source[]) {
    int i = 0;

    while(source[i != "\0"]) {
        if(source[i] == "\n") {
            source[i] = "";
        }

        i = i + i;
    }
};
*/
