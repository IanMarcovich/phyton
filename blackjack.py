
# aca definimos la funcion del mazo que serian los valores de las cartas y los tipos de palos 
# Importamos random para que las cartas sean aleatorias 
# Y usamos el .shuffle para que el orden de nuestro mazo sea aleatorio
import random

def mazo_completo():
    palos = ['Corazones','Picas','Diamantes','Treboles']
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    mazo = [(valor,palo) for palo in palos for valor in valores]
    random.shuffle(mazo) 
    return mazo


# Aca se define el valor de la mano es decir que las cartas que sean J,Q,K van a valer 10 
# y el As osea A va a valer 11(tambien puede valer 1 si es lo que conviene en esa mano es decir si yo tengo en mi mano una J y un 9 y me sale un A el valor puede ser 1) 
# y despues las demas cartas su valor es el mismo (2 al 10)
def valor_de_mano (mano):
    valor = 0
    ases = 0
    for carta in mano:
        if carta[0] in ['J','Q','K']:
            valor += 10
        elif carta[0] == 'A':
            ases += 1
            valor += 11
        else:
            valor += int(carta[0])
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
    return valor

# Aca definimos mostrar mano osea las cartas, (en el BlackJack el crupier tiene una carta que recibe boca abajo en la ronda inicial
def mostrar_la_mano (mano, carta_oculta =False ):
    if carta_oculta:
        print ("[CARTA OCULTA]]", mano [1])
    else:
        for carta in mano:
            print(f"{carta[0]} de {carta [1]}")

#Aca definimos la ronda (usamos el .pop para eliminar y devolver mazo)
# Despues usamos el while para crear la apuesta
def jugar_ronda(fichas):
    mazo = mazo_completo()
    jugador = [mazo.pop(), mazo.pop()]
    crupier = [mazo.pop(), mazo.pop()]
    
    print (f"Usted tiene  {fichas} fichas")
    while True:
        apuesta_str = input ("Cuanto desea apostar?: ")
        if apuesta_str.isdigit():
            apuesta = int(apuesta_str)
            if 0 < apuesta <= fichas:
                break
            else:
                print (f"Usted debe apostar (+)Que (0) o menos que {fichas}")
        else:
            print ("Debe ingresar un numero valido")

    print("\n Tus cartas ")
    mostrar_la_mano (jugador)
    print ("El valor total es:", valor_de_mano(jugador))

    print ("\nCartas del crupier: ")
    mostrar_la_mano (crupier, carta_oculta=True)

# en este while es turno del jugador
    while valor_de_mano(jugador) < 21:
        accion = input("\nPedir otra carta (P) o Quedarte (Q)").lower()
        if accion == 'p':
            jugador.append(mazo.pop())
            print ("\n Tu mano ahora es:")
            mostrar_la_mano(jugador)
            print("El valor total es: ", valor_de_mano(jugador))
        elif accion == 'q':
            break
        else:
            print ("OPCION NO VALIDA INGRESE (P) PARA PEDIR O (Q) PARA QUEDARSE")

    if valor_de_mano(jugador) > 21:
        print ("TE PASASTE DE 21 ¡PERDISTE!❌")
        return fichas - apuesta
    
    print ("\nTurno del crupier: ")
    mostrar_la_mano(crupier)
    
# Este while es el crupier
    while valor_de_mano(crupier) < 17:
        crupier.append(mazo.pop())
        print ("\n El crupier agarra otra carta:")
        mostrar_la_mano(crupier)
    valor_de_jugador = valor_de_mano(jugador)
    valor_de_crupier = valor_de_mano(crupier)
    
    print ("\nRESULTADOS🎰")
    print ("Tu mano es ", valor_de_jugador)
    print ("La mano del crupier es: ", valor_de_crupier)

    if valor_de_crupier > 21 or valor_de_jugador > valor_de_crupier:
        print ("GANASTE MUY BIEN!💰")
        return fichas + apuesta
    elif valor_de_jugador < valor_de_crupier:
        print ("PERDISTE LO SIENTO❌")
        return fichas - apuesta
    else:
        print ("EMPATE")
        return fichas
    
    
# Aca es donde elejimos nuestra apuesta
def blackjack():
        fichas = 1000
        print ("\n🎰 Bienvenido al Blackjack")

# EL .lower hace q no importa si escribis en mayuscula te lo va tomar como minuscula
        while fichas > 0:
            fichas = jugar_ronda(fichas)
            print (f"\nLa cantidad de fichas son {fichas}")
            continuar = input ("\nDesea seguir jugando? (S) / (N)").lower() 
            if continuar != 's':
                break
            
        if fichas <= 0:
            print ("\n TE QUEDASTE SIN FICHAS❌")
            print ("\n  SE TERMINO EL JUEGO❌")
        else:
            print (f"\nTE RETIRASTE CON {fichas} FICHAS")
            print (f"\n     GRACIAS POR JUGAR")

#  ACA TENEMOS LAS REGLAS (SE IMRPIME EN PANTALLA CUANDO ELEJIMOS LA OPCION DE IR A REGLAS)
def reglas ():
    print ("\n Reglas del blackjack")
    print ("\n EL objetivo es llegar lo mas cerca posible al 21")
    print ("\n J|Q|K valen 10")
    print ("\n El AS (A) vale 11")
    print ("\n En caso de pasarte de 21 el AS (A) pasaria a valer 1")
    print ("\n El grupier tiene que llegar a 17 o mas")
    print ("\n Si el grupier se pasa de 21 pierde")
    print ("\n Si estas mas cerca del 21 que grupier ganas")
    print ("\n Si ambos tienen lo mismo hay empate")
    print ("\n Si te pasas de 21 perdes")
# Se usa el true en un while para que se ejecute el codigo al elegir alguna de las opciones (es un booleano)
def menu():
    while True:
        print ("\nEstas en el menu principal")
        print ("(1) Para ir a jugar")
        print ("(2) Para ir a reglas")
        print ("(3) Para salir")

        opcion = input("\nElegir una opcion para continuar (1|2|3):")

        if opcion == '1':
            blackjack()
        elif opcion == '2':
            reglas()
        elif opcion == '3':
            print ("    Gracias por jugar!")
            break
        else:
            print ("OPCION NO VALIDA INGREGESE (1|2|3)")         


menu()













