import random
from collections import Counter
# для задания 4
from datetime import datetime
import this

# 1. 100 случайных имен из списка

names = 'Olga', 'Mike', 'Svetlana', 'Dima', 'Oleg', 'Maria', 'Vova', 'Roma', 'Tanya', 'Julia', 'Ivan', 'Nata', 'Valya', 'Lena', 'Kate', 'Nonna', 'Sasha', 'Pavel', 'Vlad', 'Dan'

def random_names(n, *args):
    '''
    :param names: список имен
    :param n: количество на выходе
    :return: список из случайных имен
    '''
    return [random.choice(args) for i in range (n)]

rnames = random_names(100, *names)
print(len(rnames), rnames)

# 2. Самое часто употребляющееся имя в списке на выходе функции

pnames = Counter(rnames) .most_common(1)
print(pnames)


# 3. Самая редкая буква, с которй начинает имя из списка на выходе функции

def rar_letter(names):
    rarlet = map(lambda x: x[0], rnames)
    return Counter(rarlet) .most_common()[-1]

print(rar_letter(rnames))


