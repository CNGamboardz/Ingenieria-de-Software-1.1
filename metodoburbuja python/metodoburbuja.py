# Método burbuja para calificaciones

def burbuja(calificaciones):
    n = len(calificaciones)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if calificaciones[j] > calificaciones[j + 1]:
                calificaciones[j], calificaciones[j + 1] = calificaciones[j + 1], calificaciones[j]
    return calificaciones


# Inicio de programa
cantidad = int(input("¿Cuántas calificaciones vas a ingresar?: "))

calificaciones = []

for i in range(cantidad):
    calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
    calificaciones.append(calificacion)

print("\nCalificaciones ingresadas:")
print(calificaciones)

calificaciones_ordenadas = burbuja(calificaciones)

print("\nCalificaciones ordenadas (de menor a mayor):")
print(calificaciones_ordenadas)

print("\nCalificación más baja:", calificaciones_ordenadas[0])
print("Calificación más alta:", calificaciones_ordenadas[-1])