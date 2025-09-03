# Definición de la matriz 3D para almacenar datos de temperatura
# Dimensiones: ciudades, semanas, días de la semana
# La estructura es: [ciudad][semana][dia]
temperaturas = [
    [  # Ciudad 1: Quito
        [20, 21, 22, 23, 24, 25, 26],  # Semana 1 (Lunes a Domingo)
        [21, 22, 23, 24, 25, 26, 27],  # Semana 2
        [22, 23, 24, 25, 26, 27, 28]   # Semana 3
    ],
    [  # Ciudad 2: Guayaquil
        [28, 29, 30, 31, 32, 33, 34],  # Semana 1
        [29, 30, 31, 32, 33, 34, 35],  # Semana 2
        [30, 31, 32, 33, 34, 35, 36]   # Semana 3
    ],
    [  # Ciudad 3: Cuenca
        [15, 16, 17, 18, 19, 20, 21],  # Semana 1
        [16, 17, 18, 19, 20, 21, 22],  # Semana 2
        [17, 18, 19, 20, 21, 22, 23]   # Semana 3
    ]
]

# Nombres para las ciudades, para que la salida sea más clara
ciudades = ["Quito", "Guayaquil", "Cuenca"]
# Sección 2: Cálculo del promedio con bucles anidados

print("Calculando el promedio de temperaturas por ciudad y semana:")

# Bucle externo para recorrer cada ciudad
for i in range(len(temperaturas)):
    # Bucle intermedio para recorrer las semanas de cada ciudad
    for j in range(len(temperaturas[i])):
        # Inicializar la suma de la semana
        suma_semana = 0

        # Bucle interno para sumar las temperaturas de cada día de la semana
        for k in range(len(temperaturas[i][j])):
            suma_semana += temperaturas[i][j][k]

        # Calcular el promedio de la semana
        promedio_semana = suma_semana / len(temperaturas[i][j])

        # Mostrar el resultado
        print(f"  > <El promedio de la semana {j + 1} en {ciudades[i]} es: {promedio_semana:.2f}°C")