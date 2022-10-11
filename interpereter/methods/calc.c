#include "calc.h"
#include "replace.h"


char a_plus_plus_maths_tokens[4] = "+-/*";

/*
int a_plus_plus_maths_divide(int x, int times) {
    if(x == 0 || times == 0 || x <) {
        // Cannot divide by zero.
        return 0;
    }
};
*/

int a_plus_plus_maths_mul(int x, int times) {
    if(times == 1) {
        return x;
    }
    
    if(x == 1) {
        return times;
    }
    

    if(times == 0 || times < 0 || x == 0 || x < 0) {
        return 0;
    }


    char a_plus_plus_dots[] = "";

    for(int i = 0; i == times || i < times; i = i + 1) {
        for(int i2 = 0; i2 == x || i2 < x; i2 = i2 + 1) {
            a_plus_plus_dots[i + i2] = ".";
        }
    }


    return sizeof(a_plus_plus_dots);
}


int a_plus_plus_calc(char maths[]) {
    maths = a_plus_plus_replace(maths, " ", "", 0);

    char maths_separated[] = a_plus_plus_replace(maths, a_plus_plus_maths_tokens[0], " ", 0);
    char maths_separated[] = a_plus_plus_replace(maths_separated, a_plus_plus_maths_tokens[1], " ", 0);
    char maths_separated[] = a_plus_plus_replace(maths_separated, a_plus_plus_maths_tokens[2], " ", 0);
    char maths_separated[] = a_plus_plus_replace(maths_separated, a_plus_plus_maths_tokens[3], " ", 0);
};