from generico import Generico
from metodo import Metodo

class Menu():

    def menu(self):
        #avanzar = True
        #while not correcta:
        while True:
            # correcta = False
            # while not correcta:

            print('''
                1. Listar
                2. Agregar
                3. Editar Empleado
                6. Modificar Usuario
                7. Eliminar
                0. Finalizar''')
            opcion = int(input('Elija una opcion: '))
            if opcion < 0 and opcion > 7:
                print("Opcion Incorrecta")
            elif == 0:
               # avanzar 0 False
                print('Fin del programa')
                exit()
            else:
                # correcta = True
                self.opciones(opcion)
    def opciones(self, opcion):
        generico = Generico()


        if opcion == 1:
            try:
                empleado = generico.listar()
                if len(empleado) > 0:
                    metodo.listarE(empleado)
                else:
                    print('No hay registros')
            except:
                print("ocurrio un Error")
        elif opcion == 2:
            empleado = metodoregistrar()
            try:
                generico.registrar(empleado)
            except:
                print("Error")

        elif opcion == 3:
            try:
                empleado = generico.listar()
            print("Empleado")
            if len(empleado)>0:
                emplea = metodo.actualizar(empleado)
                if emplea:
                    generico.actualizar(emplea)
                else:
                    print('No se encontro el empleado')
            else:
                print('No hay registros')
            except:
                  print('Error')
        

        elif opcion == 4:
            try:
            print("Eliminar")
        elif opcion == 6:
            self.salir()

menu = Menu()
menu.menu()

