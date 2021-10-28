# Recibo la data
num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro numero entero: "))

# Creo variables auxiliares vacías
mayor = ""
menor = ""

# Veo cuál es el número mayor y el menor
if(num1 > num2):
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

# Verifico que el número menor sea distinto de cero
if(menor == 0):
    print('error')
else:
    cuociente = mayor/menor
    print(cuociente)