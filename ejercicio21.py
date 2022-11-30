'''
21) Se requiere un algoritmo que calcule el sueldo neto de un trabajador.
Para ello, el algoritmo debe admitir el ingreso del monto a cobrar por horas y el total de horas trabajadas.
Si el empleado trabajó más de 160 horas mensuales se deben considerar la diferencia como horas extras y 
el monto por hora deberá ser el doble del valor ingresado en un inicio.
'''
valorHora=float(input("Ingrese el monto a cobrar por hora: "))
horasTrabajadas=int(input("Ingrese la cantidad de horas trabajadas: "))
if horasTrabajadas <=160:
    totalacobrar=valorHora*horasTrabajadas
    print("El sueldo neto de el trabajador es de {}".format(totalacobrar))
else:
    horasExtras =horasTrabajadas-160
    totalacobrar = valorHora*160+(horasExtras*(valorHora*2))
    print("El sueldo neto de el trabajador es de {}".format(totalacobrar))

    
