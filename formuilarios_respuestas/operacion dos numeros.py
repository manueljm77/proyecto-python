numero1 = int(input("ingrese un número "));
numero2 = int(input("ingrese otro numero "));
tipo_operacion = input("suma, resta, división, multiplicación ");

if tipo_operacion == "suma":
    print(numero1 + numero2)
elif tipo_operacion == "resta":
    print(numero1 - numero2)
elif tipo_operacion == "division":
    print(numero1 / numero2)
elif tipo_operacion == "multiplicacion":
    print(numero1 * numero2)