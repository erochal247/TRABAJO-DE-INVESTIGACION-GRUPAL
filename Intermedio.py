from .Basico import BASICO

class INTERMEDIO(BASICO):
    def numeros(self, num=10):
        print('Suma del número 1 al', num)
        suma = 0
        for i in range(1, num+1):
            suma += i
        print('El resultado de la suma es: ', suma)

    def factorial(self, num=5):
        print('Número factorial')
        fact = 1
        if num != 0:
            for i in range(1, num+1):
                fact *= i
        print('El factorial es:', fact)

    def fibonacci(self, num=20):
        print('Fibonacci hasta el', num, '\n' + '0')
        for i in range(num-1):
            n1 = 0
            n2 = 1
            for _ in range(i):
                r = n1 + n2
                n1 = n2
                n2 = r
            print(n2)

    def primosGemelos(self, num1=1, num2=10):
        if num1 != num2:
            n1 = 0
            n2 = 0
            if num1 > num2:
                n3 = num1
                num1 = num2
                num2 = n3
            print('Números primos gemelos del', num1, 'al', num2)
            
            if num2 > 4:
                for i in range(num1, num2+1):
                    incr = 2
                    primo = True
                    
                    while primo and incr < i:
                        if i % incr == 0:
                            primo = False
                        else:
                            incr += 1
                    if primo and not n1:
                        n1 = i
                    elif primo and n1:
                        n2 = i
                        if n2-n1 == 2:
                            print(n1, 'y', n2, 'Son números primos gemelos')
                        n1 = i
            else:
                print('No hay números gemelos.')
        else:
            print('Ingrese números diferentes')

    def amigos(self, num1=1184, num2=1210):
        if num1 != num2:
            print('Números amigos')
            sumA= 0
            sumB= 0
            
            if num1 > num2:
                n3 = num1
                num1 = num2
                num2 = n3
            
            for cont in range(1, num1+1):
                if num1 % cont == 0:
                    sumA += cont

            for cont in range(1, num2+1):
                if num2 % cont == 0:
                    sumB += cont

            if sumA == sumB and sumB == sumA:
                print('Son amigos')
            else:
                print('No son amigos')
        else:
            print('Ingrese números diferentes')
