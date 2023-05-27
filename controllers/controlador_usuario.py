from database.db import get_connection

def get_user():
    connection = get_connection()
    users = []
    resultados = []
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT U.Codigo_usuario, U.Nom_usuario, U.Passw, U.Estado as Estado_Usuario, 
            U.Codigo_detalle_usuario, DU.Codigo_direccion, DU.Codigo_Descripcion, DU.Codigo_tipo_doc_identificacion,
            DU.Nombre, DU.Apellido, DU.Sexo, DU.Telefono, DU.Num_doc, D.Descripcion, D.Distrito, D.Ciudad,
            D.Departamento, D.Estado as Estado_Direccion, C.Descripcion as Correo, C.Estado as Estado_Correo,
            A.Codigo_tipo_plan_alumno, A.Filial, A.Programa, A.Orcid, A.Ciclo
            FROM usuario AS U
            INNER JOIN detalle_usuario AS DU ON U.Codigo_detalle_usuario = DU.Codigo_detalle_usuario
            INNER JOIN direccion as D ON DU.Codigo_direccion = D.Codigo_direccion
            INNER JOIN correo as C ON DU.Codigo_descripcion = C.Descripcion
            INNER JOIN alumno as A ON U.Codigo_usuario = A.Codigo_alumno
        """)
        users = cursor.fetchall()
        for resultado in users:
            usuario = {
            'Codigo_usuario': resultado[0],
            'Nom_usuario': resultado[1],
            'Passw': resultado[2],
            'Estado_Usuario': resultado[3],
            'Codigo_detalle_usuario': resultado[4],
            'Codigo_direccion': resultado[5],
            'Codigo_Descripcion': resultado[6],
            'Codigo_tipo_doc_identificacion': resultado[7],
            'Nombre': resultado[8],
            'Apellido': resultado[9],
            'Sexo': resultado[10],
            'Telefono': resultado[11],
            'Num_doc': resultado[12],
            'Descripcion': resultado[13],
            'Distrito': resultado[14],
            'Ciudad': resultado[15],
            'Departamento': resultado[16],
            'Estado_Direccion': resultado[17],
            'Correo': resultado[18],
            'Estado_Correo': resultado[19],
            'Codigo_tipo_plan_alumno': resultado[20],
            'Filial': resultado[21],
            'Programa': resultado[22],
            'Orcid': resultado[23],
            'Ciclo': resultado[24]
            }   
            resultados.append(usuario)
            
    connection.commit()
    connection.close()
    return resultados


