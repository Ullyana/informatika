import math as m
x=float(input())
y=float(input())
z=float(input())
a=m.sqrt(x*y/(x+y)*(x-y))-PI/2
b=(abs(x))**(1/5)+m.sin(y)+m.atan(x)-log10(1+z)
print('a=',a)
print('b=',b)

import math as m
x=float(input())
a=1
b=-3
f=(((x)**2)**(1/3)/x+a)+x**b

