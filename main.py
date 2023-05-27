from flask import Flask, request, jsonify
from dotenv import load_dotenv
from controllers.controlador_usuario import get_user
load_dotenv()

app = Flask(__name__)

@app.route("/api/usuario", methods = ['POST', 'GET'])
def usuario():
    if request.method == 'GET':
        usuarios = get_user()
        print(usuarios)
        return jsonify({'mensaje': usuarios})

    if request.method == 'POST':
        
        return jsonify({'mensaje': 'funciona p cholo EL POST'})

if __name__ == '__main__':
    app.run(debug=True)