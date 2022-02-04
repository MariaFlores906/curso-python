# Requerir al usuario que ingrese un número entero positivo e imprimir 
# todos los números entre el ingresado por el usuario y uno menos 
# del doble del mismo.

NumIngresado = int(input('Ingrese un numero entero: '))

Numdoble = NumIngresado * 2 

for num in range (NumIngresado, Numdoble):
    print(num)
