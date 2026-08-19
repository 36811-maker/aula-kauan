from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models.user_model import UserModel

class UserControllers:

    @staticmethod
    def register_user(data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Nome de usuario e senha são obrigatorios"}

        hashed_password = generate_password_hash(password)

        if UserModel.create_user(username, hashed_password):
            return{"message": "Usuario registrado com sucesso"},20
        
        return{"error": "Nome de usuario ja existe"}, 400

    @staticmethod
    def login_user (data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Nome de usuario e senha são obrigatorios"},

        user = UserModel.find_by_username(username)
        if user and check_password_hash(user['password'], password):
            acess_token = create_access_token(identify=str(user['id']))
            return {"acess_token": acess_token}, 200

        return{"error": "nome de usuario ou senha invalidos"}, 401