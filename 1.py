from math import *

def task1():
  pass
#задание 1
x = float(input("Введите переменную x:"))
y = float(input("Введите переменную y:"))
z = float(input("Введите переменную z:"))
a = sqrt(x*y/(x+y)*(x-y))-pi/2
b = (abs(x))**(1/5)+sin(y)+atan(x)-log10(1+z)
print('a=',a)
print('b=',b)

#задание 2
x = float(input("Введите переменную x:"))
a = 1
b = -3
f = (((x)**2)**(1/3)/x+a)+x**b
print('f=',f)

#задание 3
x = float(input("Введите переменную x:"))
f = 2*(-x)-((math.cosh(x)+math.sinh(2x))*(1/3)
print('f=',f)

#задание 4
volumepyr = float(input("Введите значение объёма пирамиды:"))
perimeter = float(input("Введите значение периметра основания:"))
height = float(input("Введите значение высоты пирамиды:"))
squarecircle= float(input("Введите значение радиуса круга:"))
k = float(input("Введите значение отношения высоты пирамиды к радиусу основания:"))
radius = height/k
volumecone =1/3*pi*(radius**2)*height
print('Объём конуса равен=',volumecone)

#задание 5
velocity1 = float(input("Введите скорость первого автомобиля:"))
velocity2 = float(input("Введите скорость второго автомобиля:"))
distance1 = float(input("Введите начальное расстояние между автомобилями:"))
time = float(input("Введите время движения:"))
velocity = velocity1+velocity2
distance2 = velocity*time
distance = distance1+distance2
print('Расстояние между автомобилями равно=',distance)

        #задание 6
baseside = float(input("Введите значение стороны основания призмы:"))
square = float(input("Введите значение площади боковой грани:"))
height = square/baseside
radiuscircle = (baseside/sqrt(2))
radiussphere = (sqrt((height/2)**2+radiuscircle**2))
print('Радиус сферы описанной около четырехугольной призмы равен=',radiussphere)



from math import *

def task1():
    x = float(input("Введите переменную x:"))
    y = float(input("Введите переменную y:"))
    z = float(input("Введите переменную z:"))

    a = sqrt(x*y/(x+y)*(x-y))-pi/2
    b = (abs(x))**(1/5)+sin(y)+atan(x)-log10(1+z)

    print("{0:.4f} text {1:.4f}".format(a, b))
task1()

def task2():
    x = float(input("Введите переменную x:"))

    a = 1
    b = -3
    f = (((x)**2)**(1/3)/x+a)+x**b

    print("{0:.4f} text {1:.4f}".format(f))
task2()

def task3():
    x = float(input("Введите переменную x:"))

    f = 2*(-x)-((cosh(x)+sinh(2*x)))*(1/3)
    print("{0:.4f} text {1:.4f}".format(f))
task3()

def task4():
    volumepyr = float(input("Введите значение объёма пирамиды:"))
    perimeter = float(input("Введите значение периметра основания:"))
    height = float(input("Введите значение высоты пирамиды:"))
    squarecircle= float(input("Введите значение радиуса круга:"))
    k = float(input("Введите значение отношения высоты пирамиды к радиусу основания:"))
    radius = height/k
    volumecone =1/3*pi*(radius**2)*height
    print("{0:.4f} text {1:.4f}".format(volumecone))
task4()

def task5():
    velocity1 = float(input("Введите скорость первого автомобиля:"))
    velocity2 = float(input("Введите скорость второго автомобиля:"))
    distance1 = float(input("Введите начальное расстояние между автомобилями:"))
    time = float(input("Введите время движения:"))
    velocity = velocity1+velocity2
    distance2 = velocity*time
    distance = distance1+distance2
    print("{0:.4f} text {1:.4f}".format(distance))
task5()

def task6():
    baseside = float(input("Введите значение стороны основания призмы:"))
    square = float(input("Введите значение площади боковой грани:"))
    height = square/baseside
    radiuscircle = (baseside/sqrt(2))
    radiussphere = (sqrt((height/2)**2+radiuscircle**2))
    print("{0:.4f} text {1:.4f}".format(radiussphere))
task6()

def task7():
    A1 = float(input("Введите переменную A1:"))
    B1 = float(input("Введите переменную B1:"))
    C1 = float(input("Введите переменную C1:"))
    A2 = float(input("Введите переменную A2:"))
    B2 = float(input("Введите переменную B2:"))
    C2 = float(input("Введите переменную C2:"))
    A1, B1, C1, A2, B2, C2 in range(-10, 10)
    D = A1*B2-A2*B1
    x = (C1*B2-C2*B1)/D
    y = (A1*C2-A2*C1)/D
    A1*x+B1*y=C1
    A2*x+B2*y=C2
    print("{0:.4f} text {1:.4f}".format())
task7()
