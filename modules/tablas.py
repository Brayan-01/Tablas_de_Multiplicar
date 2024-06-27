#*************
# Sena, Mosquera CBA
# Brayan Esteban Penagos Gutierrez
# Version 1.0
# 02/05/2024
# Ficha: 2877795
# Funcionalidad: Tablas de multiplicar

#*************


def tabla():
    #Importamos esta libreria para trabajar con el sistema 
    import os
    #Importamos el modulo de numeros random
    import random
    #Importamos esta funcion para que el usuario ingrese una sola letra para poder continuar
    import msvcrt
    #Esta parte importamos las cosas que vayamos a usar del modulo colorama
    from colorama import Back, Fore, Style, Cursor, init
    #Aca iniciamos el colorama
    init()


    #Iniciamos un bucle while 
    while True:
        #Este comando lo usamos para limpiar la pantalla
        os.system('cls')
        #Generador de numeros random
        num = random.randint(1,20)  
        #Aca se muestra el numero generado aleatoriamente
        print(Fore.LIGHTRED_EX + Back.BLACK  +  f"El número generado es: {Style.RESET_ALL} {num}")
        for i in range(1, num + 1):
            print(Fore.GREEN + Back.BLACK)        #Se veria un rango para el numero generado
            print(Fore.GREEN + Back.BLACK + f"La tabla del número {i} es:")
            #Generamos otro numero de 1 hasta 10
            for j in range(1, 11):
                #Multiplicamos el primer numero con el segundo
                producto = i * j
                print(Fore.GREEN + Back.BLACK,)            #Aca le deriamos un poco mas de orden a la multiplicacion
                print(f"{i} x {j} = {producto}")
                print("")
            print(Back.RESET + Fore.RESET + Style.RESET_ALL)
            #Le pedimos al usuario que presiona una tecla para continuar con la siguiente multiplicacion
            entrada = input(Fore.LIGHTWHITE_EX + Back.BLACK +  "Presione la  tecla 'ENTER' para continuar..." + Style.RESET_ALL)
            #Esto lo que hace es que hasta que no presione una tecla no va a avanzar correctamente
            msvcrt.getch()
            os.system('cls')
        #Le preguntamos al usuario si quiere continuar o acabar
        entrada = input(Fore.GREEN + Back.BLACK +  '\n'"Desea ejecutar nuevamente el programa S/N: " + Style.RESET_ALL).upper()
        #Creamos un while para el S o N
        while entrada not in ['S', 'N']:
            #Si se equivoca al digitar el usuario, le mandara este mensaje de que solo se puede S o N
            print(Fore.RED + Back.BLACK +  "Solamente puede digitar S/N." + Style.RESET_ALL + '\n')
            entrada = input("Elija de nuevo ").upper()
        #Si elige N, se acabara el programa
        if entrada == 'N':
            os.system('cls')
            break