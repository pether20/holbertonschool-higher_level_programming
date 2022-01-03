#!/usr/bin/env python3
def no_c(my_string):
    char = 'cC'
    my_string = ''.join(x for x in my_string if x not in char)
    return my_string
