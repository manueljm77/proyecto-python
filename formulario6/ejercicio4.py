numero=int(input("numero:"))
factoriales=1
if numero!=0:
    for i in range(1,numero+1):
        factoriales=factoriales*i
print("el factor es",factoriales)
        