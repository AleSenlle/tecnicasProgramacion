"""Se requiere de un algoritmo que lea un número y calcule la suma de los números que le anteceden 
al número leído, desde el 0 en adelante. 
Por ejemplo: si el usuario ingreso el número 5, 
el algoritmo deberá sumar el número 1, 2, 3, 4 y 5."""

numero=int(input("ingrese un numero: "))
num=0
sumatoria=0
while numero>=num:
    sumatoria=sumatoria+num
    num=num+1
    print(sumatoria)
    

