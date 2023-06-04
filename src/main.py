from flask import Flask, send_file, request, jsonify, redirect, url_for, json, session
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
from service.compareWord import resaltar_diferencias, resaltar_diferencias_documento2
from wtforms import FileField
import os
from zipfile import ZipFile

load_dotenv()

# Models
from models.ModelUser import ModelUser

# Entities:

from models.entities.User import User

app = Flask(__name__)
CORS(app)

jwt = JWTManager(app)


@cross_origin()
@app.route("/api/usuario/alumno", methods = ['POST', 'GET'])
@jwt_required()
def usuario():
    if request.method == 'GET':
        alumnos = get_user_student()
        return jsonify({'message': {'alumnos':alumnos}})

    if request.method == 'POST':
        
        return jsonify({'message': 'funcionando'})
    
@cross_origin()
@app.route("/api/usuario/asesor", methods = ['POST', 'GET'])
@jwt_required()
def usuario():
    if request.method == 'GET':
        asesores = get_user_teacher()
        return jsonify({'message': {'asesores':asesores}})

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

@cross_origin()
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

@app.route('/compareWord', methods=['POST'])
def compareWord():
    documento1 = request.files['documento1']
    documento2 = request.files['documento2']
    outPath = "./documents/documento1_comparado.docx"
    outPath_2 = "./documents/documento2_comparado.docx"
    resaltar_diferencias(documento1,documento2)
    resaltar_diferencias_documento2(documento1,documento2)

    nombre_zip = 'zip/archivos.zip'
    with ZipFile(nombre_zip, 'w') as zip:
        zip.write(outPath, os.path.basename(outPath))
        zip.write(outPath_2, os.path.basename(outPath_2))

    return send_file(nombre_zip, as_attachment=True)

@app.route('/descargar_documento', methods=['GET'])
def descargar_documento():
    # Ruta del archivo de Word que deseas enviar
    ruta_documento = "./documents/documento1_comparado.docx"

    return send_file(ruta_documento, as_attachment=True)

@cross_origin()
@app.route('/get_csrf_token', methods=['GET'])
def get_csrf_token():
    csrf_token1 = generate_csrf()
    return jsonify({'csrf_token': csrf_token1})

if __name__ == '__main__':
    app.config.from_object(config['development'])
   
    app.run(port=5001)