#!/usr/bin/python
from math import sqrt
a=float(raw_input('Valor de a: '))
b=float(raw_input('Valor de b: '))
c=float(raw_input('Valor de c: '))
if (a==0)and(b==0)and(c==0):
  print'La ecuacion tiene infinitas soluciones'
 elif (a==0)and(b==0)
   print'La ecuacion no tiene soluciones'
  
 elif (a==0)
   x=-c/b
   print'La solucion de la ecuacion es: x%4.3f'%x
else:
   x1= (-b+sqrt(b**2-4*a*c))/(2*a)
   x2= (-b-sqrt(b**2-4*a*c))/(2*a)