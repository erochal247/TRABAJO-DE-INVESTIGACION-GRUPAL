class CALCULADORA:
    def __init__(self, num1=0, num2=0):
        self.numero1 = num1
        self.numero2 = num2


    def SUMA(self):
        suma = (self.numero1 + self.numero2)
        return round(suma, 2)

    def RESTA(self):
        resta = (self.numero1 - self.numero2)
        return round(resta, 2)

    def MULTIPLICACION(self):
        multipli = self.numero1 * self.numero2
        return multipli

    def DIVISION(self):
        if self.numero2 == 0: 
            return 0
        division = (self.numero1 / self.numero2)
        return round(division, 2)
