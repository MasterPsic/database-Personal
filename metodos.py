class Metodo():
    def ListarE(self, persona):
        contador = 1
        for emp in persona:
            datos = "{0} DNI: {1} NOMBRE: {2} APELLIDO: {3} Fecha Nac: {4} Direccion: {5}"
            print(datos.format(contador, emp[0], emp[1], emp[2], emp[3], emp[4]))
            contador += 1

    def registrar (self):
        print('Agregar Usuario')
        dniCorrecto = False
        while not dniCorrecto:
            dni = input('Dni:')
            if len(dni) == 8:
                if dni.isdigit():
                    dniCorrecto = True
                else:
                    print('Debe contener solo numeros')
            else:
                print('Dni invalido,debe contener 8 digitos')
        nombreCorrecto = False
        while not nombreCorrecto:
            nombre = input('Nombre: ').title()
            if len(nombre) > 2:
                if len(nombre) <= 12:
                    if nombre.isalpha():
                        nombreCorrecto = True
                        print(nombre)
 
 
 
                    else:
                        print('No superar 12 caracteres')
 
            else:
                print('Debe contener al menos 3 caracteres')
        apellido = input('Apellido: ')
        fecha = input('Fech Nac: ')
        direccion = int(input('Direccion: '))
        empleado = (dni, nombre,apellido, fecha, direccion)
        return empleado
    
    def actualizar(self, empleado):
        print('Actualizar Empleado')
        dniExiste = False
        dni = input('Dni Actualizar: ')
        for emp in empleado:
            if emp[0]  == dni:
                dniExiste = True
                break
        if dniExiste:
            nombre = input('Nombre: ').title()
            apellido = input('Apellido: ')
            fecha = input('FechNac: ')
            direccion= int (input('Direccion: '))
            empleado = (dni, nombre, apellido, fecha, direccion)
        else:
            empleado = None
        return empleado
    
    # Sugerido: def eliminar(self empleado)
class Metodo():
    # ... (otras funciones)

    def eliminar(self):
        print('Eliminar Empleado')
        dniCorrecto = False
        while not dniCorrecto:
            dni = input('Ingrese el DNI del empleado a eliminar: ')
            if len(dni) == 8 and dni.isdigit():
                dniCorrecto = True
            else:
                print('DNI inválido. Debe contener 8 dígitos numéricos.')

        confirmacion = input('¿Está seguro de que desea eliminar al empleado? (S/N): ')
        if confirmacion.upper() == 'S':
            return dni  # Devolvemos el DNI para que la función de eliminación lo use
        else:
            print('Operación de eliminación cancelada.')
            return None
