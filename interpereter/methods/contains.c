#include "contains.h"

int a_plus_plus_contains(char in[], char character) {
    for(int i = (-1); !(i > sizeof(in)); i = i + 1) {
        if(in[i] == character) {
            return 1;
        }
    }

    return 0;
};