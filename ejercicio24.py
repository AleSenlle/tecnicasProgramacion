"""Se requiere un algoritmo que solicite ingresar:
a. Importe de ventas de refacciones.
b. Importe de ventas de servicio.
c. Importe de ventas de autos y camiones.
Calcule el importe total sumando los tres importes anteriores y el promedio de ventas y muestre al usuario los resultados de este cálculo.
Si el promedio de ventas es mayor o igual a $50.000 deberá mostrar el mensaje: “Se alcanzó el objetivo” 
de lo contrario deberá mostrar el mensaje “Buscar nuevas estrategias de ventas”.
"""
importeRefacciones=float(input("Ingresar el importe de ventas de refacciones: "))
importeServicio = float(input("Ingresar el importe de ventas de servicios: "))
importeAutosCamiones = float(input("Ingresar el importe de ventas de autos y camiones: "))
importeTotal=importeRefacciones + importeServicio+ importeAutosCamiones
promedio = importeTotal/3
if promedio >= 50000:
    print("Se alcanzo el objetivo")
else:
    print("Hay que buscar nuevas estrategias de venta")
