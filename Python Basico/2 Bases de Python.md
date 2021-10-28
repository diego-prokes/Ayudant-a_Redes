# Bases de Python

[TOC]

## Hola Mundo

El primer programa que uno hace en todos los lenguajes de programación es: "Hola Mundo!". El objetivo de este programa

```python
print("Hola Mundo!")
```

## Comentarios

```python
# Para hacer comentarios en Python debe anteponerse al texto un gato ("#")
```

## Variables

```python
# EXPLICACIÓN BÁSICA DE VARIABLES #

# Una variable se puede entender como una especie de caja en la que se puede guardar un dato. Esa caja suele corresponder a una posición de memoria en la memoria del ordenador.
# Las variables se representan mediante letras o palabras completas: x, y, nombre, nombres_apellidos, etc.

# La sintaxis para definir y asignar un valor a una variable es la siguiente
# <nombre_variable> = <valor>

# Ejemplos
a = 2
nombre = "Diego"
lista_compras = ["pan","queso","huevo"]

# La sintaxis para liberar el espacio en memoria que ocupa una variable (eliminarla) es:
# del <nombre_variable>

#Ejemplo
del a
```

```python
# NOMBRES DE VARIABLES #

# Aunque no es obligatorio, se recomienda que el nombre de la variable esté relacionado con la información que se almacena en ella, para que sea más fácil entender el programa. Si el programa es trivial o mientras se está escribiendo un programa, esto no parece muy importante, pero si se consulta un programa escrito por otra persona o escrito por uno mismo pero hace tiempo, resultará mucho más fácil entender el programa si los nombres están bien elegidos.
# El nombre de una variable debe empezar por una letra o por un guion bajo (_) y puede seguir con más letras, números o guiones bajos.
# Hay algunos nombres que no están permitidos, ya que son palabras reservadas en python.
# Python es case sensitive
# Se recomienda separar palabras por guiones, pero también sirve camelCase.

# Ejemplos
nombre = "diego"
Nombre = "Diego"
_x = 10
nombres_apellidos = "Diego Maradona"
nombresApellidos = "Ada Lovelace"
lugar_1 = "Brasil"
lugar_2 = "Argentina"
```

## Redefinir el valor de una variable

```python
# Cuando una variable ya ha sido declarada y se le ha asingado un valor, (es decir, ha sido definida), se le puede reasignar un nuevo valor

numero_1 = 10
print(numero_1)   # 10
numero_1 = 5
print(numero_1)   # 5
numero_1 = 25 - 5
print(numero_1)   # 20
```



## Tipos de Datos

```python
# TIPOS DE DATOS BÁSICOS #

# Las variables almacenan datos. Estos datos pueden ser de distintos tipos:
#  +-----------------+------------+
#  | Número Entero   |    int     |
#  | Número Decimal  |    float   |
#  | Caracter        |    chr     |
#  | Cadena de texto |    str     |  Un string es una lista de carácteres
#  | booleano        |    bool    |
#  +-----------------+------------+

entero = 10
decimal = 10.0

un_caracter = '$'
otro_caracter = '10'
otro_caracter_2 = 'a'
otro_caracter_3 = chr(125) # ASCII
cadena_texto = "Hola Mundo!"

booleano = True
booleano_2 = False

# Si se quiere conocer el tipo de dato de una variable podemos ayudarnos de la función type()
print("\n")
print("La variable 'entero' almacena el valor: ", entero, " y es del tipo: ", type(entero))
print("La variable 'decimal' almacena el valor: ", decimal, " y es del tipo: ", type(decimal))
print("\n")
print("La variable 'un_caracter' almacena el valor: ", un_caracter, " y es del tipo: ", type(un_caracter))
print("La variable 'otro_caracter' almacena el valor: ", otro_caracter, " y es del tipo: ", type(otro_caracter))
print("La variable 'otro_caracter_2' almacena el valor: ", otro_caracter_2, " y es del tipo: ", type(otro_caracter_2))
print("La variable 'otro_caracter_3' almacena el valor: ", otro_caracter_3, " y es del tipo: ", type(otro_caracter_3))
print("La variable 'cadena_texto' almacena el valor: ", cadena_texto, " y es del tipo: ", type(cadena_texto))
print("\n")
print("La variable 'booleano' almacena el valor: ", booleano, " y es del tipo: ", type(booleano))
print("La variable 'booleano_2' almacena el valor: ", booleano_2, " y es del tipo: ", type(booleano_2))

```

## Conversión entre Tipos de Datos

Existen funciones que le permiten al usuario convertir tipos de datos.

```python
# Existen alguns funciones predeterminadas en Python que permiten transformar un tipo de dato en otro:
entero = 80
decimal = 6.14159
caracter = 'Q'
cadena = 'Análisis Numérico'
booleano = True

# Tanto los valores Decimales como los Booleanos pueden ser convertidos en Enteros con la función int():
print(int(decimal))  # 6
print(int(True))     # 1
print(int(False))    # 0

# Algo similar ocurre al intentar convertir Enteros o Booleanos en Decimales con la función float():
print(float(entero)) # 80.0
print(float(True))   # 1.0
print(float(False))  # 0.0

# Es posible también, a partir de la tabla de caracteres ASCII, obtener el caracter correspondiente a un entero con chr() o viceversa con ord():
print(chr(entero))   # P
print(ord(caracter)) # 81

#Mucho más interesante que esto último resulta la conversión de cualquiera de los tipos de datos presentados en cadenas de texto, algo de vital importancia a la hora de presentar resultados combinándolos con texto.
print(str(entero))   # 80
print(str(decimal))  # 4.14159
print(str(booleano)) # True
```

## Tipos de datos complejos

Los tipos de datos complejos se constituyen de los tipos de datos presentados en este documento. Son las listas, las tuplas y los diccionarios. Sin embargo, aún no las veremos, pues no considero que formen parte de las bases de python.

## Bibliografía

[Variables en Python y Tipos de datos](https://www.mclibre.org/consultar/python/lecciones/python-variables.html)

[Tipos de Datos y Conversión de Tipos en Python](https://ingsosa.com/tipos-de-datos-en-python/)

