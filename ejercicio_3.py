#Escribir un programa que haga transformaciones de pesos a dólares. Debe preguntarle al usuario si desea transformar
#de pesos mexicanos a dólares, de pesos chilenos a dólares, o desde pesos argentinos a dólares. Mostrar por pantalla 
#la cantidad de monedas a convertir, la moneda que se convirtió y el monto en dólares.
#Peso Chileno a dólar: 855
#Peso Mexicano a dólar: 20
#Peso Argentino a dólar: 115

print("Ingrese la moneda que desea cambiar:")
opc = input("1)Pesos Chilenos \n2)Pesos Mexicanos \n3)Pesos argentinos\n")
opc = int(opc)
if (opc == 1) : 
    valor = 855.0 
    mon = "Peso Chileno"
if (opc == 2) : 
    valor = 20.0
    mon = "Peso Mexicano"
if (opc == 3) : 
    valor = 115.0
    mon = "Peso Argentino"
cantidad = input("Ingrese cantidad que desea cambiar: ")
cantidad = float(cantidad)
total = cantidad/valor
total = str(total)
cantidad = str(cantidad)
print("Cantidad a convertir: " + cantidad +"\nMoneda base: " +mon+"\nMonto en Dolares: "+total)