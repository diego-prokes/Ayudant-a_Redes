# Recibo la data
te = int(input("Ingrese la cantidad de te: "))
galletas = int(input("Ingrese la cantidad de galletas: "))
sandwich = int(input("Ingrese la cantidad de sandwich: "))
nombre = input("Ingrese su nombre: ")
pagado = int(input("Ingrese lo pagado: "))

# Manejo de datos
total = te*600 + galletas*300 + sandwich*800

# Salida de datos
if(total < pagado):
    print("CLIENTE", nombre)
    print("TOTAL =", total)
    print("PAGADO =", pagado)
    print("VUELTO =", pagado-total)
else:
    print("El monto pagado no es suficiente para realizar esta compra.")