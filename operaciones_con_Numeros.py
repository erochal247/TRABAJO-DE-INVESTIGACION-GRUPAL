from operacion_numeros.Basico import BASICO
from operacion_numeros.Intermedio import INTERMEDIO

class OperacionesConNumeros:
    def menu(self):
        opcion = 0
        operBasica = BASICO()
        operIntermedia = INTERMEDIO()
        while opcion != 11:
            print("Menú Operación Números")
            print(" 1) Presentar los números de 1 a n")
            print(" 2) Sumar los números de 1 a n")
            print(" 3) Múltiplo de cualquier numero")
            print(" 4) Presentar los divisores de un numero")
            print(" 5) Numero Primo")
            print(" 6) Factorial de cualquier numero")
            print(" 7) Fibonacci de una serie de n números")
            print(" 8) Perfecto")
            print(" 9) Primos gemelos")
            print(" 10) Números amigos")
            print("11) Salir")
            
            while True:
                try:
                    opcion = int(input("Ingresar una opción: "))
                    if opcion not in range(1, 12):
                        print("Ingresar una opción correcta")
                    else:
                        break
                except ValueError:
                    print("Ingresar una opción correcta")
            
            if opcion != 11:
                if opcion in range(1, 9):
                    while True:
                        try:
                            num = int(input("Ingresar un número: "))
                            if num > 0:
                                break
                            else:
                                print("Ingresar un número positivo mayor a 0")
                        except ValueError:
                            print("Ingrese los valores correctos")
                else:
                    while True:
                        try:
                            num1 = int(input("Ingrese un número: "))
                            num2 = int(input("Ingrese otro número: "))
                            if num1 > 0 and num2 > 0:
                                break
                            else:
                                print("Ingrese un número positivo mayor a 0")
                        except ValueError:
                            print("Ingresar los valores correctos")
            
                if opcion == 1:
                    operBasica.numeros(num)
                
                elif opcion == 2:
                    operIntermedia.numeros(num)
                
                elif opcion == 3:
                    operIntermedia.multiplo(num)
                
                elif opcion == 4:
                    operIntermedia.divisores(num)
                
                elif opcion == 5:
                    operIntermedia.primos(num)
                
                elif opcion == 6:
                    operIntermedia.factorial(num)
                
                elif opcion == 7:
                    operIntermedia.fibonacci(num)
                
                elif opcion == 8:
                    operIntermedia.perfecto(num)
                
                elif opcion == 9:
                    operIntermedia.primosGemelos(num1, num2)
                else:  
                    operIntermedia.amigos(num1, num2)
            
            else:
                print("Gracias")
            input("\nPulsa Enter para salir")
            
