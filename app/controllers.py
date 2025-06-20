from app.models import Usuario
from app.data import usuarios

def adicionar_usuario(nome, email):
    id = len(usuarios) + 1
    novo_usuario = Usuario(id, nome, email)
    usuarios.append(novo_usuario)
    return novo_usuario

def listar_usuarios():
    return [usuario.to_dict() for usuario in usuarios]

def deletar_usuario(id):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario.id != id]