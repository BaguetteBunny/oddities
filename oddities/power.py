import utils
from math import isqrt

def is_perfect_square(number: int) -> bool:
    if not utils.is_natural(number): raise ValueError("Parameter must be a natural number!")
    root = isqrt(number)
    return root * root == number