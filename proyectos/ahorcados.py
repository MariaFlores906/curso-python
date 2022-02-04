palabra = 'camino'
vidas = 7


letras_usadas = []

letras_adivinadas = []

palabra_actual = []

for i in range (len(palabra)):
    palabra_actual.append('- ')


palabra_espacios = []
for char in palabra_espacios:
    palabra_espacios.append(char + ' ')



while vidas > 0:
    print('Tienes ' + str(vidas) + ' vidas ')
    letra_ing = input('Ingrese una letra: ')
    letras_usadas.append(letra_ing)
    if letra_ing  in letras_usadas:
        pass
    else:
        letras_usadas.append(letra_ing)
    print('letras usadas: ' + str(letras_usadas))


    if letra_ing in palabra:
        if letra_ing in letras_adivinadas:
            pass
        else:
            letras_adivinadas.append(letra_ing)
        
    else:
        vidas = vidas - 1


    error = True
    for i in range(len(palabra)):
        if letra_ing == palabra[i]:
            palabra_actual[i] = letra_ing + ' '
            error = False
    
    print(' '.join(palabra_actual))

    if palabra_espacios == palabra_actual:
        print(''.join(palabra_actual))
        print('Has ganado!!')
        break


else:
    print('Te quedaste sin vidas, has perdido ;(')

