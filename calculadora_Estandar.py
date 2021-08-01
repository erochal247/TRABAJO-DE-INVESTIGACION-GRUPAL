from .calculadora import CALCULADORA

class calculadoraESTANDAR(CALCULADORA):
    def __init__(self, num1=0, num2=0):
        super().__init__(numero1=num1, numero2=num2)

    def MULTIPLICACION(self):
        multipli = (self.numero1 * self.numero2)
        return round(multipli, 2)

    def EXPONENTE(self):
        exponente = (self.numero1 ** self.numero2)
        return round(exponente, 2)

    def valorABSOLUTO(self, numero):
        return abs(numero)
