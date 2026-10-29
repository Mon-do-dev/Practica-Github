# Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
from math import  sqrt

#Pedir coeficientes
a = float(input('Dame el valor del coeficiente a: '))
b = float(input('Dame el valor del coeficiente b: '))
c = float(input('Dame el valor del coeficiente c: '))

discriminante =  b * b - 4 * a * c

if discriminante < 0:
    print('La ecuación no tiene solución.')
raiz=sqrt(discriminante)
x_1 = (-b + raiz) / (2 * a)     # calculamos una primera solución
if discriminante != 0:          # comprobamos si hay otra solución
    x_2 = (-b - raiz) / (2 * a) # calculamos la segunda solución
