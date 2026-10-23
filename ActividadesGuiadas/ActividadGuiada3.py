#Calculo de la longitud y el áreaº  

import math
var_radio=float(input("Ingrese el valor del radio: "))

var_area=math.pi * var_radio**2
var_longitud=2 * math.pi * var_radio

print(var_area)
print(var_longitud)

print(f"El área es: {var_area:.2f}")
print("El area es: ",round(var_area,2))
print(f"La longitud es: {var_longitud:.2f}")
print("La longitud es: ",round(var_longitud,2))

#Metodos de redondeo
print(math.ceil(var_area))
print (round(var_area,2))
print (math.floor(var_area))
print(f"El resultado es: {var_area:.2f}")