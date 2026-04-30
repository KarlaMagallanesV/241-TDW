from flask import Flask, request, render_template, flash
import pymysql

# Inicialización de Flask
app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'

# Configuración de conexión a Aiven MySQL
DB_CONFIG = {
    'host': 'mysql-5153051-formulario.h.aivencloud.com',
    'port': 12714,
    'user': 'avnadmin',
    'password': 'TU_PASSWORD_AQUI',
    'database': 'defaultdb',
    'ssl': {'ca': None},
    'cursorclass': pymysql.cursors.DictCursor
}

def get_connection():
    return pymysql.connect(**DB_CONFIG)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        print(f"[FORMULARIO] name={name} | email={email} | message={message}")

        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO contactos (name, email, message) VALUES (%s, %s, %s)",
                (name, email, message)
            )
            conn.commit()
            cur.close()
            conn.close()
            print("[DB] Guardado correctamente en la base de datos")
            flash('Contacto guardado exitosamente!')
        except Exception as e:
            flash(f'Error al guardar: {str(e)}', 'error')
    return render_template('contact.html')

# Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)
