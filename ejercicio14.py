# Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería math y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
 


import math
diametro = float(input("Ingrese el valor del diámetro del círculo: "))  
radio = diametro / 2
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print("El área del círculo es:", round(area, 1))
print("El perímetro del círculo es:", round(perimetro, 1))