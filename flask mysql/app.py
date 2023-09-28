from flask import Flask, render_template, request flash, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'persona'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/listado')
def listado():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT empleadodb.dni, empleado.nombre, empleado.apellido, empleado.fechNac,
                direccion.nombre, FROM empleado, direccion
                where empleado.domicilio = direccion.id""")
    datos = cur.fetchall()
    print(datos)
    return render_template('home.html', empleado =datos)

@app.route('registroEmpleado', methods = ['GET', 'POST'])
def registroEmpleados():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM.direcion")
        datos = cur.fetchall()
        #print(datos)
        return render_template('registro.html', domicilio = datos)
    if request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha = request.form['fecha']
        direccion = request.form['direccion']
        cur = mysql.connection.cursor()
        cur.execute('''insert into empleado(dni, nombre, apellido FechNac, domicilio)
                    values(%s, %s, %s, %s)''', (dni, nombre, apellido, fecha, direccion))
        mysql.connection.commit()

        return redirect(url_for('listado'))
    
@app.route('/editar/<id>')
def obtener(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM empleado where dni =%s" % (id))
    datos = cur.fetchall()
    print(datos)
    return render_template('editar.html', empleado = datos [0])
    
@app.route('/actualizarEmpleado/<dni>', methods = ['POST'])
def actualizarEmpleado(dni):
    if request.method =='POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha = request.form['fecha']
        direccion = request.form['direccion']
    '   cur = mysql.connection.cursor()
        cur.execute('''update empleado set nombre = %s,
                    apellido = %s,
                    fechNac = %s,
                    domicilio = %s,
                    where dni = %s''', (nombre, apellido, fecha, direccion, dni))
        mysql.connection.commit()
        return redirect(url_for('listado'))

@app.route('/eliminar/<string:dni>')
def eliminar(dni):
    cur = mysql.connection.cursor()
    cur.execute('delete from empleado where dni = [0]'.format(dni))
    mysql.connection.commit()
    return redirect(url_for('listado'))

                    
if __name__ == '__main__':
    app.run(port= 3000, debug=True)


