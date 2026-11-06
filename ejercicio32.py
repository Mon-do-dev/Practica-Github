#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas

frase = "A quien madruga, Dios le ayuda"
palabras = ["madruga", "Dios", "dios"]

for palabra in palabras:
    if palabra.lower() in frase.lower():
        indice = frase.lower().index(palabra.lower())
        print(f"La palabra '{palabra}' se encuentra en la posición: {indice}")
    else:
        print(f"La palabra '{palabra}' no se encuentra en la frase.")
