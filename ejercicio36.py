"""//36) Se requiere de un algoritmo que permita ingresar los registros de un censo hasta que el censista 
//indique que ya ha cargado todos los resultados.
Cuando esto ocurra, se deberá informar cantidad de personas censadas, 
//el promedio de edad de ellos y cuantas de estas personas cuentan con internet en sus hogares."""
contador = 0
sumaEdades = 0
internet=0
while True:
    finalizarIngreso = input("Si desea finalizar el ingreso de edades presione s: ")
    if finalizarIngreso == "s":
        break
    else:
        contador = contador+1
        edades = float(input("Ingrese la edad: "))
        sumaEdades = sumaEdades+edades
        pInternet=input("Si tiene internet presione s: ")
        if pInternet =="s":
            internet=internet+1
promedio =float(sumaEdades/contador)
print("El promedio de edades es de {}".format(promedio))
print("La cantidad de personas censadas es de {}".format(contador))
print("El numero de personas con internet en su hogar es de {}".format(internet))
