import random

# // Carga el archivo acumulado.txt
def cargar_acumulado():
    try:
        with open("acumulado.txt", "r") as archivo:
            acumulado = float(archivo.read())
    except FileNotFoundError:
        acumulado = 0.0
    return acumulado
# // Guarda los valores en el archivo acumulado.txt
def guardar_acumulado(acumulado):
    with open("acumulado.txt", "w") as archivo:
        archivo.write(str(acumulado))
        
# // 
def juego_apuesta():
    acumulado = cargar_acumulado()

    while True:
        numero_rd = random.randint(1, 5)
        attempts = 0
        print(f"Monedero {acumulado}")
        consignacion =float(input("Antes de jugar, deberá consignar dinero al monedero para poder jugar. "))
        acumulado = acumulado + consignacion
        guardar_acumulado(acumulado)
        apuesta = float(input("Elige un monto para apostar y multiplicar tu dinero: "))
        
        if apuesta > acumulado:
            print(f"La apuesta supera el capital actual del monedero {acumulado}; no es posible realizar esta.")
            continue


        while True:
            acumulado = acumulado - apuesta
            guardar_acumulado(acumulado)
            
            numero_user = int(input("Elija un número (entre 1 y 3) para ganar: "))
            attempts += 1

            if numero_user == numero_rd:
                ganancia = apuesta
                print(f"¡Felicidades! Ganaste {ganancia}!")

                acumulado = apuesta * 2
                guardar_acumulado(acumulado)

                cont = input("¿Deseas seguir apostando? 'si' para continuar, 'no' para finalizar: ")

                if cont.lower() == 'si':
                    break
                elif cont.lower() == 'no':
                    print("Gracias por jugar. ¡Hasta la próxima!")
                    return
                else:
                    print("Entrada no válida. Por favor, ingresa 'si' o 'no'.")

            elif attempts >= 3:
                print("Limite de intentos alcanzado, perdiste :(")
                acumulado = acumulado - apuesta
                guardar_acumulado(acumulado)
                cont = input("¿Deseas seguir apostando? 'si' para continuar, 'no' para finalizar: ")

                if cont.lower() == 'si':
                    break
                elif cont.lower() == 'no':
                    print("Gracias por jugar. ¡Hasta la próxima!")
                    return
                else:
                    print("Entrada no válida. Por favor, ingresa 'si' o 'no'.")
# // Usa el juego
juego_apuesta()