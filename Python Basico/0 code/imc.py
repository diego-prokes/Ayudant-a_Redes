# Ingreso de data
altura = float(input("Ingrese su altura en metros: "))
peso = int(input("Ingrese su peso en kilos: "))
edad = int(input("Ingrese su edad en anios: "))

# Manejo de datos
imc = peso / (altura**2)

# Salida de datos
if(edad<45 and imc<22):
    print("bajo")
elif( (edad<45 and imc>=22) or (edad>=45 and imc<22)):
    print("medio")
elif(edad>=45 and imc >=22):
    print("alto")

