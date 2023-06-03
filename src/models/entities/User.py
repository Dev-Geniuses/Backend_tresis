from werkzeug.security import check_password_hash, generate_password_hash

class User():
    def __init__(self, id, user, passw) -> None:
        self.id = id
        self.user = user
        self.passw = passw

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
    # print(generate_password_hash('244123'))
    # print('hola')
    # print(generate_password_hash('123432'))