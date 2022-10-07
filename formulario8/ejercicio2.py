dict = {}
cadena = input("Dame una cadena:")
for caracter in cadena:
	if caracter in dict:
		dict[caracter]+=1
	else:
		dict[caracter]=1	

for renglon,cantidad in dict.items():
	print (renglon,"->",cantidad)
