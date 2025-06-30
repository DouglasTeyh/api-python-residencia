from app.models import Usuario
from app.data import usuarios

def adicionar_usuario(nome, email):
    for usuario in usuarios:
        if usuario.email == email:
            return None
    
    novo_id = len(usuarios) + 1
    novo_usuario = Usuario(novo_id, nome, email)
    usuarios.append(novo_usuario)
    return novo_usuario

def listar_usuarios():
    return [usuario.to_dict() for usuario in usuarios]

def deletar_usuario(usuario_id):
    global usuarios
    usuario_encontrado = None

    for usuario in usuarios:
        if usuario.id == usuario_id:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        usuarios = [usuario for usuario in usuarios if usuario.id != usuario_id]
        return True
    else:
        return False

def atualizar_usuario(usuario_id, nome, email):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            usuario.nome = nome
            usuario.email = email
            return usuario
    return None
