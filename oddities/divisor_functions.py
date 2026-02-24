import oddities.utils

def is_abundant_number(number: int) -> bool:
    return oddities.utils.get_sum_of_all_divisor(number, aliquot = True) > number

def is_almost_perfect_number(number: int) -> bool:
    return oddities.utils.get_sum_of_all_divisor(number, aliquot = True) == number - 1

def is_arithmetic_number(k: int) -> bool:
    s = oddities.utils.get_divisors(k)
    return sum(s) % len(s) == 0

def is_betrothed_number(k: int) -> bool: raise NotImplementedError

def is_colosally_abundant_number(k: int) -> bool: raise NotImplementedError

def is_deficient_number(number: int) -> bool:
    return oddities.utils.get_sum_of_all_divisor(number, aliquot = True) < number

DESCARTES_NUMBERS = (198585576189)

def is_descartes_number(number: int) -> bool:
    if not oddities.utils.is_natural(number): raise ValueError("Parameter must be a natural number!")
    return number in DESCARTES_NUMBERS

def is_erdos_nicolas_number(number: int) -> bool:
    if not oddities.utils.is_natural(number): raise ValueError("Parameter must be a natural number!")
    divisors = oddities.utils.get_divisors(number) 
    total = 0

    for i, d in enumerate(divisors):
        total += d
        if total == number and i < len(divisors) - 1:
            return True
        elif total > number:
            return False
    return False

def is_hemiperfect_number(k: int) -> bool: raise NotImplementedError

def is_highly_abundant_number(number: int) -> bool:
    sig_n = oddities.utils.get_sum_of_all_divisor(number, aliquot = False)

    for i in range(1, number):
        if oddities.utils.get_sum_of_all_divisor(i, aliquot = False) >= sig_n: return False
    return True

def is_highly_composite_number(number: int) -> bool:
    if not oddities.utils.is_natural(number): raise ValueError("Parameter must be a natural number!")

    max_divisor_count = len(oddities.utils.get_divisors(number))

    for i in range(1, number):
        if len(oddities.utils.get_divisors(i)) >= max_divisor_count: return False
    return True

def is_hyperperfect_number(k: int) -> bool: raise NotImplementedError

def is_multiply_perfect_number(k: int) -> bool: raise NotImplementedError

def is_perfect_number(number: int) -> bool:
    return oddities.utils.get_sum_of_all_divisor(number, aliquot = True) == number

def is_practical_number(k: int) -> bool: raise NotImplementedError

def is_primitive_abundant_number(k: int) -> bool: raise NotImplementedError

def is_quasiperfect_number(number: int) -> bool:
    if not oddities.utils.is_natural(number): raise ValueError("Parameter must be a natural number!")
    return False

def is_refactorable_number(k: int) -> bool: raise NotImplementedError

def is_semiperfect_number(k: int) -> bool: raise NotImplementedError

SUBLIME_NUMBERS = (12, 6_086_555_670_238_378_989_670_371_734_243_169_622_657_830_773_351_885_970_528_324_860_512_791_691_264)

def is_sublime_number(number: int) -> bool:
    if not oddities.utils.is_natural(number): raise ValueError("Parameter must be a natural number!")
    return number in SUBLIME_NUMBERS

def is_super_abundant_number(number: int) -> bool:
    sig_n = oddities.utils.get_sum_of_all_divisor(number, aliquot = False)

    for i in range(1, number):
        if oddities.utils.get_sum_of_all_divisor(i, aliquot = False)/i >= sig_n/number: return False
    return True

def is_superior_highly_composite_number(k: int) -> bool: raise NotImplementedError

def is_superperfect_number(number: int) -> bool:
    return oddities.utils.get_sum_of_all_divisor(oddities.utils.get_sum_of_all_divisor(number)) == 2*number