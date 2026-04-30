import mysql.connector

conn = mysql.connector.connect(
    host='mysql-5153051-formulario.h.aivencloud.com',
    port=12714,
    user='avnadmin',
    password='TU_PASSWORD_AQUI',
    database='defaultdb',
    ssl_disabled=False
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM contactos')
rows = cursor.fetchall()

if rows:
    print(f"{'ID':<5} {'NAME':<20} {'EMAIL':<25} {'MESSAGE':<30} {'FECHA'}")
    print("-" * 90)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<25} {row[3]:<30} {row[4]}")
else:
    print("No hay registros en la tabla")

conn.close()
