#Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print("El primer número es mayor que el segundo.")
elif num1 < num2:
    print("El primer número es menor que el segundo.")
else:
    print("Los dos números son iguales.")