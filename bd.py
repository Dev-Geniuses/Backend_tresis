import pymysql

def obtener_conexion():
    return pymysql.connect(
        host='db4free.net',
        user='admintresis',
        password='devhack123',
        db='tresis'
    )