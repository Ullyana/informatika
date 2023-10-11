from math import *
def square(a):
    print(type(sqrt(a)))
    if type(sqrt(a)) == 'int':
        b_d = 0
    else:
        b_d = 1
        return b_d
def task1():
    print('введите число')
    b = float(input())
    if square(b) == 0:
        print('является квадратом целого числа')
    else:
        print('не является квадратом целого числа')
    c = 6   #заданное число
    if b > c:
        print('число больше заданного')
    else:
        print('число меньше заданного')
task1()
