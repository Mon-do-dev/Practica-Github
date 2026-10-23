# programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
segundos = int(input("Ingrese el número de segundos: "))
minutos = segundos // 60
horas = minutos // 60
print("Horas:", horas)
print("Minutos:", minutos % 60)
print("Segundos:", segundos % 60)
