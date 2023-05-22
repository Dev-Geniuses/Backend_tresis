import pymysql

def obtener_conexion():
    return pymysql.connect(
        host='localhost:3307',
        user='root',
        password='',
        db='tresis'
    )