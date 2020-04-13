reset = True

n1 = 'Ingrese el primer numero  '
n2 = 'Ingrese el segundo numero  '

ops = 'ha elegido sumar los numeros. '
opr = 'ha elegido restar los numeros. '
opd = 'ha elegido dividir los numeros. '
opm = 'ha elegido multiplicar los numeros. '

res = 'No ha ingresado ningun valor'
rest = ''

while reset:

    menu = '''
            ***** Menu *****

     ¿Que operacion matematica desea realizar?
            1 -> sumar
            2 -> restar
            3 -> multiplicar
            4 -> dividir

        ******-----*****  '''
    print(menu)
    if rest == '':
        print(f'Sabe que : {res}')
    else:
        print(f'El resultado es: {rest}')


    print()
    opcion = int(input('Ingrese la opcion numerica: '))
    #   print(f'La opcion es: {opcion}')

    if opcion == 1:

        print({ops})
        a = float(input(f' {n1} ->'))
        b = float(input(f'{n2} ->'))
        rest = a+b
        #print(rest)

    elif opcion == 2:

        print({opr})
        a = float(input(f' {n1} ->'))
        b = float(input(f'{n2} ->'))
        rest = a - b
        #print(rest)

    elif opcion == 3:

        print({opm})
        a = float(input(f' {n1} ->'))
        b = float(input(f'{n2} ->'))
        rest = a * b
        #print(rest)

    elif opcion == 4:

        print({opm})
        a = float(input(f' {n1} ->'))
        b = float(input(f'{n2} ->'))
        rest = a / b
        #print(rest)

    else:
        print(f'La opcion {opcion} no esta disponible.')
        reset = False




