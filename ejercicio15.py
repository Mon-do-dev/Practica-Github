# Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.


import math
radio = float(input("Ingrese el valor del radio del cilindro: "))
altura = float(input("Ingrese el valor de la altura del cilindro: "))
area = 2 * math.pi * radio * altura + 2 * math.pi * radio ** 2
volumen = math.pi * radio ** 2 * altura
print("El área del cilindro es:", round(area, 2))
print("El volumen del cilindro es:", round(volumen, 2))