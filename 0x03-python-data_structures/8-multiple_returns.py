#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else "None"
    multi = length, first_char
    return multi
