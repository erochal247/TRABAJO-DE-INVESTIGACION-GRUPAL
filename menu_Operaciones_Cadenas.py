class Operaciones_con_cadenas:
    def __init__(self, cad=''):
        self.cadena = cad
    
    def recorrerCadena(self):
        for a in self.cadena:
            print(a)
    
    def buscarCaracter(self, buscar=''):
        caracteres = self.cadena.find(buscar)
        if caracteres > 0:
            print('El caracter {} esta dentro de la cadena'.format(buscar))
        else:
            print('El caracter {} no esta en la cadena'.format(buscar))

    def listaPosicion(self, caracter=''):
        listPosicion = []
        for a in range(0, len(self.cadena)):
            if self.cadena[a].lower() == caracter:
                listPosicion.append(a+1)
        return listPosicion

    def listaPalabras(self):
        while True:
            if len(self.cadena)+1 > 1:
                break
            else:
                print('Ingresar la palabra correcta')
                self.cadena = input('Ingresar la palabra: ').lower().replace('','')
        return list(self.cadena.split())

    def cadenaLista(self):
        print('Ingreso de datos')
        print('Ingreso para poder salir')
        listConversion = []
        while True:
            conversion = input('Ingrese los caracteres: ')
            if conversion.replace('', '') == '__':
                break
            listConversion.append(conversion)
        converCad = "".join(listConversion)
        print("Lista: ", listConversion)
        print("Cadena: ", converCad)
    
    def insertarDato(self, dato, posicion):
        cad = list(self.cadena)
        cad.insert(posicion, dato)
        converStrg = ''.join(cad)
        print("Cadena nueva: ", converStrg)
    
    def eliminarOcurrencias(self, dato):
        print("Cadena nueva: ", self.cadena.lower().replace(dato, ''))

    def retornaValor(self, posicion):
        cad = list(self.cadena)
        vuelta = 0
        for a in posicion:
            if vuelta > 0:
                cad.pop((a-1)-vuelta)
            else:
                cad.pop(a-1)
            vuelta += 1
        return ''.join(cad)
    
    def concatenarCadena(self, dato):
        print('Cadena concatenada: ', self.cadena + dato)


def menu():
    cadena = ''
    opcion = 0
    while opcion != 10:
        print('Menú Operaciones con Cadenas')
        print(' 1) Presentar y recorrer los datos de la cadena')
        print(' 2) Buscar un carácter en una cadena')
        print(' 3) Retornar una lista con la posiciones dado un carácter de la cadena')
        print(' 4) Retornar una lista con todas las palabras de una cadena')
        print(' 5) Retornar una cadena a partir de una lista')
        print(' 6) Insertar un dato en una cadena dada lo Posición')
        print(' 7) Eliminar todas las ocurrencias en una cadena')
        print(' 8) Retornar cualquier valor de una cadena eliminándolo')
        print(' 9) Concatenar cadenas')
        print('10) Salir')
        
        while True:
            try:
                opcion = int(input('Ingrese una opcion: '))
                if opcion not in range(1, 11):
                    print('Ingrese un opción valida')
                else:
                    break
            except ValueError:
                print('Ingrese una opción valida')    
        
        if opcion != 10:
            if opcion != 5:
                cadStr = input('Ingrese una cadena: ')
            cadena = Operaciones_con_cadenas(cadStr)
            
            if opcion == 1:
                cadena.recorrerCadena()

            elif opcion == 2:
                while True:
                    buscarCaracter = input('Ingrese el caracter que desea buscar: ').lower().replace(' ', '')
                    if len(buscarCaracter) > 0 and len(buscarCaracter) < 2:
                        break
                    else:
                        print('Ingrese un caracter correcto')
                cadena.buscarCaracter(buscarCaracter)
            
            elif opcion == 3:
                while True:
                    listaCaracter = input('Ingrese el caracter a ser listado: ').lower().replace(' ', '')
                    if len(listaCaracter) > 0 and len(listaCaracter) < 2:
                        break
                    else:
                        print('Ingrese un caracter válido')
                caracterPos1 = cadena.listaPosicion(listaCaracter)
                print('Posiciones encontradas: {}'.format(caracterPos1))

            elif opcion == 4:
                caracterPos = cadena.listaPalabras()
                print('Posiciones encontradas: {}'.format(caracterPos))
            
            elif opcion == 5:
                cadena.cadenaLista()
            
            elif opcion == 6:
                insertarDato = input('Ingrese un dato a insertar: ')
                while True:
                    try:
                        posicion = int(input('Del número 1 al {} ingrese la posición: '.format(len(cadStr))))
                        if posicion in range(1, len(cadStr)+1):
                            break
                        else: print('Ingrese la posición correcta')
                    except ValueError:
                        print('Ingrese un valor correcto')
                cadena.insertarDato(insertarDato, posicion)

            elif opcion == 7:
                ocurrencia = input('Ingrese los caracteres que desea eliminar: ').lower()
                cadena.eliminarOcurrencias(ocurrencia)

            elif opcion == 8:
                print('Ingreso de posiciones')
                print('Pulsar -- para salir')
                posiciones = set()
                while True:
                    pos = input('Del número 1 al {} ingrese las posiciones a eliminar: '.format(len(cadStr)))
                    if pos.replace(' ', '') == '--':
                        break
                    try:
                        pos = int(pos)
                        if pos in range(1, len(cadStr)+1):
                            posiciones.add(pos)
                        else: print('Ingrese una posición correcta')
                    except ValueError:
                        print('Ingrese valores válidos')
                valor = cadena.retornaValor(posiciones)
                print('Cadena nueva retornada: ', valor)
            else:
                concatenar = input('Ingrese otra cadena: ')
                cadena.concatenarCadena(concatenar)
        else: print('\nGracias')
        input('\nPulsa Enter para salir')
