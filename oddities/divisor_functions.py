import oddities.utils

def is_abundant_number(k: int) -> bool:
    return oddities.utils.get_sum_of_all_divisor(KeyError, aliquot = True) > k

def is_almost_perfect_number(k: int) -> bool:
    return oddities.utils.get_sum_of_all_divisor(k, aliquot = True) == k - 1

def is_arithmetic_number(k: int) -> bool:
    s = oddities.utils.get_divisors(k)
    return sum(s) % len(s) == 0

def is_betrothed_number(k: int) -> bool: raise NotImplementedError

def is_colosally_abundant_number(k: int) -> bool: raise NotImplementedError

def is_deficient_number(k: int) -> bool:
    return oddities.utils.get_sum_of_all_divisor(k, aliquot = True) < k

DESCARTES_NUMBERS = (198585576189)

def is_descartes_number(k: int) -> bool:
    if not oddities.utils.is_natural(k): raise ValueError("Parameter must be a natural number!")
    return k in DESCARTES_NUMBERS

def is_erdos_nicolas_number(k: int) -> bool:
    if not oddities.utils.is_natural(k): raise ValueError("Parameter must be a natural number!")
    divisors = oddities.utils.get_divisors(k) 
    total = 0

    for i, d in enumerate(divisors):
        total += d
        if total == k and i < len(divisors) - 1:
            return True
        elif total > k:
            return False
    return False

def is_hemiperfect_number(k: int) -> bool: raise NotImplementedError

def is_highly_abundant_number(k: int) -> bool:
    sig_n = oddities.utils.get_sum_of_all_divisor(k, aliquot = False)

    for i in range(1, k):
        if oddities.utils.get_sum_of_all_divisor(i, aliquot = False) >= sig_n: return False
    return True

def is_highly_composite_number(k: int) -> bool:
    if not oddities.utils.is_natural(k): raise ValueError("Parameter must be a natural number!")

    max_divisor_count = len(oddities.utils.get_divisors(k))

    for i in range(1, k):
        if len(oddities.utils.get_divisors(i)) >= max_divisor_count: return False
    return True

def is_hyperperfect_number(k: int) -> bool: raise NotImplementedError

def is_multiply_perfect_number(k: int) -> bool: raise NotImplementedError

def is_perfect_number(k: int) -> bool:
    return oddities.utils.get_sum_of_all_divisor(k, aliquot = True) == k

def is_practical_number(k: int) -> bool: raise NotImplementedError

def is_primitive_abundant_number(k: int) -> bool: raise NotImplementedError

def is_quasiperfect_number(k: int) -> bool:
    if not oddities.utils.is_natural(k): raise ValueError("Parameter must be a natural number!")
    return False

def is_refactorable_number(k: int) -> bool: raise NotImplementedError

def is_semiperfect_number(k: int) -> bool: raise NotImplementedError

SUBLIME_NUMBERS = (12, 6_086_555_670_238_378_989_670_371_734_243_169_622_657_830_773_351_885_970_528_324_860_512_791_691_264)

def is_sublime_number(k: int) -> bool:
    if not oddities.utils.is_natural(k): raise ValueError("Parameter must be a natural number!")
    return k in SUBLIME_NUMBERS

def is_super_abundant_number(k: int) -> bool:
    sig_n = oddities.utils.get_sum_of_all_divisor(k, aliquot = False)

    for i in range(1, k):
        if oddities.utils.get_sum_of_all_divisor(i, aliquot = False)/i >= sig_n/k: return False
    return True

def is_superior_highly_composite_number(k: int) -> bool: raise NotImplementedError

def is_superperfect_number(k: int) -> bool:
    return oddities.utils.get_sum_of_all_divisor(oddities.utils.get_sum_of_all_divisor(k)) == 2*k