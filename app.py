from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

# Ruta de la base de datos
DATABASE = r'C:\Users\aleja\Desktop\III Semestre 2024\Base da datos relacionales\Proyecto-Flask\bdd.db'

# Función para conectar con la base de datos
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Para obtener resultados en formato de diccionario
    return conn

# Ruta principal (Menú principal)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para agregar pacientes
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        # Aquí capturas los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha_nacimiento = request.form['fecha_nacimiento']
        telefono = request.form['telefono']
        correo = request.form['correo']

        # Conexión a la base de datos e inserción de datos
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO Pacientes (Nombre, Apellido, Fecha_de_Nacimiento, Teléfono, Correo_Electronico) 
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, apellido, fecha_nacimiento, telefono, correo))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))  # Redirige a la página principal después de agregar
    return render_template('agregar.html')

# Ruta para buscar pacientes
@app.route('/buscar', methods=['GET'])
def buscar():
    nombre = request.args.get('nombre', '')
    conn = get_db_connection()
    pacientes = conn.execute('''
        SELECT * FROM Pacientes 
        WHERE Nombre LIKE ? OR Apellido LIKE ?
    ''', ('%' + nombre + '%', '%' + nombre + '%')).fetchall()
    conn.close()
    return jsonify([{'id': paciente['ID'], 'nombre': paciente['Nombre'], 'apellido': paciente['Apellido']} for paciente in pacientes])

# Ruta para modificar pacientes
@app.route('/modificar/<int:id>', methods=['GET', 'POST'])
def modificar(id):
    conn = get_db_connection()
    paciente = conn.execute('SELECT * FROM Pacientes WHERE ID = ?', (id,)).fetchone()

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha_nacimiento = request.form['fecha_nacimiento']
        telefono = request.form['telefono']
        correo = request.form['correo']

        conn.execute('''
            UPDATE Pacientes 
            SET Nombre = ?, Apellido = ?, Fecha_de_Nacimiento = ?, Teléfono = ?, Correo_Electronico = ?
            WHERE ID = ?
        ''', (nombre, apellido, fecha_nacimiento, telefono, correo, id))

        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    conn.close()
    return render_template('modificar.html', paciente=paciente)

# Ruta para eliminar pacientes
# Ruta para eliminar pacientes
@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Pacientes WHERE ID = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
