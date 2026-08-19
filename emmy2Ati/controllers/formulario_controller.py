from models.formulario_model import FormularioModel

class FormularioController:


    @staticmethod
    def create_formulario(user_id, data):
        nome = data.get('nome')
        email = data.get('email')
        data_nascimento = data.get('data_nascimento')
        cpf = data.get('cpf')
        genero = data.get('genero')

        if not nome or not email or not data_nascimento or not cpf or not genero:
            return {"error": "Todos os campos são obrigatorios"}, 400
        
        formulario = FormularioModel.create_formulario
        (user_id, nome, email,cpf, genero)
        if formulario:
            return{"message": "Formulario criado com sucesso"},201
        return{"error": "Erro ao criar formulario"},500