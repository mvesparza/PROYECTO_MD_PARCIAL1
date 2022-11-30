"""
JUEGO DE PIEDRA - PAPEL O TIJERA

Este tradicional juego será implementado en el siguiente código
en donde generaremos un número aleatorio entre 0 y 3 que será 
la jugada de la máquina. Después con un simple menú haremos 
nuestra elección.
"""
import random
""""para ejecutar el programa necesitamos la librería random (aleatorio)"""
print("************** PIEDRA - PAPEL O TIJERA **************") #imprimir/mostrar incio del juego
while True:
    """iniciamos un ciclo mientras"""
    aleatorio = random.randrange(0,3)
    """se establece la variable aleatorio"""
    elijeMaquina = ""
    print("1. Piedra") #imprimir/mostrar opción 1
    print("2. Papel") #imprimir/mostrar opción 2
    print("3. Tijera") #imprimir/mostrar opción 3
    opcion = int(input("Elije tu opcion ")) # convierte la opcion elejida a entero
    if opcion == 1:
        """
        iniciamos una sentencia condicional
        para cada una de la opciones
        """
        elijeUsuario = "Piedra"
    elif opcion == 2:
        """
        Si la condición que sigue a la palabra clave if se 
        evalúa como verdadera, el bloque de código se ejecutará
        para cada una de las opciones
        """
        elijeUsuario = "Papel"
    elif opcion == 3:
        elijeUsuario = "Tijera"
    print("Elejiste: ", elijeUsuario) # muestra opcion elejida por el usuario
    if aleatorio == 0:
        elijeMaquina = "Piedra"
    elif aleatorio == 1:
        elijeMaquina = "Papel"
    elif aleatorio == 2:
        elijeMaquina = "Tijera"
    print("PC elijió: ", elijeMaquina) # muestra opcion elejida por la PC
    print("...")
    if elijeMaquina == "Piedra" and elijeUsuario == "Papel":
        """inicamos sentencia condicional para jugar"""
        print("GANASTE!! PAPEL ENVUELVE PIEDRA")
    elif elijeMaquina == "Papel" and elijeUsuario == "Tijera":
        """
        Si la condición que sigue a la palabra clave if se 
        evalúa como verdadera, el bloque de código se ejecutará
        para cada una de las opciones
        """
        print("GANASTE!! TIJERA CORTA PAPEL")
    elif elijeMaquina == "Tijera" and elijeUsuario == "Piedra":
        print("GANASTE!! PIEDRA APLASTA TIJERA")
    elif elijeMaquina == "Papel" and elijeUsuario == "Piedra":
        print("PERDISTE!! PAPEL ENVUELVE PIEDRA")
    elif elijeMaquina == "Tijera" and elijeUsuario == "Papel":
        print("PERDISTE!! TIJERA CORTA PAPEL")
    elif elijeMaquina == "Piedra" and elijeUsuario == "Tijera":
        print("PERDISTE!! PIEDRA APLASTA TIJERA")
    elif elijeMaquina ==  elijeUsuario: # Si ambos jugadores elijen la misma opcion
        print("EMPATE")

    jugar_otravez = input("Jugar de nuevo? (s/n): ")
    if jugar_otravez.lower() != "s":
        """
        iniciamos una sentencia condicional
        para seguir o no jugando
        """
        break # Cierra el bucle por completo

    """Fin del programa"""