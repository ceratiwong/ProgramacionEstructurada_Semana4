#Registro de estudiantes
"""
Registrar notas de n cantidad de estudiantes
"""

notas = []

def agregar_notas(nota):
    notas.append(nota)

def mostrar_notas():
    return notas

def evaluar_notas():
    for nota in notas:
        if nota >= 70:
            print(f"{nota}, es aprobado.")
        else:
            print(f"{nota}, es reprobado.")

