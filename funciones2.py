def calcular_pago(horas, tarifa):
    pago = horas * tarifa
    print("Pago dentro de la función: C$", pago)


calcular_pago(40, 120)

# La siguiente instrucción produciría NameError:
# print(pago)