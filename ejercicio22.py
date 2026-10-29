#Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado. 
nota=int(input("Introduce la nota"))

if nota>5:
 print ("Has Aprobado")
if nota<5:
 print("Has suspendido")
 if nota==5:
  print("Has Aprobado")