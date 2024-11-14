"""
Owen David Loza Quirarte
13/11/2024
Lista de alumnos con calificaciones a promedios. 
"""
from pathlib import Path

def calcular_promedios(entrada, salida):
    archivo_entrada = Path(entrada)
    archivo_salida = Path(salida)
    
    with open(archivo_entrada, "r", encoding="utf8") as f_in:
        with open(archivo_salida, "w", encoding="utf8") as f_out:
            for linea in f_in:
                partes = linea.split()
                nombre = partes[0]
                apellido = partes[1]
                calificaciones = [int(cal) for cal in partes[2:]]
                
                promedio = sum(calificaciones) / len(calificaciones)
                
                # Formateo de salida: APELLIDO en mayúsculas, Nombre, y promedio a un decimal
                linea_salida = f"{apellido.upper()}, {nombre}: {promedio:.1f}\n"
                f_out.write(linea_salida)

# Llamada a la función con los archivos de entrada y salida
calcular_promedios("data/calificaciones.txt", "data/promedios.txt")