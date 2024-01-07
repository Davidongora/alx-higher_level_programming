#!/usr/bin/python3
"""this module has a function that prints a square with the character #"""
def print_square(size):
    """function that prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")        
    elif size < 0:
        raise ValueError("size must be >=0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")
