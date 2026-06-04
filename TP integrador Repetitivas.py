# Ejercicio 1:
'''
while True:
    nombre = input("Ingrese nombre del cliente: ")
    if nombre != "" and nombre.isalpha():
        break
    else:
        print("Error. Ingrese solo letras y no deje vacío.")


while True:
    cantidad = input("Ingrese cantidad de productos: ")
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
        break
    else:
        print("Error. Ingrese un número entero mayor a 0.")

total_sin_descuento = 0
total_con_descuento = 0


for i in range(1, cantidad + 1):
    
    
    while True:
        precio = input(f"Producto {i} - Precio: ")
        if precio.isdigit():
            precio = int(precio)
            break
        else:
            print("Error. Ingrese un número válido.")

    
    while True:
        descuento = input("Descuento (S/N): ").lower()
        if descuento == "s" or descuento == "n":
            break
        else:
            print("Error. Ingrese S o N.")

    total_sin_descuento += precio

    if descuento == "s":
        precio_desc = precio * 0.9
    else:
        precio_desc = precio

    total_con_descuento += precio_desc


ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print("\n--- RESUMEN ---")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
'''

#Ejercicio 2: 
'''
usuario_correcto = "alumno"
clave_correcta = "python123"



for intento in range(1, 4):
    print(f"Intento {intento}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        break
    else:
        print("Error: credenciales inválidas.")
else:
    print("Cuenta bloqueada")
    exit()

while True:
    print("Elije alguna de las opciones:")
    print("1. Ver estado de inscripción")
    print("2. Cambiar clave")
    print("3. Mostrar mensaje motivacional")
    print("4. Salir")
    opcion = input("ingrese el numero: ") 
    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue
    opcion = int(opcion)

    if  opcion < 1 or opcion > 4:
        print("Error: opción fuera de rango.")
        continue
    
    if opcion == 1:
        print("Inscripto")
     
    if opcion == 2:
        while True:
          nueva = input("Nueva clave: ")
          confirmar =input("confirmar clave: ")
          if len(nueva) < 6:
              print("Error: minimo 6 caracteres.")
              continue

          if nueva != confirmar:
              print("Error: no coinciden las claves")
              continue

          print("Clave cambiada correctamente")
          break
            
    if opcion == 3: 
        print("¡Seguí adelante, vos podés!")
     
    if opcion== 4:
        break
'''


#Ejercicio 3:

'''
lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""


while True:
    operador = input("Nombre del operador: ")
    if operador.isalpha():
        break
    print("Error: solo letras.")


while True:
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    op = input("Opción: ")

    if not op.isdigit():
        print("Error: número inválido")
        continue

    op = int(op)

    if op < 1 or op > 5:
        print("Error: fuera de rango")
        continue

    
    if op == 1:
        dia = input("Día (1=Lunes 2=Martes): ")

        if dia != "1" and dia != "2":
            print("Error: día inválido")
            continue

        while True:
            nombre = input("Nombre paciente: ")
            if nombre.isalpha():
                break
            print("Error: solo letras")

        
        if dia == "1":
            if nombre in (lunes1, lunes2, lunes3, lunes4):
                print("Paciente ya registrado")
            elif lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("No hay cupos en Lunes")

        
        else:
            if nombre in (martes1, martes2, martes3):
                print("Paciente ya registrado")
            elif martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("No hay cupos en Martes")

    
    elif op == 2:
        dia = input("Día (1=Lunes 2=Martes): ")

        while True:
            nombre = input("Nombre paciente: ")
            if nombre.isalpha():
                break
            print("Error: solo letras")

        if dia == "1":
            if lunes1 == nombre:
                lunes1 = ""
            elif lunes2 == nombre:
                lunes2 = ""
            elif lunes3 == nombre:
                lunes3 = ""
            elif lunes4 == nombre:
                lunes4 = ""
            else:
                print("No encontrado")

        elif dia == "2":
            if martes1 == nombre:
                martes1 = ""
            elif martes2 == nombre:
                martes2 = ""
            elif martes3 == nombre:
                martes3 = ""
            else:
                print("No encontrado")

        else:
            print("Día inválido")

    
    elif op == 3:
        dia = input("Día (1=Lunes 2=Martes): ")

        if dia == "1":
            print("Lunes:")
            print("1:", lunes1 if lunes1 != "" else "(libre)")
            print("2:", lunes2 if lunes2 != "" else "(libre)")
            print("3:", lunes3 if lunes3 != "" else "(libre)")
            print("4:", lunes4 if lunes4 != "" else "(libre)")

        elif dia == "2":
            print("Martes:")
            print("1:", martes1 if martes1 != "" else "(libre)")
            print("2:", martes2 if martes2 != "" else "(libre)")
            print("3:", martes3 if martes3 != "" else "(libre)")

        else:
            print("Día inválido")

    
    elif op == 4:
        ocup_lunes = sum(x != "" for x in (lunes1, lunes2, lunes3, lunes4))
        ocup_martes = sum(x != "" for x in (martes1, martes2, martes3))

        print(f"Lunes: {ocup_lunes} ocupados, {4 - ocup_lunes} libres")
        print(f"Martes: {ocup_martes} ocupados, {3 - ocup_martes} libres")

        if ocup_lunes > ocup_martes:
            print("Día con más turnos: Lunes")
        elif ocup_martes > ocup_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate")

    
    elif op == 5:
        print("Sistema cerrado")
        break
'''


