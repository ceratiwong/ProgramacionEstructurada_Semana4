def agregar_producto(inventario, producto):
    inventario.append(producto)


productos = ["arroz", "aceite"]
agregar_producto(productos, "café")

for producto in productos:
    print(producto)

#UTILICÉ EL CICLO FOR PARA IMPRIMIR LOS PRODUCTOS SIN LOS CORCHETES NI COMILLAS SIMPLES.