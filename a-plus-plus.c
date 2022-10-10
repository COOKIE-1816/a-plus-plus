/*
          @@@@@@@@@@@		--- INFORMACE O SOUBORU ---
       #&&@@@.....@@@&&%	Název souboru		    a-plus-plus.c
       %@@@@@     &@@@@@	Cesta k souboru		    /
    *@@@@@           @@@	Verze souboru			1.0
    *@@@@@
    *@@@@@			        Produkt				    A++ interpereter
    *@@@@@			        Verze produktu          1, gen. 2.
    *@@@@@
    *@@@@@			        Tento soubor je považován za součást produktu, ve
    *@@@@@			        kterém se nachází. Licence k nalezení v koř. adr. produktu.
-------------------------------------------------------------------------------------------------
*/

#include <unistd.h>
#include <stdio.h>
#include <limits.h>

#include "console.h"

int main(int arguments_count, char *arguments[]) {
    char cwd[4069];

    if(sizeof(arguments) == 1) {
        if(getcwd(cwd, sizeof(cwd)) != NULL) {
            return console(cwd);
        } else {
            printf("A++ interpereter failed: cannot get working directory.");
            return 1;
        }
    }

    if((sizeof(arguments) == 2 || sizeof(arguments == 3)) && arguments[2] == "console") {
        if(sizeof(arguments) == 3) {
            return console(arguments[3]);
        }

        
    }
};