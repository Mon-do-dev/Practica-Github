"ejercicio2"
#Espacios en blanco

codigo=input("introduce un codigo:")
codigo=codigo.strip()
mayusculas=codigo.upper()
minusculas=codigo.lower()
longitud=len(codigo)
guion=codigo.count("-")

#codigo=codigo.replace("-","*")
if"TEC"in codigo.upper():
    contiene="SI"
else:
    contiene="NO"
if codigo[-2:]=="25":
    coleccion="SI"
else:
    coleccion="No"

print("Mayusculas:",mayusculas, "/Minúsculas:",minusculas, "/Caracteres:",longitud, "/Guiones:",guion,)