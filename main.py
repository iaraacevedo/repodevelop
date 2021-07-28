print('Hola mundo')
option = 0
while option not in (1,2,3,4):
    print('1- sumar')
    print('2- multiplicar')
    print('3- restar')
    print('4- dividir')
    option = int(input('ingrese una opcion: '))
    if option==1:
        a= int(input('ingrese nro'))
        b = int(input('ingrese nro2 '))
        print('resultado',a+b)