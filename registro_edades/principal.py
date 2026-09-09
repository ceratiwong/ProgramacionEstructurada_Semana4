import edades

def main():
    cantidad_edades = int(input("Ingrese la cantidad de edades a registrar: "))
    for i in range(cantidad_edades):
        edades.registrar_edades()
        edades.mostrar_edades()

main()