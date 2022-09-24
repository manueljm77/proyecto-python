calificaciones = []
for indice in range(1,6):
	while True:
		calificacion = int(input("Introduce la calificacion %d:" % indice))
		if calificacion>=0 and calificacion<=10: break
	calificaciones.append(calificacion)
print("calificaciones: ",end="")
for calificacion in calificaciones:
	print(calificaciones," ",end="")
print()
print("calificacion media: ",sum(calificaciones)/len(calificaciones))
print("calificacion max: ",max(calificaciones))
print("calificacion min: ",min(calificaciones))