#Ejercicio 4: 
'''
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

agente = input("Ingrese nombre del agente: ")

while not agente.isalpha:
    print("Error: ingrese solo letras.")
    agente = input("ingresa nuevamente el nombre del agente: ")

forzar_seguidas = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print("Menu")
    print("1.Forzar cerradura")
    print("2.Hackear panel")
    print("3.Descansar")

    opcion = input("Elije una opcion: ")

    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: solo se permiten numeros")
        opcion = input("ingresa nuevamente una opcion (1, 2 o 3): ")

    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar_seguidas +=1

        if forzar_seguidas == 3:
            alarma = True
            print("La cerradura se trabo. Alarma activada")
        else:
            if energia < 40:
                print("Riesgo de alarma")
                riesgo = input("Elije un numero del 1 al 3: ")
                while not riesgo.isdigit() or int(riesgo) not in [1, 2, 3]:
                    riesgo = input("Ingrese un número válido (1-3): ")

                if int(riesgo) == 3:
                    alarma = True
                    print("Alarma activada !!!")

            if not alarma:
                cerraduras_abiertas += 1
                print("Cerradura abierta ")
        
        print(f"estado actual: energia: {energia}, tiempo: {tiempo}, cerraduras abiertas: {cerraduras_abiertas}")


    elif opcion == 2:
         energia -= 10
         tiempo -=3
         forzar_seguidas = 0

         for i in range (4):
              print(f"pasos {1+i}/4")
              codigo_parcial += "A"

         if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
              cerraduras_abiertas += 1
              print("cerradura abierta por hackeo")
    
         print(f"estado actual: energia: {energia}, tiempo: {tiempo}, cerraduras abiertas: {cerraduras_abiertas}")

    elif opcion == 3:
         energia += 15
         if energia > 100:
              energia = 100
         tiempo -= 1
         forzar_seguidas = 0

         if alarma:
              energia -= 10
              print("si la alarma esta prendida resta 10 de energia extra")
        
         print("descansaste")

         print(f"estado actual: energia: {energia}, tiempo: {tiempo}, cerraduras abiertas: {cerraduras_abiertas}")
    
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
         print("El sistema se boloqueo")


print("Resultado")

if cerraduras_abiertas == 3:
     print(f"Felicidades {agente} usted pudo escapar")

elif energia <= 0 or tiempo <= 0:
     print("Derrota te quedaste sin tiempo y energia")

elif alarma:
     print("Derrota se bloqueo el sistema de alarmas")

'''

#Ejercicio 5: 

import random
print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Ingrese el nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: solo se permiten letras")
    nombre = input("Ingrese el nombre del Gladiador nuevamente: ")



vida_del_gladiador = 100
vida_del_enemigo = 100
pociones_de_vida = 3
daño_base_ataque =  15
daño_base_enemigo = 12
turno_gladiador = True

print("=== INICIO DEL COMBATE ===")
print(f"{nombre} (HP: {vida_del_gladiador}) VS ENEMIGO (HP: {vida_del_enemigo}) / POCIONES: {pociones_de_vida}")



while vida_del_gladiador >= 0 and vida_del_enemigo >= 0:
    print("Menu")

    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")

    opcion = input("Elige una acción: ")

    while not opcion.isdigit() or opcion not in ["1","2", "3"]:
        print("Error: solo se permiten numeros")
        opcion = input("ingresa nuevamente una opcion (1, 2 o 3): ")

    if opcion == "1":
        if vida_del_enemigo < 20:
            daño_final = daño_base_ataque * 1.5
            print("Golpe Critico")
        else:
            daño_final = daño_base_ataque
        
        vida_del_enemigo -= daño_final
        print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")
        print(f"Vida restante del enemigo: {vida_del_enemigo}")
        

    elif opcion == "2":
        for i in range(3):
            vida_del_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
        

    elif opcion == "3":
        if pociones_de_vida > 0:
            vida_del_gladiador += 30
            pociones_de_vida -=1
            print(f"Tu vida actual es: {vida_del_gladiador}")
        else:
            print("¡No te quedan pociones!")
        
    
    #TURNO DEL ENEMIGO
    if vida_del_enemigo >0:
        vida_del_gladiador -= daño_base_enemigo
        print("¡El enemigo te ataco por 12 puntos de daño!")

    print("=== NUEVO TURNO ===")
    print(f"{nombre} (HP: {vida_del_gladiador}) VS Enemigo (HP: {vida_del_enemigo}) / Pociones: {pociones_de_vida}")

if vida_del_gladiador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print(f"DERROTA. Has caído en combate.")
    
    