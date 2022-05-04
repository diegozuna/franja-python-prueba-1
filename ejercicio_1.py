#ejercicio 1
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
#Escribe un programa que comience leyendo el número de barras vendidas que no son del día. Después tu programa debe 
#mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

precio_real = 3.49
precio_desc = 1.396
precio_desc = round(precio_desc, 3)
cant_barras = input("Ingrese barras de pan que no son del dia: ")
cant_barras = float(cant_barras)
precio_total = precio_desc * cant_barras
precio_total = round(precio_total,2)
precio_reals = precio_real * cant_barras
precio_reals = round(precio_reals,2)
precio_reals = str(precio_reals)
precio_real = str(precio_real)
precio_desc = str(precio_desc)
precio_total = str(precio_total)
print("PRECIO HABITUAL POR PAN: "+precio_real+"€")
print("PRECIO SIN DESCUENTO: "+precio_reals+"€")
print("DESCUENTO TOTAL POR PAN: "+precio_desc+"€")
print("COSTO TOTAL: "+precio_total+"€" )