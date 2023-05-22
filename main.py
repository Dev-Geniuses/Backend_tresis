from flask import Flask, request
from bd import obtener_conexion

app = Flask(__name__)

@app.route("/api/usuario", methods = ['POST', 'GET'])
def usuario():
    if request.method == 'GET':
        conexion = obtener_conexion()
        print(conexion)

if __name__ == '__main__':
    app.run(debug=True)