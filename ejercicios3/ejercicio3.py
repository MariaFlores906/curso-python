from calendar import prcal


print('Elija una opcion')
print('1 suma')
print('2 resta')
print('3 multiplicacion')
print('4 division')

opcion = int(input())

if opcion == 1:
    print('Ingrese un numero: ')
    num1 = int(input())
    print('Ingrese otro numero: ')
    num2 = int(input())
    resultado = num1 + num2
    print('El resulado de la suma es: ' +  str(resultado))

elif opcion == 2:
    print('Ingrese su numero: ')
    num1 = int(input())
    print('Ingrese otro numero: ')
    num2 = int(input())
    resultado = num1 - num2
    print('El resultado de la resta es: ' + str(resultado))

elif opcion == 3:
    print('Ingrese su numero: ')
    num1 = int(input())
    print('Ingrese otro numero: ')
    num2 = int(input())
    resultado = num1 * num2
    print('El resultado de la multiplicacion es: ' + str(resultado))

elif opcion == 4:
    print('Ingrese su numero: ')
    num1 = int(input())
    print('Ingrese otro numero: ')
    num2 = int(input())
    resultado = num1 / num2
    print('El resultado de la division es: ' + str(resultado))
    

