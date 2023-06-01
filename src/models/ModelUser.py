from .entities.User import User 
import json
class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT Codigo_usuario, Nom_usuario, passw FROM usuario
                    WHERE Nom_usuario = '{}'""".format(user.user))
                
                result = cursor.fetchone()
                if result != None:
                    user = User(result[0],result[1], User.check_password(result[2], user.passw))
                    return user
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self, db, id):
        try:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT Codigo_usuario, Nom_usuario FROM usuario
                    WHERE Codigo_usuario = '{}'""".format(id))
                
                result = cursor.fetchone()
                if result != None:
                    return User(result[0],result[1], None)
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)