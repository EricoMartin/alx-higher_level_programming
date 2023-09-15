#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        romans = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
            'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
            'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
        }
        n = 0
        res = 0

        while n < len(roman_string):
            if n + 1 < len(roman_string) and roman_string[n:n+2] in romans:
                res = res + romans[roman_string[n:n+2]]
                n += 2
            else:
                res += romans[roman_string[n]]
                n += 1
        return res
