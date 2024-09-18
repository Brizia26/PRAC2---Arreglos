import numpy as np
import time

filas = int(input("¿Cuántos alumnos deseas manejar? "))
columnas = int(input("¿Cuántas materias deseas manejar? "))

alumnos = np.random.randint(0, 101, (filas, columnas))

print(f"Has creado una matriz de {filas} alumnos y {columnas} materias.")

def buscar_calificacion(matriz, alumno, materia):
    if alumno < 1 or alumno > filas or materia < 1 or materia > columnas:
        return "Alumno o materia fuera de rango."
    return matriz[alumno - 1][materia - 1]  

alumno_a_buscar = int(input(f"Introduce el número del alumno (1 a {filas}): "))
materia_a_buscar = int(input(f"Introduce el número de la materia (1 a {columnas}): "))

start_time = time.time()

calificacion = buscar_calificacion(alumnos, alumno_a_buscar, materia_a_buscar)

end_time = time.time()

execution_time = end_time - start_time

print(f"La calificación del alumno {alumno_a_buscar} en la materia {materia_a_buscar} es: {calificacion}")
print(f"El tiempo de ejecución fue de {execution_time:.10f} segundos.")
