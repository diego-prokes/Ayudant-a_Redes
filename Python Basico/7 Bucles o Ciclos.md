# Bucles o Ciclos

[TOC]

## Introducción

Las sentencias condicionales son una forma de alterar el flujo de ejecución del programa. Mas no son los únicos. Los **bucles o ciclos** le permiten al programa realizar una acción varias veces, sin tener que repetir el código la cantidad de veces que quiera hacerse.

```python
# Ejercicio de Ejemplo

# Escriba un programa que imprima en la consola los números del 0 al 9
# Lo forma de hacer esto sin ciclos es la siguiente

print(0)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)

```

## Ciclos

### Ciclo While

El ciclo while se lee como: 

***Mientras <esta condición> sea verdadera, debe ejecutarse una y otra vez el siguiente bloque de código.***

```python
# Sintaxis del ciclo while
# while( <condición>):
# 	<bloque_de_código>

# Ejercicio de Ejemplo
_i = 0
while( _i < 10 ):
    print(_i)
    _i += 1
# La sentencia else es opcional
else:
    print("Ya se han impreso los numeros del 0 al 9")
```

### Ciclo For

El ciclo for es un tanto distinto al ciclo while. En vez de iterar (realizar cierta acción varias veces) mientras se cumpla una condición, el ciclo for recorre una lista de valores y una vez los haya recorrido todos, deja de iterar. Se podría leer como:

***Para <este valor> almacenado en <esta lista de valores>, se ejecuta este bloque de código.***

```python
# Sintaxis del ciclo for
# for <nombre_variable> in <lista_de_valores>:
# 	<bloque_de_código>

# Ejercicio de Ejemplo

# Primera Opción
lista = (0,1,2,3,4,5,6,7,8,9)
for _i in lista:
    print(_i)
print("\n")
# Segunda Opción
for _i in range(10):
    print(_i)
print("\n")
```

## Break & Continue Statement

Las instrucciones `break` y `continue` pueden alterar la ejecución de los ciclos.

### Break Statement

Con la sentencia break podemos detener el bucle en mitad de su ejecución:

```python
# Ejemplo while
_i = 0
while( _i < 10 ):
    print(_i)
    _i += 1
    if(_i == 5):
        print("ejecución interrumpida")
        break
print("Fin del ciclo while \n")
        
# Ejemplo for
for _i in range(10):
    print(_i)
    if(_i == 5):
        break
print("Fin del ciclo for \n")
```

### Continue Statement

Con la sentencia continue podemos detener la iteración actual, y continuar con la siguiente:

```python
# Ejemplo while
_i = 0
while( _i < 10 ):
    _i += 1
    if(_i == 5):
	    print("ejecución interrumpida")
	    continue
    print(_i)
print("Fin del ciclo while \n")
        
# Ejemplo for
for _i in range(10):
    if(_i == 5):
        print("ejecución interrumpida")
    	continue
    print(_i)
print("Fin del ciclo for \n")
```

## Bibliografía

[Python While Loops (w3schools.com)](https://www.w3schools.com/python/python_while_loops.asp)
