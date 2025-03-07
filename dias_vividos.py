# Solicitar el nombre del usuario
nombre = input("¿Cuál es tu nombre? ")

# Solicitar la edad del usuario y convertirla a entero
edad = int(input("¿Cuántos años tienes? "))

# Calcular cuántos días ha vivido
dias_vividos = edad * 365

# Mostrar el resultado
print(f"{nombre}, has vivido aproximadamente {dias_vividos} días.")
