def is_natural(number: int) -> bool:
    return isinstance(number, int) and number > 0

def is_whole(number: int) -> bool:
    return isinstance(number, int) and number >= 0

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