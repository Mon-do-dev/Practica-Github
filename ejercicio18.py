 #Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan una promoción en la que los menores de 18 años pagan la mitad del precio de la entrada y los adultos el 90% del precio. Realiza un programa que calcule el total a pagar, introduciendo por teclado el número de menores y adultos que van a ver la película. El precio de la entrada es de 12 euros.

precio_entrada = 12
num_menores = int(input("Ingrese el número de menores de 18 años: "))
num_adultos = int(input("Ingrese el número de adultos: "))
total_menores = num_menores * precio_entrada * 0.5
total_adultos = num_adultos * precio_entrada * 0.9
total_pagar = total_menores + total_adultos
print("El total a pagar es:", total_pagar, "euros.")
