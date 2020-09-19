# Все функции принимают на вход натуральные числа от 1 до 1000

# 1. Проверка числа на простоту

def n_prime(n):
    x = 2
    while n % x != 0:
        x += 1
    return x == n

# 2. Выводит список всех делителей числа

def dividers(n):
    dividers_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            dividers_list.append(i)
    return dividers_list

# 3. Выводит самый большой простой делитель числа, отличный от самого числа

def max_div_prime(n):
    dividers_list = [1]
    x = 1
    while x < n:
        div_list = [i for i in range(1, x + 1) if x % i == 0 and n % x == 0]
        if len(div_list) == 2:
            dividers_list.append(x)
        x += 1
    return max(dividers_list)

# PRO 4. Функция выводит каноническое разложение числа на простые множители

def canonical_decomposition(n):
    divid = []
    i = 2
    while i * i <= n:
        n //= i
        divid.append(i)
    else:
        i = i + 1
    if n > 1:
        divid.append(n)
    return divid

# PRO 5. Функция выводит самый большой делитель числа, отличный от самого числа

def great_div(n):
    return max(canonical_decomposition(n))