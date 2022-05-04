#ejercicio 2
#Escribir un programa que le pregunte al usuario una cantidad a invertir, el interés porcentual anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión redondeado a dos decimales.

cant_invertida = input("Ingrese la cantidad que desea invertir: ")
cant_invertida = float(cant_invertida)
interes = input("Ingrese el porcentaje de interes anual: ")
interes = float(interes)
interes = interes/100
tiempo = input("Ingrese cantidad de años: ")
tiempo = int(tiempo)
total = (cant_invertida * tiempo * interes) + cant_invertida
total = str(total)
print("El capital obtenido es de: "+total)