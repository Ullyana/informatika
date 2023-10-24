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


1 задание (готовое)
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

2 задание 
from math import *
from matplotlib import *
def task2():
    a = float(input())
    b = float(input())
for i in range[a, b]:
    
task1()


5 задание (готовое)
def task5():
    print("Введите значение стороны a: ")
    a = float(input())
    print("Введите значение стороны b: ")
    b = float(input())
    print("Введите значение стороны c: ")
    c = float(input())
    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует")
        if (c ** 2 == a ** 2 + b ** 2) or (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2):
            print("Треугольник прямоугольный")
        elif (c ** 2 < a ** 2 + b ** 2) or (a ** 2 < b ** 2 + c ** 2) or (b ** 2 < a ** 2 + c ** 2):
            print("Треугольник острый")
        elif (c ** 2 > a ** 2 + b ** 2) or (a ** 2 > b ** 2 + c ** 2) or (b ** 2 > a ** 2 + c ** 2):
            print("Треугольник тупой")
    else:
        print("Треугольник не существует")

task5()
