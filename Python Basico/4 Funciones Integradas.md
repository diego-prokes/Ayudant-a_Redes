# Funciones Integradas

[TOC]

## Introducción

La librería estándar de Python, incluída en cualquier instalación de Python, cuenta con varias funciones integradas que pueden facilitar mucho le realización de ciertas acciones. Siempre que existe una función integrada será preferible a hacerla por tu cuenta.

## Funciones de parámetros numéricos

### abs()

Valor absoluto de un número (distancia):

```python
print(abs(-10)) # 10
```

### round()

Redondeo de un flotante a entero, menor de .5 a la baja, mayor o igual a .5 al alza:

```python
print(round(5.5)) # 6
print(round(5.4)) # 5
```

### divmod()

Debe recibir dos argumentos numéricos, y devuelve dos valores: resultado de la división entera, y el resto.

```python
print(divmod(22, 4)) # (5, 2)
```

### max()

Si recibe más de un argumento, devuelve el mayor de ellos.

```python
print(max(23, 12, 145, 88))       # 145
print(type(max(23, 12, 145, 88))) # <type 'int'>
```

### min()

Si recibe más de un argumento, devuelve el menor de ellos.

```python
print(min(23, 12, 145, 88))       # 12
print(type(min(23, 12, 145, 88))) # <type 'int'>
```

### pow()

La función `pow()` si recibe 2 argumentos, eleva el primero argumento a la potencia del segundo argumento.

```
x = pow(2, 3)
y = pow(10, 2)
z = pow(10, -2)

print(x)        # x = 8
print(y)        # y = 100
print(z)        # z = 0.01
```



## Funciones de parámetros String

### eval()

Evalúa una cadena como una expresión, acepta variables si se han definido anteriormente:

```python
print(eval('2 + 5'))      # 7
n = 10
print(eval('n * 10 - 5')) # 95
```

### len()

Longitud de una colección o cadena:

```python
print(len("Una cadena")) # 10
print(len(""))           # 0
```

### max()

Si recibe más de un argumento, devuelve el mayor de ellos.

```python
print(max("a", "Z"))              # 'a'
print(type(max("a", "Z"))         # <type 'str'>
```

### min()

Si recibe más de un argumento, devuelve el menor de ellos.

```python
print(min("a", "Z"))              # 'Z'
print(type(min("a", "Z"))         # <type 'str'>
```



## Bibliografía

[Funciones integradas](https://docs.hektorprofe.net/python/programacion-de-funciones/funciones-integradas/)

[Funciones Integradas](https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion5/funciones_integradas.html)

