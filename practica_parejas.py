#Práctica de David Alejandro Bermúdez Barberena y Michael Alejandro Wong Espinoza
# --- FUNCIONES Y PROCEDIMIENTOS ---

def calcular_subtotal(precio, cantidad):
    # Variables locales para el cálculo
    subtotal_calculado = precio * cantidad
    return subtotal_calculado


def calcular_descuento(subtotal):
    # Variable local para almacenar el descuento
    monto_descuento = 0.0
    if subtotal >= 3000:
        monto_descuento = subtotal * 0.08  # 8% de descuento
    return monto_descuento


def calcular_iva(monto_con_descuento):
    # Variable local para el IVA
    monto_iva = monto_con_descuento * 0.15  # 15% de IVA
    return monto_iva


def mostrar_factura(producto, subtotal, descuento, iva, total):
    # Procedimiento para imprimir el desglose detallado
    print("-" * 40)
    print("         FACTURA DE COMPRA         ")
    print("-" * 40)
    print(f"Producto:   {producto}")
    print(f"Subtotal:   C$ {subtotal:,.2f}")
    print(f"Descuento: -C$ {descuento:,.2f}")
    print(f"IVA (15%):  C$ {iva:,.2f}")
    print(f"Total:      C$ {total:,.2f}")
    print("-" * 40 + "\n")


def procesar_compra(producto, precio, cantidad):
    # Uso de variables locales para gestionar el flujo de cada compra
    subtotal = calcular_subtotal(precio, cantidad)
    descuento = calcular_descuento(subtotal)
    subtotal_con_descuento = subtotal - descuento
    iva = calcular_iva(subtotal_con_descuento)
    total = subtotal_con_descuento + iva

    # Llamada al procedimiento para mostrar el resultado
    mostrar_factura(producto, subtotal, descuento, iva, total)


# --- PRUEBAS DEL PROGRAMA ---

# Prueba 1: Compra CON descuento (Subtotal >= C$ 3,000)
print("=== CASO 1: COMPRA CON DESCUENTO ===")
procesar_compra(producto="Saco de papas", precio=450.00, cantidad=8)
# Subtotal: 450 * 8 = C$ 3,600 (Aplica 8% de descuento)

# Prueba 2: Compra SIN descuento (Subtotal < C$ 3,000)
print("=== CASO 2: COMPRA SIN DESCUENTO ===")
procesar_compra(producto="Bolsa de rábanos", precio=250.00, cantidad=4)
# Subtotal: 250 * 4 = C$ 1,000 (No aplica descuento)