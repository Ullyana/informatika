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
def task2():
    print('Введите значение a:')
    a = float(input())
    print('Введите значение b:')
    b = float(input())
    x = [a]
    h = abs(a-b)/10
    f = []
    i=0
    while len(x) <= 10:
        if x[i]<0:
            c = 7*sin(x[i])+9*cos(x[i])
            f.append(c)
        else:
            d = (x[i]-exp(x[i]))**2
            f.append(d)
        x.append(x[i]+h)
        i+=1
    print(x,f)
task2()

3 задание 
def decimal_in_new_numeral_system(number, base):
    result = ''
    intp = int(number)
    frp = number - intp
    while intp > 0
        r = intp % base
        result = str(r) + result
        intp = intp // base
    result += '.'
    pr = 4
    while frp > 0 and pr > 0
        frp *= base
        digit = int(frp)
        result += str(digit)
        frp -= digit
        pr -= 1
    return result
def task3():
    number = float(input('Введите десятичное число: '))
    base = int(input('Выберите систему счисления: '))
    result = decimal_in_new_numeral_system(number, base)
    print(f"Результат: {result}")
task3()

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

4 задание 
def task4():
    x = float(input())
    y = float(input())
    one = (y<=3*x-5) and (y<=-3*x+13) and (y>=-0,5*x+2)
    two = ((x-4)**2+(y+1)**2<=4) and (y<=2*x-8) and (x>=3)
    three = (y<=x-7) and (y>=x-10) and (y<=-2*x+11) and (y>=-2*x-5)
    four = (x>=4) and (x<=5) and ((x-4)**2+(y+1)**2<=4)
    five = (y<=-x+1) and ((x-4)**2+(y+1)**2<=4)
    
    six = (y<=5) and (y>=1) and (y>=1,5*x+2) and (x>=-1)
    seven = (y<=0,5*x+2) and (y<=-x+2) and (y>=-0,25*x+0,5)
    eight = (y<=-x-1) and (y<=-3*x-1) and (y>=-1,5*x-2,5)
    nine = ((x+1)**2+(y-1)**2<=4) and (y>=2) and (x<=-1)
    ten = ((x+1)**2+(y-1)**2<=4) and (y<=-x-1) and (y<=1)
    figure1 = one or two or three or four or five
    figure2 = six or seven or eight or nine or ten
task4()


def factorial(n):
    result = 1
    for i in range(1,n+1)
        result *=i
        return result
def task8()
    e = 1.e-8  #точность ряда

    d = 2 # разность арифметической прогрессии# # # = x - (( x - 1 ) ** 3) / factorial(3) + (( x - 1 ) ** 5) / factorial(5) + 

task8()


def factorial(n):
    result = 1
    for i in range(1,n+1)
        result *=i
        return result
def task8()
    x = float(input())
    e = 0,001   #точность ряда
    d = 2
    S1 = x - (( x - 1 ) ** (1+(d*1)) / factorial((1+(d*1))
    S2 = x - (( x - 1 ) ** (1+(d*1)) / factorial((1+(d*1)) + ( x - 1 ) ** (1+(d*2)) / factorial((1+(d*2))
if S2-S1=e:
task8()



                                                                                                
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i
        return result

def task8():
    EPS = 0.001

    x = float(input('Введите x: '))
    m = int(input('Введите конечное число: '))
    while (sum1 - sum >= EPS):
    for i in range(1, m+1):

        sum=x+(-1)**i*((x-1)**(2*i+1)/factorial(2*i+1))

        sum1=sum
        print(i,sum,sum1)


Непонятно в чем проблема:
    def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i
        return result

def task8():
    EPS = 0.001
    x = float(input('Введите x: '))
    m = int(input('Введите конечное число: '))
    h = m + 1
    for i in range(1, m + 1):
        sum = x+(-1)**i*((x-1)**(2*i+1)/factorial(2*i+1))
    for i in range(1, h + 1):
        sum1 = x + (-1) ** i * ((x - 1) ** (2 * i + 1) / factorial(2 * i + 1))
    while (abs(sum - sum1) >= EPS):
        print(i,sum1,sum)
task8()

Непонятно в чем проблема 2:
     def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i
        return result

def task8():
    EPS = 0.001

    x = float(input('Введите x: '))
    m = int(input('Введите конечное число: '))
    for i in range(1, m + 1):
        sum = x+(-1)**i*((x-1)**(2*i+1)/factorial(2*i+1))
    for i in range(1, m + 2):
        sum1 = x + (-1) ** i * ((x - 1) ** (2 * i + 1) / factorial(2 * i + 1))
        if sum1-sum >= EPS:
            print(sum1,sum)
task8()



     
Готовое 8 задание но без Эпс
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i
        return result

def task8():

    x = float(input('Введите x: '))
    m = int(input('Введите конечное число: '))

    for i in range(1, m+1):

        sum=x+(-1)**i*((x-1)**(2*i+1)/factorial(2*i+1))

        print(i,sum)
task8()
    
6 задание 
def rabbits_of_the_year(months):
    if months == 1 or months == 2:
        return 1
    else:
        return rabbits_of_the_year(months-1)+rabbits_of_the_year(months-2)
def task6():
    h = float(input('Введите количество месяцев: '))
    quantity_rabbits = rabbits_of_the_year(h)
    print(quantity_rabbits)
task6()


9 задание 
def task9_1():
    current_sum = 0
    for i in range(1,8):
        for j in range(i):
            current_sum += (j+2*i-1)

    print(current_sum)
task9_1()
    
