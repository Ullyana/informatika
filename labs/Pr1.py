from math import *

def task1():
    x = float(input("Введите переменную x:"))
    y = float(input("Введите переменную y:"))
    z = float(input("Введите переменную z:"))

    a = sqrt(x*y/(x+y)*(x-y))-pi/2
    b = (abs(x))**(1/5)+sin(y)+tan(x)-log10(1+z)

    print("a = {0:.4f}, b = {1:.4f}".format(a, b))
task1()

def task2():
    x = float(input("Введите переменную x:"))

    a = 1
    b = -3
    f = (x**(2/3)/(x+a))+x**b

    print("f(x)={0:.4f}".format(f))
task2()

def task3():
    x = float(input("Введите переменную x:"))

    f = 2**(-x)-((cosh(x)+sinh(2*x)))**(1/3)

    print("f(x)= {0:.4f}".format(f))
task3()

def task4():
    height = float(input("Введите значение высоты пирамиды:"))
    k = float(input("Введите значение отношения высоты пирамиды к радиусу основания:"))

    radius = height/k
    volumecone =1/3*pi*(radius**2)*height

    print("volumecone = {0:.4f}".format(volumecone))
task4()

def task5():
    velocity1 = float(input("Введите скорость первого автомобиля:"))
    velocity2 = float(input("Введите скорость второго автомобиля:"))
    distance1 = float(input("Введите начальное расстояние между автомобилями:"))
    time = float(input("Введите время движения:"))

    velocity = velocity1+velocity2
    distance2 = velocity*time
    distance = distance1+distance2

    print("distance = {0:.4f}".format(distance))
task5()


def task6():
    baseside = float(input("Введите значение стороны основания призмы:"))
    square = float(input("Введите значение площади боковой грани:"))

    height = square / baseside
    radiuscircle = (baseside / sqrt(2))
    radiusphere = (sqrt((height / 2) ** 2 + radiuscircle ** 2))

    print("radiusphere = {0:.4f}".format(radiusphere))
task6()

def task7():
    A1 = float(input("Введите переменную A1:"))
    B1 = float(input("Введите переменную B1:"))
    C1 = float(input("Введите переменную C1:"))
    A2 = float(input("Введите переменную A2:"))
    B2 = float(input("Введите переменную B2:"))
    C2 = float(input("Введите переменную C2:"))

    D = A1*B2-A2*B1
    x = (C1*B2-C2*B1)/D
    y = (A1*C2-A2*C1)/D

    print("x = {0:.4f}, y = {1:.4f}".format(x, y))
task7()

def task8():
    N = float(input("Введите количество оборотов :"))
    L = float(input("Введите расстояние от центра оси до края лопасти :"))
    time = 120

    frequency = N/time
    period = 1/frequency
    velocity = 2*pi*L*frequency

    print("частота = {0:.4f}".format(frequency))
    print("период обращения = {0:.4f}".format(period))
    print("линнейная скорость точки = {0:.4f}".format(velocity))
task8()

def task9():
    rate = float(input("Введите количество процентов:"))
    months = float(input("Введите количество месяцев:"))
    initialsum = float(input("Введите сумму вклада:"))

    finalsum = initialsum*rate*30/365*months

    print("финальная сумма = {0:.4f}".format(finalsum))
task9()



