#!/usr/bin/python3.8
if __name__ == "__main__":
    from hidden_4 import *
    for a in dir():
        if a[:2] != "__":
            print(f"{a}")
