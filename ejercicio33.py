"""Se requiere de un algoritmo que permita el ingreso de las edades de un grupo de personas. 
Una vez cargados todos estos valores informar el promedio de sus edades."""
contador=0
sumaEdades=0
while True:
    contador = contador+1
    edades=float(input("ingrese la edad "))
    sumaEdades=sumaEdades+edades
    
    finalizarIngreso=input("si desea finalizar el ingreso de edades ingrese n: ")
    if finalizarIngreso =="n":
        break
promedio = float(sumaEdades/contador)
print(promedio)