import constants as C
from math import sqrt

def is_natural(number: int) -> bool:
    return True if isinstance(number, int) and number > 0 else False

def is_whole(number: int) -> bool:
    return True if isinstance(number, int) and number >= 0 else False

def is_mersenne_number(number: int) -> bool:
    if not is_natural(number): raise ValueError("Parameter must be a natural number!")
    m = number + 1
    return m & (m-1) == 0

def get_mersenne_exponent(number: int) -> bool:
    if not is_mersenne_number(number): raise ValueError("Parameter must be a mersenne prime!")
    return (number-1).bit_length() - 1

def is_mersenne_prime(exponent: int) -> bool:
    if not is_natural(exponent): raise ValueError("Parameter must be a natural number!")
    elif (exponent == 1): return False
    elif (exponent == 2): return False

    s = 4
    mersenne = 2**exponent - 1

    for _ in range(exponent - 2):
        s = (s**2 - 2) % mersenne
    return s == 0

def is_fermat_prime(number: int) -> bool:
    if not is_natural(number): raise ValueError("Parameter must be a natural number!")
    return number in C.FERMAT_NUMBERS and number < 65538 # Biggest known fermat prime is 65537

def is_fermat_number(number: int) -> bool:
    if not is_natural(number): raise ValueError("Parameter must be a natural number!")
    return number in C.FERMAT_NUMBERS
