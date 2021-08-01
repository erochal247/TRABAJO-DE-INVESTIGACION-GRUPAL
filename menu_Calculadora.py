from tipo_de_calculadoras.calculadora_Cientifica import calculadoraCIENTIFICA
from tipo_de_calculadoras.calculadora_Estandar import calculadoraESTANDAR


class MENUCalculadora:
    def menu(self):
        opc = 0
        calCientifica = calculadoraCIENTIFICA()
        
        while opc != 10:
            print('Menú Calculadora')
            print('  1) Suma')
            print('  2) Resta')
            print('  3) Multiplicacion')
            print('  4) Division')
            print('  5) Exponente')
            print('  6) Valor Absoluto')
            print('  7) Circunferencia')
            print('  8) Area Circulo')
            print('  9) Area Cuadrado')
            print(' 10) Salir')
            
            while True:
                try:
                    opcion = int(input('Ingrese una de las opciones: '))
                    if opcion not in range(1, 11):
                        print('Ingrese una de las opción disponibles.')
                    else:
                        break
                except ValueError:
                    print('Ingrese una opción correcta')
            
            if opcion != 10:
                if opcion not in range(6, 10):
                    while True:
                        try:
                            num1 = float(input('Ingrese un número: '))
                            num2 = float(input('Ingrese otro número: '))
                            break
                        except ValueError:
                            print('Ingrese valores que sean correctos.')
                    
                    calEstandar = calculadoraESTANDAR(num1, num2)

                if opcion == 1:
                    print('El resultado de la suma es: ', calEstandar.SUMA())

                elif opcion == 2:
                    print('El resultado de la resta es: ', calEstandar.RESTA())

                elif opcion == 3:
                    print('El resultado de la multiplicación es: ', calEstandar.MULTIPLICACION())

                elif opcion == 4:
                    print('El resultado de la división es: ', calEstandar.MULTIPLICACION())

                elif opcion == 5:
                    print('El número {} elevado al exponente {} es igual a: {}'.format(num1, num2, calEstandar.EXPONENTE()))

                elif opcion == 6:
                    while True:
                        try:
                            num1 = float(input('Ingrese un número: '))
                            break
                        except ValueError:
                            print('Ingrese un valor correcto.')
                    print('\nEl valor absoluto es igual a:', calEstandar.valorABSOLUTO(num1))

                else: 
                    if opcion in range(7, 9):
                        while True:
                            try:
                                radio = float((input('Ingrese el radio: ')))
                                break
                            except ValueError:
                                print('Ingrese el valor correcto')
                        if opcion == 7:
                            print('El resultado de la circunferencia es igual a: ', calCientifica.CIRCUNFERENCIA(radio))
                        
                        else:  
                            print('El área del circulo es: ', calCientifica.areaCIRCULO(radio))
                    
                    else:  
                        while True:
                            try:
                                lado = float((input('Ingrese el valor de un lado: ')))
                                break
                            except ValueError:
                                print('Ingrese el valor correcto')
                        print('El área del cuadrado es: ', calCientifica.areaCUADRADO(lado))
            
            else:
                print('___Gracias____')
            input('\nPulsa Enter para terminar')
