import random

pcnum = random.randint(1, 10)

Vidas = 5

while True:
    NumIngresado = int(input('Ingrese un numero del 1 al 10: '))

    if NumIngresado == pcnum:
        print('Has ganado :D!!')
        break

    else:
        print('Intente de nuevo')
        Vidas = Vidas - 1
        print('Vidas restantes: ' + str(Vidas))
    
    if Vidas == 0:
        print('Se te han agotado las vidas :(')
        break
