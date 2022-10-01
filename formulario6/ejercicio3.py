import os

total = 0
for i in range (1, 21):
    print ('PROCESO ' + repr (i))
    if i==1:
        pago=10
    else:
        pago=pago*2
    total=total+pago
    print ('Valor de pago: ' + repr (pago))
    print ()
print ('Valor de total: ' + repr (total))
os.system ('pause')

    