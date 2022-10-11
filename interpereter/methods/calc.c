#include "calc.h"
#include "replace.h"


char a_plus_plus_maths_tokens[4] = "+-/*";

int a_plus_plus_maths_mul(int x, int times) 
    if(times == 1) {
        return x;
    } else if(times =< 0) {
        return 0;
    } else {
        char a_plus_plus_dots[] = "";
        
        for(int i = 0; i =< times; i = i + 1) {
            for(int i2 = 0; i2 =< x; i2 = i2 + 1) {
                a_plus_plus_dots[i + i2] = ".";
            }
        }
    }
}

int a_plus_plus_calc(char maths[]) {
    maths = a_plus_plus_replace(maths, " ", "", 0);
};