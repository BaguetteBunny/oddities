import oddities

assert oddities.is_mersenne_number(number = 63)
assert oddities.is_mersenne_number(number = 64) == False

assert oddities.is_mersenne_prime(exponent = 13)
assert oddities.is_mersenne_prime(exponent = 14) == False

assert oddities.is_fermat_number(18446744073709551617)
assert oddities.is_fermat_number(18446744073709551618) == False

assert oddities.is_fermat_prime(number = 257)

print("Passed!")