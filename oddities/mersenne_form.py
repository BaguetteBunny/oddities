import oddities.utils

"""
Mersenne Numbers
Expressed in the form: 2^n - 1

n: Natural Number

https://en.wikipedia.org/wiki/Mersenne_prime
"""

def get_mersenne_number_exponent(k: int) -> int:
    if not is_mersenne_number(k): raise ValueError("Parameter must be a mersenne number!")
    return (k+1).bit_length() - 1

def is_mersenne_number(k: int) -> bool:
    if not oddities.utils.is_natural(k): raise ValueError("Parameter must be a natural number!")
    m = k + 1
    return m & (m-1) == 0

def is_mersenne_prime(k: int) -> bool:
    exp = get_mersenne_number_exponent(k)
    return is_mersenne_prime_exponent(exp)

def is_mersenne_prime_exponent(n: int) -> bool:
    if not oddities.utils.is_natural(n): raise ValueError("Parameter must be a natural number!")
    elif (n == 1): return False
    elif (n == 2): return True

    s = 4
    mersenne = 2**n - 1

    for _ in range(n - 2):
        s = (s**2 - 2) % mersenne
    return s == 0

"""
Cullen Numbers
Expressed in the form: n * 2^n + 1

n: Natural Number

https://en.wikipedia.org/wiki/Cullen_number
"""

CULLEN_PRIME_EXPONENTS = (1, 141, 4713, 5795, 6611, 18496, 32292, 32469, 59656, 90825, 262419, 361275, 481899, 1354828, 6328548, 6679881)

def get_cullen_number_exponent(k: int) -> int: raise NotImplementedError

def is_cullen_number(k: int) -> bool:
    n = k - 1
    max_n = k.bit_length()

    for m in range(1, max_n + 1):
        if n == m * (1 << m): return True
        if m * (1 << m) > n: break
    return False

def is_cullen_prime(k: int) -> bool: raise NotImplementedError

def is_cullen_prime_exponent(n: int) -> bool: raise NotImplementedError

"""
Double Mersenne Number
Expressed in the form: 2^(2^p - 1) - 1

p: Prime Number

https://en.wikipedia.org/wiki/Double_Mersenne_number
"""

DOUBLE_MERSENNE_PRIMES = (7, 127, 2147483647, 170141183460469231731687303715884105727)

def get_double_mersenne_number_exponent(k: int) -> int: raise NotImplementedError

def is_double_mersenne_number(k: int) -> bool:
    if not oddities.utils.is_natural(k): raise ValueError("Parameter must be a natural number!")

    m = k + 1
    if m & (m - 1) != 0:
        return False
    
    exp = m.bit_length() - 1
    e = exp + 1
    if e & (e - 1) != 0:
        return False
    
    p = e.bit_length() - 1
    return p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)

def is_double_mersenne_prime(k: int) -> bool:
    if not oddities.utils.is_natural(k): raise ValueError("Parameter must be a natural number!")
    return k in DOUBLE_MERSENNE_PRIMES

def is_double_mersenne_prime_exponent(n: int) -> bool: raise NotImplementedError

"""
Fermat Number
Expressed in the form: 2^(2^n) + 1

n: Natural Number

https://en.wikipedia.org/wiki/Fermat_number
"""

FERMAT_PRIMES = (3, 5, 17, 257, 65537)

def get_fermat_number_exponent(k: int) -> int: raise NotImplementedError

def is_fermat_number(k: int) -> bool:
    if not oddities.utils.is_natural(k): raise ValueError("Parameter must be a natural number!")

    m = k - 1
    if m <= 0 or m & (m-1) != 0:
        return False
    
    n = m.bit_length() - 1
    if n & (n - 1) != 0:
        return False
    
    return n.bit_length() - 1    

def is_fermat_prime(k: int) -> bool:
    if not oddities.utils.is_natural(k): raise ValueError("Parameter must be a natural number!")
    return k in FERMAT_PRIMES

def is_fermat_prime_exponent(n: int) -> bool: raise NotImplementedError