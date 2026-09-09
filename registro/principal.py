import crud 
def leer_datos():
    print("Dime la nota: ")
    nota = int(input())
    crud.agregar_notas(nota)

def menu():
    print("""
1. Ingresar Notas
2. Mostrar Notas
3. Evaluar Notas
0. Salir

Digita una opción válida:
    """)
    opcion = int(input())
    return opcion

def main():
    while True:
        op = menu()
        if op == 1:
            leer_datos()
        elif op == 2:
            print(crud.mostrar_notas())
        elif op == 3:
            crud.evaluar_notas()
        elif op == 0:
            print("Saliendo...")
            break
        else:
            print("Opción inválida, por favor intenta de nuevo.")

main()