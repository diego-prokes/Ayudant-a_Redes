# Operadores

[TOC]

## Introducción

Los **operadores** son símbolos **que** representan una acción a realizar con los elementos **que** se encuentran antes o después. La función de cada operador depende del tipo de dato que se esté utilizando. Por ejemplo, el operador de suma en python es "+". Sin embargo, este será el caso solamente si los elementos que se encuentran antes y después de él son número, decimales o enteros. Veremos esto en profundidad más adelante.

## Operadores Algorítmicos

Los operadores algorítmicos son operadores que realizan acciones sobre números, ya sea enteros o decimales.

| Operador | Acción                         |
| -------- | ------------------------------ |
| **–**    | **Resta**                      |
| **+**    | **Suma**                       |
| *****    | **Multiplicación**             |
| **/**    | **División**                   |
| **//**   | **División entera o cociente** |
| **%**    | **Módulo o resto**             |
| ******   | **Potencia**                   |

```python
# Los operadores aritméticos son los siguientes
x = 5 - 3
print("5 - 3 = ", x)  # x = 2
x = 2 + 3
print("2 + 3 = ", x)  # x = 5
x = 2 * 3
print("2 * 3 = ", x)  # x = 6
x = 6 / 2
print("6 / 2 = ", x)  # x = 3
x = 7 / 2
print("7 / 2 = ", x)  # x = 3
x = 7 % 3
print("7 % 3 = ", x)  # x = 1
x = 2 ** 5
print("7 ** 5 = ", x) # x = 32
```

```python
# Si se escribe una expresión que debe operar más de una vez seguirá la siguiente preponderancia
# 1. Potencia
# 2. Multiplicación, división, Cociente y Módulo
# 3. Suma y resta
# 4. Lectura de izquierda a derecha
x = 3 * 2 ** 3 + 1
print(x) # x = 25

# Aún así es recomendable encerrar entre paréntesis aquellas operaciones que deben realizadas primero. Esto es importante porque habrán veces en las que sea necesario y otras en que mejore la legibilidad.
x = (3 * (2 ** 3)) + 1
print(x)
```

## Operadores de Asignación

Los operadores de asignación sirven para asignarle un valor a una variable.

| **Operador** | **Acción**                 |
| ------------ | -------------------------- |
| **=**        | **Asignación Básica**      |
| ***=**       | **Asigna Producto**        |
| **/=**       | **Asigna División**        |
| **//=**      | **Asigna División Entera** |
| **+=**       | **Asigna Suma**            |
| **-=**       | **Asigna Resta**           |
| **%=**       | **Asigna Modulo**          |

```python
x = 5     # x = 5
x += 5    # x = 10
x -= 2    # x = 8
x *= 10   # x = 80
x //= 2   # x = 40
x /= 4    # x = 10.0
x %= 9    # x = 1.0
print(x)
```

## Otros Operadores

Existen más operadores, pero considero que son más avanzados y serán vistos más adelantes. Sin embargo, puedes encontrarlos en la bibliografía al final del archivo.

## Bibliografía

[Números y operaciones aritméticas elementales](https://www.mclibre.org/consultar/python/lecciones/python-operaciones-matematicas.html)

[Qué son los operadores y los tipos que existen](https://yosoy.dev/que-son-los-operadores-y-los-tipos-que-existen/)

[Precedencia de operadores](https://interactivechaos.com/es/manual/tutorial-de-python/precedencia-de-operadores)

