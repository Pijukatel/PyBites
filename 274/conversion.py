import pytest

def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    result = ""
    while True:
        remainder = number % base
        number = number // base
        result += str(remainder)
        if number == 0:
            break

    return int(result[::-1])
