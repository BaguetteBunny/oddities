import constants as C
from math import isqrt

# Util
def is_natural(number: int) -> bool:
    return isinstance(number, int) and number > 0

def is_whole(number: int) -> bool:
    return isinstance(number, int) and number >= 0

# Getters
def get_divisors(n: int) -> list[int]:
    if not is_natural(n): raise ValueError("Parameter must be a natural number!")
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            k = n // i
            if i != k: divisors.append(k)
        i += 1
    return sorted(divisors)

def get_mersenne_exponent(number: int) -> int:
    if not is_mersenne_number(number): raise ValueError("Parameter must be a mersenne prime!")
    return (number+1).bit_length() - 1

def get_sum_of_all_divisor(n: int, aliquot: bool = False) -> int:
    if not is_natural(n): raise ValueError("Parameter must be a natural number!")
    total = 0
    i = 1

    while i * i <= n:
        if n % i == 0:
            total += i
            k = n // i
            if i != k: total += k
        i += 1
    return total - n if aliquot else total

# Checkers
def is_perfect_number(number: int) -> bool:
    return get_sum_of_all_divisor(number, aliquot = True) == number

def is_quasiperfect_number(number: int) -> bool:
    if not is_natural(number): raise ValueError("Parameter must be a natural number!")
    return False

def is_almost_perfect_number(number: int) -> bool:
    return get_sum_of_all_divisor(number, aliquot = True) == number - 1

def is_superperfect_number(number: int) -> bool:
    return get_sum_of_all_divisor(get_sum_of_all_divisor(number)) == 2*number

def is_erdos_number(number: int) -> bool:
    if not is_natural(number): raise ValueError("Parameter must be a natural number!")
    divisors = get_divisors(number) 
    total = 0

    for i, d in enumerate(divisors):
        total += d
        if total == number and i < len(divisors) - 1:
            return True
        elif total > number:
            return False
    return False

def is_abundant_number(number: int) -> bool:
    return get_sum_of_all_divisor(number, aliquot = True) > number

def is_highly_abundant_number(number: int) -> bool:
    sig_n = get_sum_of_all_divisor(number, aliquot = False)

    for i in range(1, number):
        if get_sum_of_all_divisor(i, aliquot = False) >= sig_n:
            return False
    return True

def is_super_abundant_number(number: int) -> bool:
    sig_n = get_sum_of_all_divisor(number, aliquot = False)

    for i in range(1, number):
        if get_sum_of_all_divisor(i, aliquot = False)/i >= sig_n/number:
            return False
    return True
        

def is_perfect_square(number: int) -> bool:
    if not is_natural(number): raise ValueError("Parameter must be a natural number!")
    root = isqrt(number)
    return root * root == number

def is_mersenne_number(number: int) -> bool:
    if not is_natural(number): raise ValueError("Parameter must be a natural number!")
    m = number + 1
    return m & (m-1) == 0

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

def is_descartes_number(number: int) -> bool:
    if not is_natural(number): raise ValueError("Parameter must be a natural number!")
    return number in C.DESCARTES_NUMBERS