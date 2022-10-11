#include "replace.h"

char a_plus_plus_replace(char source[],
             char target,
             char replacement,
             int ignore_when_closed) {
    
    int i = 0;
    int is_closed = 0;

    while(source[i] != "\0") {
        if(source[i] == "\"" || source[i] == "'") {
            if(is_closed == 0) {
                is_closed = 1;
            } else {
                is_closed = 0;
            }
        } else {
            if(ignore_when_closed == 0) {
                if(source[i] == target) {
                    source[i] = replacement;
                }
            } else {
                if(is_closed == 0) {
                    source[i] = replacement;
                }
            }
        }

        i = i + 1;
    }

    return source;
};