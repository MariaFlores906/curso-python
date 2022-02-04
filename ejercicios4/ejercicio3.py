# Crear un programa que pida al usuario que ingrese 10 numeros con un bucle for y 
# luego imprima la suma de todos los numeros

Listnum = [0]

for num in range(10):
   numero = (int(input('Ingrese un numero: ')))
   Listnum.append(numero)

suma = 0

for num in Listnum:
    suma = num + suma 

print(suma)
    





