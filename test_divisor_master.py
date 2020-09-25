from divisor_master import n_prime
from divisor_master import dividers
from divisor_master import max_div_prime
from divisor_master import canonical_decomposition
from divisor_master import great_div

# test1

def test_n_prime ():
    assert n_prime(21) == False

def test_2_n_prime():
    assert n_prime(31) == True

#test2

def test_3_dividers ():
    assert dividers(399) == [1, 3, 7, 19, 21, 57, 133, 399]

# test3

def test_4_max_div_prime ():
    assert max_div_prime(399) == 19

#test4

def test_5_canonical_decomposition ():
    assert canonical_decomposition(543) == [3, 181]

#test 5

def test_6_great_div ():
    assert great_div(56) == 7

