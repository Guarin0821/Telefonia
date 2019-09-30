from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)


#Mysql Conexion
app.config['MYSQL_HOST'] =  'localhost'
app.config['MYSQL_USER'] =  'jordy'
app.config['MYSQL_PASSWORD'] =  'jordy'
app.config['MYSQL_DB'] =  'flaskcontacts'
mysql = MySQL(app)


#settings
app.secret_key = 'mysecretkey'

@app.route('/linea')
def  linea():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM linea')
    data = cur.fetchall()
    return render_template('linea.html', linea = data)

@app.route('/registrar_equipo')
def registrar_equipo():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM equipo')
    data = cur.fetchall()
    return render_template('registrar_equipo.html', equipo = data)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM  contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    
    if request.method =='POST': # si tiene datos haga esto

        documento=request.form['documento']
        name=request.form['name']
        lastname=request.form['lastname']
        fecha_nacimiento=request.form['fecha_nacimiento']      # captura los datos 
        telefono_fijo=request.form['telefono_fijo']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO  contacts ( documento, name, lastname, fecha_nacimiento, telefono_fijo) VALUES ( %s, %s, %s, %s, %s)',
        ( documento, name, lastname, fecha_nacimiento, telefono_fijo))
        mysql.connection.commit()
        flash('Contacto Agregado Exitosamente!!')
    
        return redirect(url_for('index'))

       


@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s' , (id))
    data = cur.fetchall()

    return render_template('edit-contact.html', contact = data[0])

@app.route('/edit/<id>')
def get_registrar_equipo(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM equipo WHERE id = %s' , (id))
    data = cur.fetchall()

    return render_template('edit_equipo.html', equipo = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):

    if request.method == 'POST':
        documento=request.form['documento']
        name=request.form['name']
        lastname=request.form['lastname']
        fecha_nacimiento=request.form['fecha_nacimiento']       
        telefono_fijo=request.form['telefono_fijo']
        cur = mysql.connection.cursor()
        cur.execute(""" 
        UPDATE contacts
        SET documento = %s,
            name = %s,
            lastname = %s,
            fecha_nacimiento = %s,
            telefono_fijo = %s
            WHERE id = %s
        """, (documento, name, lastname, fecha_nacimiento, telefono_fijo, id))
        mysql.connection.commit()
        flash('Contacto Actualizado Exitosamente!!')
        return redirect(url_for('index'))

@app.route('/update1/<id>', methods = ['POST'])
def update_equipo(id):

    if request.method == 'POST':

        linumerolinea=request.form['linumerolinea']
        equmarca=request.form['equmarca']
        equdescripcion=request.form['equdescripcion']
        equestado=request.form['equestado']   
        cur = mysql.connection.cursor()
        cur.execute(""" 
        UPDATE equipo
        SET linumerolinea = %s,
            equmarca = %s,
            equdescripcion = %s,
            equestado = %s
            WHERE id = %s
        """, (linumerolinea, equmarca, equdescripcion, equestado, id))
        mysql.connection.commit()
        flash('Contacto Actualizado Exitosamente!!')
        return redirect(url_for('registrar_equipo'))


@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'. format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado Exitosamente!')
    return redirect(url_for('index'))

    
@app.route('/registrar_equipo', methods=['POST'])
def add_equipo():
    
    if request.method =='POST': # si tiene datos haga esto

        linumerolinea=request.form['linumerolinea']
        equmarca=request.form['equmarca']
        equdescripcion=request.form['equdescripcion']
        equestado=request.form['equestado']      # captura los datos 
       

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO  equipo ( linumerolinea, equmarca, equdescripcion, equestado) VALUES ( %s, %s, %s, %s)',
        ( linumerolinea, equmarca, equdescripcion, equestado))
        mysql.connection.commit()
        flash('Contacto Agregado Exitosamente!!')
    
        return redirect(url_for('registrar_equipo'))

@app.route('/linea', methods=['POST'])
def add_linea():
    
    if request.method =='POST': # si tiene datos haga esto

        linumerodelinea=request.form['linumerodelinea']
        perid=request.form['perid']
        linestado=request.form['linestado']   # captura los datos 
       

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO  linea ( linumerodelinea, perid, linestado) VALUES ( %s, %s, %s)',
        ( linumerodelinea, perid, linestado))
        mysql.connection.commit()
        flash('Contacto Agregado Exitosamente!!')
    
        return redirect(url_for('linea'))

if __name__ == '__main__':    
    app.run(port = 3000, debug= True) 