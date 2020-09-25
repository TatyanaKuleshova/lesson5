from homework4 import random_names

#test1 (в списке рандом 100 элементов)

def test_1_random_names():
    list_names = ('Olga', 'Mike', 'Svetlana', 'Dima', 'Oleg', 'Maria', 'Vova', 'Roma', 'Tanya', 'Julia', 'Ivan', 'Nata', 'Valya', 'Lena', 'Kate', 'Nonna', 'Sasha', 'Pavel', 'Vlad', 'Dan')
    assert len(random_names(100, list_names)) == 100

#test 2 (в 2созданных списках по 100 элементов)

def test_2_random_names():
    list_n = ('Olga', 'Mike', 'Svetlana', 'Dima', 'Oleg', 'Maria', 'Vova', 'Roma', 'Tanya', 'Julia', 'Ivan', 'Nata', 'Valya', 'Lena', 'Kate', 'Nonna', 'Sasha', 'Pavel', 'Vlad', 'Dan')
    assert len(random_names(100, list_n)) == len(random_names(100, list_n))