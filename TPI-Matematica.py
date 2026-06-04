def decimal_a_binario(numero):
    return bin(numero)[2:]


def binario_a_decimal(binario):
    return int(binario, 2)


while True:
    print("Bienvenidos a conversión de números")
    print("--------Menu---------")
    print("1.Números decimales a binarios")
    print("2.Números binario a decimal")
    print("0.Salir")

    opcion = input("seleccione una opción: ").strip()

    if opcion == "1":
        numero = input("Ingresa un numero: ").strip()

        if numero.isdigit():
            numero = int(numero)

            print(f"La conversión de {numero} a binario es: {decimal_a_binario(numero)}")

        elif numero == "":
            print("Error: el numero no debe estar vacio")
        
        else:
            print("Error: solo se permiten numeros")

    elif opcion == "2":
        binario = input("Ingresa un numero binario: ").strip()

        if binario != "" and all(c in "01" for c in binario):
            print(f"La conversión {binario} a decimal es: {binario_a_decimal(binario)}")

        else:
            print("Error: ingresa un binario valido (solo 0 y 1)")

    elif opcion == "0":
        break

    else:
        print("Opcion invalida")