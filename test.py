import oddities

# Utils
assert oddities.get_divisors(6) == [1, 2, 3, 6]
assert oddities.get_sum_of_all_divisor(1, True) == 0

assert oddities.is_perfect_number(6)
assert oddities.is_almost_perfect_number(33554432)
assert oddities.is_superperfect_number(262144)
assert oddities.is_erdos_nicolas_number(61900800)
assert oddities.is_highly_abundant_number(4)

#
# Of form a × 2b ± 1
#
assert oddities.is_cullen_number(3)

assert oddities.is_mersenne_number(63)
assert oddities.is_mersenne_number(64) == False

assert oddities.is_mersenne_prime_exponent(13)
assert oddities.is_mersenne_prime_exponent(14) == False

assert oddities.is_fermat_number(18446744073709551617)
assert oddities.is_fermat_number(18446744073709551618) == False

assert oddities.is_fermat_prime(257)

print("Passed!")