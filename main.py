# Все функции принимают на вход натуральные числа от 1 до 1000
from divisor_master import n_prime
from divisor_master import dividers
from divisor_master import max_div_prime
from divisor_master import canonical_decomposition
from divisor_master import great_div

# 1. Проверка числа на простоту

n = int(input('Введите число от 1 до 1000: '))
print(n_prime(n))

# 2. Выводит список всех делителей числа

print('Все делители числа', n, dividers(n))

# 3. Выводит самый большой простой делитель числа, отличный от самого числа

print('Самый большой простой делитель числа ', n, max_div_prime(n))

# PRO 4. Функция выводит каноническое разложение числа на простые множители

print('Каноническое разложение числа на множители: ', canonical_decomposition(n))

# PRO 5. Функция выводит самый большой делитель числа, отличный от самого числа

print("Самый большой делитель числа ", n, great_div(n))