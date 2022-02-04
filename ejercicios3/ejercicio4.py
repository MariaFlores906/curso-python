#Escriba un programa que pida el año actual y un año cualquiera y que escriba 
# cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

Año1 = int(input('Ingrese el año actual: '))
Año2 = int(input('Ingrese un año cualquiera: '))

if Año1 < Año2: 
    Resultado = Año2 - Año1
    print('Faltan  ' +  str(Resultado) + ' años para llegar al año ' + str(Año2))

elif Año1 > Año2:
    Resultado = Año1 - Año2
    print('Han pasado ' + str(Resultado) + ' años desde el año ' + str(Año2))

