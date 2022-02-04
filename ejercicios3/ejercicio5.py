# Escriba un programa que pida dos números enteros y que calcule su división, escribiendo 
# si la división es exacta o no

Num1 = int(input('Ingrese un numero: '))
Num2 = int(input('Ingrese otro numero: '))

Residuo = Num1 % Num2

if Num1 == 0:
    print('No se puede dividir por 0')

else:
    if Residuo == 0:
        print('La division es exacta')

    else:
        print('La division no es exacta')

