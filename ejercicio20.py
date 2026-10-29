#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10 

numero1= int(input ("Introduce un numero"))
numero2= int(input("Introduce otro numero"))

if numero1 or  numero2 in[1,2,3,4,5,6,7,8,9,10]:
   if numero1>numero2:
       print("El mayor es:"' numero 1')
   if numero2>numero1:
       print("El mayor es:"' numero 2')
else:
    print("no has introducido el rango correcto")