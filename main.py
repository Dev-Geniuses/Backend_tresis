from flask import Flask, request, jsonify
from dotenv import load_dotenv
from controllers.controlador_alumno import get_user_student
from controllers.controlador_asesor import get_user_teacher
from flask_cors import cross_origin
load_dotenv()

app = Flask(__name__)

@app.route("/api/usuario", methods = ['POST', 'GET'])
@cross_origin()
def usuario():
    if request.method == 'GET':
        alumnos = get_user_student()
        asesores = get_user_teacher()
        return jsonify({'message': {'alumnos':alumnos, 'asesores':asesores}})

    if request.method == 'POST':
        
        return jsonify({'message': 'funcionando'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)