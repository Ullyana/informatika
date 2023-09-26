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


