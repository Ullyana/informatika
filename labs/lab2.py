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

from math import *
def is_square(a):
    root = isqrt(a)
    return root*root == a
    if root*root == a:
        b = 0
    else:
        b = 1
        return b
def task1():
    e == 0;
    while e:
        print('введите число:')
        c = float(input())
        c = int()
        if is_square(c) == 0:
            print('является квадратом целого числа')
        else:
            print('не является квадратом целого числа')
        d = 6   #заданное число
        if c > d:
            print('число больше заданного')
        else:
            print('число меньше заданного')
task1()


1 задание исправленное
def is_square(n):
    if n < 1:
        return False
    else:
        for i in range(int(n / 2) + 1):
            if (i * i) == n:
                return True
        return False
def task1():
    a = True
    while a:
        print('Введите число:')
        b = float(input())
        c = 51 #заданное число
        if is_square(b) == True:
            print('Число является квадратом целого числа')
        else:
            print('Число не является квадратом целого числа')
        if b > c:
            print('Число больше заданного')
        else:
            print('Число меньше заданного')
task1()
