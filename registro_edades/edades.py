#Registro de edades de personas, hay que clasificar si son niños, jóvenes, adultos o adultos mayores. Mostrar el más joven y el más anciano.

edades = []

edad_joven = 1000
edad_anciano = 0

def agregar_edades(edad):
    edades.append(edad)

def clasificar_edades(edad):
    if edad > 0 and edad <= 12:
        return "Niño"
    elif edad > 12 and edad <= 17:
        return "Joven"
    elif edad > 17 and edad <= 59:
        return "Adulto"
    elif edad >= 60:
        return "Adulto Mayor"

def joven_anciano(edad):
    global edad_joven, edad_anciano
    if edad < edad_joven:
        edad_joven = edad
        print(f"La persona más joven tiene {edad_joven} años.")
    elif edad > edad_anciano:
        edad_anciano = edad
        print(f"La persona más anciana tiene {edad_anciano} años.")

def registrar_edades():
    while True:
        edad = int(input("Ingrese su edad: "))
        if edad < 0 or edad > 100:
            print("Edad inválida. Intente nuevamente.")
        else:
            agregar_edades(edad)
            break

def mostrar_edades():
    for edad in edades:
        clasificar_edades(edad)
        joven_anciano(edad)