print("06. CALCULAR EL MONTO A PAGAR POR UN PRÉSTAMO")
monto = float(input("Ingrese monto del préstamo : "))
tasa  = int(input("Ingrese tasa de interés : % "))
meses = int(input("Ingrese Nro de meses : "))


interes = monto * ( meses * (tasa / 100))
totalp  = monto + interes 
if tasa>30:
    
    print("tasa erronea")
else:
        
    print("Interés Generado : $ {:.2f}".format(interes))
    print("Pago Total  : $ {:.2f}".format(totalp))

    

