# Hacer una calculadora que pueda sumar, restar, dividir o multiplicar


print("Ingrese el tipo de operacion que desea realizar: suma, resta, multiplicacion o division")
operacion = input()
num1 = int(input("Ingrese el primer operando: "))
num2 = int(input("Ingrese el segundo operando: "))
if(operacion == "suma"):
    resultado = num1 + num2
elif(operacion == "resta"):
    resultado = num1 - num2
elif(operacion == "division"):
    resultado = num1 / num2
elif(operacion == "multiplicacion"):
    resultado = num1 * num2
print(resultado)
