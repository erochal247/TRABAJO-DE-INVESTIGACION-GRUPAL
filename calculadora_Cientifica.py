from .calculadora import CALCULADORA

class calculadoraCIENTIFICA(CALCULADORA):
    num_pi = 3.1416

    def __init__(self, num1=0, num2=0):
        super().__init__()
    
    def CIRCUNFERENCIA(self, rad):
        circunfe = (2 * self.num_pi) * rad
        return round(circunfe, 2)

    def areaCIRCULO(self, rad):
        circulo = (self.num_pi * (rad**2))
        return round(circulo, 2)

    def areaCUADRADO(self, lad):
        cuadrado = (lad * lad)
        return round(cuadrado, 2)
