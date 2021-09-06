# Entrada de Datos y Excepciones

[TOC]

## Entrada de datos

Ya que tu programa puede decidir qué hacer cuando una variable cumpla o no ciertas condiciones, algo de mucho valor es permitir que el usuario pueda ingresar datos en tu programa. Esto se puede hacer con la función `input()`. 

```python
# Función input()

# La función input() se ejecuta, valga la redundancia, durante la ejecución del programa.
# Le permite al usuario ingresar un string mediante la terminal.
# Si deseas convertir el tipo de dato que recibes puedes usar las funciones int(), float(), chr(), etc.

# Ejemplo
texto = input() # Permite que ingreses texto
print("Tipo: ", type(texto), ". Valor: ", texto)
numero = int(input())
print("Tipo: ", type(numero), ". Valor: ", numero)
```

```python
# También puedes Desplegar un texto en la consola del usuario antes de solicitar el dato
numero_entero = int(input("Ingresa un numero entero: "))
print("Tipo: ", type(numero_entero), ". Valor: ", numero_entero)
```

## Manejo de Excepciones: try & except

Suele pasar que los usuarios ingresan valores que no están permitidos. Por ejemplo, si le solicitas un número y escribe un texto o le agrega un espacio extra sin querer. Para estos casos se usa la pareja de expresiones `try` y `except`. Este curso es de carácter básico y el uso de la pareja `try_except` puede llegar a ser muy complejo si se profundiza, por ende sólo hablaremos de ella de una forma liviana.

```python
# Ejemplo
numero_entero = False

try:
	numero_entero = int(input("Ingresa un numero: "))
    # print(numero_entero)
except ValueError as error:
    print(error)
    print("Los caracteres ingresados no pueden ser leidos como un numero entero.") 

if(numero_entero != False):
    print("El valor ingresado es: ", numero_entero)
```

## Bibliografía

[Python input() Function (w3schools.com)](https://www.w3schools.com/python/ref_func_input.asp)

[Python Data Types (w3schools.com)](https://www.w3schools.com/python/python_datatypes.asp)

[Python Try Except (w3schools.com)](https://www.w3schools.com/python/python_try_except.asp)