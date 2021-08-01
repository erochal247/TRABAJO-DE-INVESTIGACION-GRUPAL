from operacion_numeros.Intermedio import INTERMEDIO

class Lista(INTERMEDIO):
    def __init__(self, lista=['P', 'O', 'O', '@', '1', ':', ')', '0', ' ', '-'], num=5):
        self.lista = lista
        self.num = num
    
    def presentalista(self):
        print('Recorrer lista')
        if len(self.lista) != 0:
            for a in range(len(self.lista)):
                if a+1 == len(self.lista):
                    print(self.lista[a] + '.')
                else: print(self.lista[a] + ',', end=' ')
        else: print('No hay elementos que recorrer')
    
    def buscarlista(self, valor='0'):
        print('Buscar valor')
        if len(self.lista) != 0:
            ubicacionDato = []
            for a, b in enumerate(self.lista):
                if b == valor:
                    ubicacionDato.append(a+1)
            print('El valor', valor, 'se encontró en la posición', ubicacionDato)
            if not ubicacionDato:
                print('El valor', valor, 'no se encontró en la lista.')
        else:
            print('No hay valor que buscar porque\nla lista está vacía.')

    def listafactorial(self):
        listfactorial = []
        print('Lista con', end=' ')
        INTERMEDIO.factorial(self, self.num)
        for i in reversed(range(1, self.num+1)):
            listfactorial.append(i)
        return listfactorial
    
    def primo(self):
        listPrimo = []
        noPrimo = False
        print('Número primo')
        for numero in range(self.num+1):
            if numero >= 2:
                for a in range(2, numero):
                    if numero % a == 0:
                        noPrimo = True
                        break
                if not noPrimo:
                    listPrimo.append(numero)
            else: pass
            noPrimo = False
        return listPrimo
    
    def listaNotas(self, notasDictadas={'MARIA':[10, 8, 9], 'RONNY':[9, 5, 6]}):
        print('Lista con notas de alumnos')
        for a in notasDictadas:
            print('Para el alumno', a, 'sus notas son las siguientes:\n ->| ', end='')
            for b in notasDictadas[a]:
                print(b, end=' | ')
    
    def insertarlista(self, posicion=2, valor=3):
        print('Insertar dato en  la lista según su posición')
        print('Lista antigua:', self.lista)
        self.lista.insert(posicion-1, valor)
        print('Lista nueva: ', self.lista)
    
    def eliminarlista(self, valor='0'):
        print('Eliminar ocurrencias de una lista')
        repetElement = self.lista.count(valor)
        print('Lista antigua:', self.lista)
        if repetElement:
            for a in range(repetElement):
                self.lista.remove(valor)
            print('Lista nueva:', self.lista)
        else:
            print('No encontramos ese elemento')
    
    def retornarValor(self, posicion=0):
        print('Retornar cualquier valor de la lista eliminandolo')
        try:
            return self.lista[posicion-1]
        except IndexError:
            print('No hay suficientes elementos para\npoder eliminar esa posición de la lista')
            print('Ingresa otra posición')
    
    def copiarTupla(self, tupla=('cadena', 'tupla', 'valor', 'lista')):
        print('Copiar tupla a lista\nTupla prefabricada')
        print('Tupla:', tupla)
        print('Lista:', list(tupla))
    
    def vueltolista(self, listDiccionary={15.0:['Carlos', 'Esther'], 10.0:['Andres', 'Rocha', 'Maria']}):
        print('Dar vuelto a los clientes')
        for a in listDiccionary:
            print('El valor de $' + str(a) + ' será entregado a los clientes:\n- ', end='')
            for b in listDiccionary[a]:
                print(b + '-_-', end='')


