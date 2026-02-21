import constants as C
from math import isqrt

def is_natural(number: int) -> bool:
    return isinstance(number, int) and number > 0

def is_whole(number: int) -> bool:
    return isinstance(number, int) and number >= 0

def is_perfect_square(number: int) -> bool:
    if not is_natural(number): raise ValueError("Parameter must be a natural number!")
    root = isqrt(number)
    return root * root == number

def get_divisors(n: int) -> list[int]:
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            k = n // i
            if i != k: divisors.append(k)
        i += 1
    return sorted(divisors)

def is_mersenne_number(number: int) -> bool:
    if not is_natural(number): raise ValueError("Parameter must be a natural number!")
    m = number + 1
    return m & (m-1) == 0

def get_mersenne_exponent(number: int) -> bool:
    if not is_mersenne_number(number): raise ValueError("Parameter must be a mersenne prime!")
    return (number+1).bit_length() - 1

def is_mersenne_prime(exponent: int) -> bool:
    if not is_natural(exponent): raise ValueError("Parameter must be a natural number!")
    elif (exponent == 1): return False
    elif (exponent == 2): return True

    s = 4
    mersenne = 2**exponent - 1

    for _ in range(exponent - 2):
        s = (s**2 - 2) % mersenne
    return s == 0

def is_fermat_prime(number: int) -> bool:
    if not is_natural(number): raise ValueError("Parameter must be a natural number!")
    return number in C.FERMAT_PRIMES

def is_fermat_number(number: int) -> bool:
    if not is_natural(number): raise ValueError("Parameter must be a natural number!")

    m = number - 1
    if m <= 0 or m & (m-1) != 0:
        return False
    
    n = m.bit_length() - 1
    if n & (n - 1) != 0:
        return False
    
    return n.bit_length() - 1    

def is_sublime_number(number: int) -> bool:
    if not is_natural(number): raise ValueError("Parameter must be a natural number!")
    return number in C.SUBLIME_NUMBERS