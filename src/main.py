from flask import Flask, request, jsonify, redirect, url_for, json, session
from dotenv import load_dotenv
from controllers.controlador_alumno import get_user_student
from controllers.controlador_asesor import get_user_teacher
from flask_cors import CORS,cross_origin
from flask_wtf.csrf import CSRFProtect
from flask_wtf.csrf import generate_csrf
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from config import config
from database.db import get_connection
import json
load_dotenv()

# Models
from models.ModelUser import ModelUser

# Entities:

from models.entities.User import User

app = Flask(__name__)
CORS(app, origins='http://localhost:5173')
csrf = CSRFProtect()
jwt = JWTManager(app)


@app.route("/api/usuario", methods = ['POST', 'GET'])
@cross_origin()
@jwt_required()
def usuario():
    if request.method == 'GET':
        alumnos = get_user_student()
        asesores = get_user_teacher()
        return jsonify({'message': {'alumnos':alumnos, 'asesores':asesores}})

    if request.method == 'POST':
        
        return jsonify({'message': 'funcionando'})

@app.route("/api/docs", methods = ['POST', 'GET'])
def upload_file():
    file = request.files['file']
    if file:
        print(file.save(file.filename))
        return 'El archivo se ha recibido correctamente.'
    return 'No se ha recibido ningún archivo.', 400

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=="POST":
        recieve_json = request.get_json()
        connection = get_connection()
        user = User(0,recieve_json.get('user'),recieve_json.get('passw'))
        logged_user = ModelUser.login(connection,user)
        if logged_user != None:
            if logged_user.passw:
                access_token = create_access_token(identity=logged_user.id)
                return jsonify({'message': 'Contraseña correcta', 'data': json.loads(json.dumps(logged_user.__dict__)),'access_token': access_token})
            else:
                return jsonify({'message': 'Contraseña invalida'})
        else:
            return jsonify({'message': 'Usuario no encontrado'})
    else:
        return jsonify({'message': 'retorno'})

@app.route('/logout')
def logout():
    return jsonify({'message': 'Sesión cerrada correctamente'})

@app.route('/get_csrf_token', methods=['GET'])
def get_csrf_token():
    csrf_token1 = generate_csrf()
    return jsonify({'csrf_token': csrf_token1})

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.run(port=5001)