
palabra = 'camino'
vidas = 7


letras_usadas = []

letras_adivinadas = []


while vidas > 0:
    
    letra_ing = input('Ingrese una letra: ')
    letras_usadas.append(letra_ing)


    if letra_ing  in letras_usadas:
        pass
    else:
        letras_usadas.append(letra_ing)
    print('letras usadas: ' + str(letras_usadas))


    palabra_actual = ''

    for letra in palabra:
        if letra not in letras_usadas:
            palabra_actual = palabra_actual + '- '
        else:
            palabra_actual = palabra_actual + letra


    if letra_ing in palabra: 
        letras_adivinadas.append(letra_ing)

    else:
        vidas = vidas - 1
    
    

    print('Palabra: ' + str(palabra_actual))
    print('Tienes ' + str(vidas) + ' vidas ')



        
    if palabra_actual == palabra:
        print('Has ganado!!')
    


else:
    print('Te quedaste sin vidas, has perdido ;(')

