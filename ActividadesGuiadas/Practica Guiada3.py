import random

# Genera un número aleatorio entre 1 y 100, ambos incluidos
numero = random.randint(1, 100)

# Solicita la edad y comprueba que se haya introducido un número entero
edad_texto = input("Introduce tu edad: ")

try:
    edad = int(edad_texto)
except ValueError:
    print("Error: la edad introducida no es un número")
else:
    # Comprueba que la edad esté dentro del intervalo permitido
    if edad < 1 or edad > 100:
        print("Error: la edad debe estar entre 1 y 100 años")
    else:
        # Muestra el número obtenido y asigna el premio correspondiente
        print(f"Número obtenido: {numero}")

        if numero <= 10:
            print("¡Premio especial! Entrada gratuita")
        elif numero <= 30:
            print("Has conseguido un descuento del 50 %")
        elif numero <= 60:
            print("Has conseguido un descuento del 20 %")
        else:
            print("Lo sentimos, esta vez no has conseguido ningún premio")



