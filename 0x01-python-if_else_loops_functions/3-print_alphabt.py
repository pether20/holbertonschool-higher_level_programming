#!/usr/bin/python3
for a in range(97, 123):
    if a in (113, 101):
        continue
    else:
        print('{:s}'.format(chr(a)), end='')
