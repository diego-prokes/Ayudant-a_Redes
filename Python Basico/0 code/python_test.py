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