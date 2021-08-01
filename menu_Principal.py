from menu_Calculadora import MENUCalculadora
from operaciones_con_Numeros import OperacionesConNumeros
from tratamiento_de_Lista import menu as Lista
from menu_Operaciones_Cadenas import menu as Operaciones_con_cadenas

class MenuPrincipal:
    def seleccion(self):
        opcion = 0
        while opcion != 5:
            print(" Menu Principal Bienvenidos")
            print(" 1) Calculadora")
            print(" 2) Operación Numeros")
            print(" 3) Tratamiento de Listas")
            print(" 4) Operaciones de Cadenas")
            print("5) Salir")

            while True:
                try:
                    opcion = int(input("Seleccione la opcion: "))
                    if opcion > 0 and opcion < 6: break
                    else: print("Ingrese la opcion correcta")
                except ValueError:
                    print("Ingresar el valor correcto")
            if opcion == 1: MENUCalculadora().menu()

            elif opcion == 2: OperacionesConNumeros().menu()

            elif opcion == 3: Lista()

            elif opcion == 4: Operaciones_con_cadenas()
        else:
            print("Gracias")
            input("\nPulsa Enter para poder salir")


if __name__ == '__main__':
    menu = MenuPrincipal()
    menu.seleccion()
