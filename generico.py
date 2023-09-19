from mysql.connector import Error
import mysql.connector
class Generico():          
        def __init__(self):
            try:
                self.conexion = mysql.connector.connect(
                    host = 'localhost',
                    port = 3306,
                    user = 'root',
                    password ='',
                    database = 'persona'
                )
            except Error as ex:                           
                print('No se pudo realizar la conexion {0}'.format(ex))
        def listar(self):
            if self.conexion.is_connected():
                try:
                    cur = self.conexion.cursor()
                    cur.execute('select * from empleado')
                    respuesta = cur.fetchall()
                    return respuesta
                except Error as ex:
                       print ('No se pudo concretar listar: {0}'.format(ex))
                       
        def registrar (self, empleado):
            if self.conexion.is_connected():
                try:
                    cur = self.conexion.cursor()
                    sql = ("insert into empleado (dni, nombre, apellido, fechNac, domicilio) values ({0}, '{1}', '{2}', '{3}', {4})")
                    cur.execute(sql.format(empleado[0],empleado[1], empleado[2], empleado[3], empleado[4]))
                    self.conexion.commit()
                except Error as ex:
                    print('No se pudo registrar el empleado: {0}'.format(ex))

        def actualizar (self, empleado):
            if self.conexion.is_connected():
                try:
                    cur = self.conexion.cursor()
                    sql = """update empleado set nombre = '{0}', apellido = '{1}',
                            fechNac = '{2}', domicilio = {3}, where dni = {4}"""
                    cur.execute(sql.format(empleado[1], empleado[2], empleado[3], empleado[4], empleado[0]))
                    self.conexion.commit()
                    print ('Se actualizo el registro')
                except Error as ex:
                     print ('No se pudo actualizar al empleado: {0}'.format(ex))

        def eliminar(self, empleado):
            if self.conexion.is_connected():
                try:
                    cur = self.conexion.cursor()
                    sql = "delete from empleado where dni = {0}"
                    cur.execute(sql.format(empleado))
                    self.conexion.commit()
                    print ('Se Elimina Empleado')
                except Error as ex:
                    print ('No se pudo eliminar al Empleado: {0}'.format(ex))
        