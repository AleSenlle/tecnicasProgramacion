consumoMesAnterior=float(input("Ingrese el consumo del mes anterior (en kw): "))
consumoActual=float(input("Ingrese el consumo del mes actual (en kw): "))
montoApagar=(consumoMesAnterior+consumoActual)*115.30
print("El monto total a pagar es de {}".format(montoApagar))