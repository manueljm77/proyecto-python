numero = int(input("Dame un número:"))
raizcuadrada = {}

for num in range(1,numero+1):
    raizcuadrada[num] = num ** 2
for num, valor in raizcuadrada.items():
    print("%d -> %d" % (num,valor))
