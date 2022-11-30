"""Se requiere de un algoritmo que calcule la tabla de multiplicar del número que el usuario desee."""
numero=int(input("ingrese un numero: "))
contador=0
while contador <= 10:
    resultado=numero*contador
    print("{} * {} = {}".format(numero,contador,resultado))
    contador=contador+1
