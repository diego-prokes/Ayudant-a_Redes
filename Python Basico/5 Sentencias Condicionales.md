# Sentencias Condicionales

Hasta ahora hemos aprendido a escribir un programa que hace exactamente lo que le decimos que haga. Sin embargo, a menudo desearemos que este reaccione a distintas situaciones. Por ejemplo, cuando jugamos un videojuego de plataformas (el que claramente fue programado) deseamos que al presionar la flecha hacia la derecha, el personaje se mueva en esta dirección. Para conseguir esto, podemos usar las sentencias condicionales.

```python
# Las sentencias condicionales le permiten al programa ejecutar un bloque de código sólo si una condición se cumple.

# Su sintaxis es la siguiente:
# if( <condición> ):
# 	<bloque_de_código>
```

En python un bloque de código se reconoce por su indentación (TAB).

```python
# Puede elegirse entre múltiples condiciones mediante la siguiente sintaxis

# Su sintaxis es la siguiente:
# if( <condición> ):
# 	<bloque_de_código>
# elif( <otra_condición> ):
# 	<otro_bloque_de_código>
# else:
# 	<bloque_de_código>

#Ejemplo
x = 10
if (x == 15):
    print("El valor es: ")
    print(x)
elif ( x == 5):
    print("El valor es: ")
    print(x)
print("El valor no calza con las condiciones del programa")
# else:
#     print("El valor es: ")
#     print(x)
```

Dependiendo del caso puede omitirse la instrucción `else:`.

