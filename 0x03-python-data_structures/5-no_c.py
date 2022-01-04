#!/usr/bin/python3
def no_c(my_string):
    str, char = '', 'cC'
    for i in my_string:
        if i not in char:
            str += i
    return str
