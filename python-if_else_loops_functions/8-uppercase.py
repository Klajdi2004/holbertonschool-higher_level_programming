#!/usr/bin/python3
def uppercase(string):
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - ord('a') + ord('A'))
        print(char, end="")
    print()                                                
