from generico import Generico
class Menu():
    def salir(self):
        exit()

    def menu(self):
        #avanzar = True
        #while not correcta:
        while True:
            opcion = int(input(f'''
                1. Listar
                2. Agregar
                3. Buscar
                4. Editar
                5. Eliminar
                6. Salir
Ingresa una opcion: '''))
            if opcion < 0 and opcion > 6:
                print("Opcion Incorrecta")
            else:
                self.opciones(opcion)
    def opciones(self, opcion):
        generico = Generico()
        if opcion == 1:
            try:
                empleado = generico.listar()
                if len(empleado) > 0:
                    print(empleado)
                else:
                    print('No hay empleados')
            except:
                print("ocurrio un Error")

        elif opcion == 2:
            print("Buscar")
        elif opcion == 3:
            print("Editar")
        elif opcion == 4:
            print("Eliminar")
        elif opcion == 6:
            self.salir()

menu = Menu()
menu.menu()

