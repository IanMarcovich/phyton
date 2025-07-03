
import random

num_secreto = random.randint (1, 30)
max_intentos = 5
intentos = 0

print ("Adivina un numero secreto entre el 1 y el 30")
print (f"Tienes {max_intentos} intentos")
while intentos < max_intentos:
    intento = int (input(f"Intento {intentos + 1}:  "))
    intentos += 1

    if intento < num_secreto:
        print ("Un poco mas!")
    elif intento > num_secreto:
        print ("Uf te pasaste!")
    else:
        print (f"🎊¡SII ESE ES EL NUMERO MUY BIEN!!🎊  El numero era {num_secreto} ")
        break
else:
    print (f"😔¡Se acabo los intentos!😔  El numero era {num_secreto}")
