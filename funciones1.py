#Reasignar un parámetro inmutable

def aumentar(monto):
    monto += 1
    return monto

monto = 12
print(aumentar(monto))
print(monto)