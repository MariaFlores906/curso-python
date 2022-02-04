from ast import Continue
import random

opciones = ('piedra', 'papel', 'tijera')

PcOption = random.choice(opciones)

UserOption = input('piedra, papel o tijera: ')
print(PcOption)

if PcOption == UserOption:
    print('Empate')

elif UserOption == 'piedra':
    if PcOption == 'papel':
        print('Pc ha ganado')
    elif PcOption == 'tijera':
        print('Has ganado')
  

elif UserOption == 'papel':
    if PcOption == 'tijera':
        print('Pc ha ganado')
    elif PcOption == 'piedra':
        print('Has ganado')
    
elif UserOption == 'tijera':
    if PcOption == 'piedra':
        print('Pc ha ganado')
    elif PcOption == 'papel':
        print('Has ganado')











