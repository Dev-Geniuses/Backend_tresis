from flask import Flask, request, jsonify
from bd import obtener_conexion

app = Flask(__name__)

@app.route("/api/usuario", methods = ['POST', 'GET'])
def usuario():
    if request.method == 'GET':
        conexion = obtener_conexion()
        print(conexion)
        return jsonify({'mensaje': 'funciona p cholo'})

    if request.method == 'POST':
        conexion = obtener_conexion()
        
        return jsonify({'mensaje': 'funciona p cholo EL POST'})

if __name__ == '__main__':
    app.run(debug=True)