from database.db import get_connection

def get_user_teacher():
    connection = get_connection()
    users = []
    resultados = []
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT U.Codigo_usuario, U.Nom_usuario, U.Passw, U.Estado as Estado_Usuario, 
            U.Codigo_detalle_usuario, DU.Codigo_direccion, DU.Correo, DU.Codigo_tipo_doc_identificacion,
            DU.Nombre, DU.Apellido, DU.Sexo, DU.Telefono, DU.Num_doc, D.Descripcion, D.Distrito, D.Ciudad,
            D.Departamento, D.Estado as Estado_Direccion, C.Estado as Estado_Correo, CD.Codigo_asesor,
            CD.Codigo_alumno, CD.Codigo_curso, CD.Grupo, TA.Tipo, CASE ASE.Es_jurado WHEN 0 THEN 'No' 
            WHEN 1 THEN 'Si' END AS Es_jurado
            FROM curso_detalle AS CD
            INNER JOIN asesor as ASE ON CD.Codigo_asesor = ASE.Codigo_asesor
            INNER JOIN tipo_asesor as TA ON ASE.Codigo_tipo_asesor = TA.Codigo_tipo_asesor
            INNER JOIN usuario as U ON ASE.Codigo_asesor = U.Codigo_usuario
            INNER JOIN detalle_usuario AS DU ON U.Codigo_detalle_usuario = DU.Codigo_detalle_usuario
            INNER JOIN direccion as D ON DU.Codigo_direccion = D.Codigo_direccion
            INNER JOIN correo as C ON DU.Correo = C.Correo
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
            'Correo': resultado[6],
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
            'Estado_Correo': resultado[18],
            'Codigo_asesor': resultado[19],
            'Codigo_alumno': resultado[20],
            'Codigo_curso': resultado[21],
            'Grupo': resultado[22],
            'Tipo_Asesor': resultado[23],
            'Es_jurado': resultado[24]
            }   
            resultados.append(usuario)
            
    connection.commit()
    connection.close()
    return resultados