def menu():
    opcion = 0
    while opcion != 11:
        list = []
        numero = 0
        print('--Menú Tratamiento de Lista--')
        print('  1) Recorrer y presentar los datos de una lista')
        print('  2) Buscar un valor en una lista')
        print('  3) Retornar una lista con los factoriales')
        print('  4) Retornar una lista de números primos')
        print('  5) Recorrer una lista de diccionario con notas de alumnos')
        print('  6) Insertar un dato en una Lista dada lo Posición')
        print('  7) Eliminar todas las ocurrencias en una Lista')
        print('  8) Retornar cualquier valor de una lista eliminándolo')
        print('  9) Copiar cada elemento de una tupla en una lista')
        print(' 10) Dar el vuelto a varios clientes')
        print('11) Salir')

        while True:
            try:
                opcion = int(input('Ingrese una opción: '))
                if opcion in range(1, 12): break
                else: print('Ingrese una opción')
            except ValueError:
                print('Ingrese una opción válida')

        if opcion in range(1, 5) or opcion in range(6, 9):  
            if opcion not in range(3, 5):
                element = ''
                valor = ''
                print('Ingreso de elementos en una lista')
                print('Ingrese "F" para salir')
                while element.replace(' ', '') != 'F':
                    element = input('Ingrese un elemento: ')
                    if element.replace(' ', '') != 'F':
                        list.append(element)
                if (opcion == 2 or opcion == 6 or opcion == 7): 
                    valor = input('Ingrese un valor: ')
            
            if opcion == 3 or opcion == 4 or opcion == 6 or opcion == 8: 
                _num = 0
                while True:
                    try:
                        _num = int(input('Ingrese un número: '))
                        if _num > 0: break
                        else: print('Ingrese un número entero mayor a 0')
                    except ValueError:
                        print('Ingrese un valor correcto')

        elif opcion == 5 or opcion == 10:  
            nombre = ''
            numero = ''
            diccionario = {}
            print('Ingreso de elementos en un diccionario')
            print('Ingrese "F" para salir')
            
            if opcion == 5: 
                while True: 
                    nombre = input('Ingrese un nombre: ')
                    if nombre != 'F':
                        diccionario[nombre] = []
                        while True:  
                            try:
                                numero = input('Ingrese la calificación: ').replace(' ', '')
                                if numero.replace(' ', '') != 'F':
                                    numero_aux = float(numero)
                                    if numero_aux > 0 and numero_aux <= 10:
                                        diccionario[nombre].append(numero_aux)
                                    else:
                                        print('Ingrese notas entre un rango de 1-10')
                                else:
                                    if numero.replace(' ', '') == 'F' and not diccionario[nombre]:  
                                        print('Ingresa al menos un dato')
                                    else: break
                            except ValueError:
                                print('Ingrese un valor correcto.')
                    else:
                        if nombre.replace(' ', '') == 'F' and not diccionario: 
                            print('Ingresa al menos un dato')
                        else: break
            else:  
                while True:  
                    numero = input('Ingrese un valor: $')
                    if numero != 'F':
                        try:
                            numero = round(float(numero), 2)
                            diccionario[numero] = []
                            while True:  
                                    nombre = input('Ingrese nombres de clientes: ').replace(' ', '')
                                    if nombre.replace(' ', '') != 'F':
                                            diccionario[numero].append(nombre)
                                    else:
                                        if nombre.replace(' ', '') == 'F' and not diccionario[numero]:  
                                            print('Ingresa al menos un valor')
                                        else: break   
                        except ValueError:
                            print('Ingrese un valor correcto')
                    else:
                        if numero.replace(' ', '') == 'F' and not diccionario:  
                            print('Ingresa al menos un dato')
                        else: break
        
        elif opcion == 9: pass
        else:
            print('Gracias')
            input('\nPulsa Enter para salir')
            break
        
        manipular = Lista(list, _num)
        if opcion != 11:
            print('')
            if opcion == 1:
                manipular.presentalista()
         
            elif opcion == 2:
                manipular.buscarlista(valor)
         
            elif opcion == 3:
                factorial = manipular.listafactorial()
                print('Lista Factorial:', factorial)
         
            elif opcion == 4:
                primo = manipular.primo()
                print(primo)
         
            elif opcion == 5:
                manipular.listaNotas(diccionario)
           
            elif opcion == 6:
                manipular.insertarlista(_num, valor)
            
            elif opcion == 7:
                manipular.eliminarlista(valor)
           
            elif opcion == 8:
                valor_lista = manipular.retornarValor(_num)
                print('Elemento de la lista:', valor_lista)
            
            elif opcion == 9:
                manipular.copiarTupla()
            else:
                manipular.vueltolista(diccionario)
            input('\nPulsa Enter para limpiar la pantalla')
