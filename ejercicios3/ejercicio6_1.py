#Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. 
#No considerar el caso en que ambos números son iguales.

Num1 = int(input('Ingrese un numero: '))
Num2 = int(input('Ingrese otro numero: '))

if Num1 > Num2:
    print('El primer numero ingresado es mayor')

else:
    print('El primer numero ingresado es menor')