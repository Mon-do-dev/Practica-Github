#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10 
num1 = float(input("Introduce el primer número (0-10): "))
while num1 < 0 or num1 > 10:
    print("Número fuera de rango. Por favor, introduce un número entre 0 y 10.")
    num1 = float(input("Introduce el primer número (0-10): "))

num2 = float(input("Introduce el segundo número (0-10): "))
while num2 < 0 or num2 > 10:
    print("Número fuera de rango. Por favor, introduce un número entre 0 y 10.")
    num2 = float(input("Introduce el segundo número (0-10): "))

if num1 > num2:
    print("El primer número es mayor que el segundo.")
elif num1 < num2:
    print("El primer número es menor que el segundo.")
else:
    print("Los dos números son iguales.")
