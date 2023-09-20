from cmath import *

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
