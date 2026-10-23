#El usuario introduze un numero por tecla del 1 al 10 y el ordenador piensa en un numero al azar y si acierta saldra por texto si es correcto o no

import random
var_random=random.randint(1,5)
var_usuario=int(input("Ingrese un numero del 1 al 5: "))

if var_usuario in [1,2,3,4,5]:
    if int (var_usuario)==var_random:
        print ("fallaste")
    else:
        print("acertaste")
else:
    print("no has introducido el rango correcto")
