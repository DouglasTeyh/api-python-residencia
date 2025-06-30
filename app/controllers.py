from app.models import Usuario
from app.data import usuarios, salvar_usuarios

def adicionar_usuario(nome, email):
    # Evita emails duplicados
    if any(u.email == email for u in usuarios):
        return None
    novo_usuario = Usuario(nome=nome, email=email)
    usuarios.append(novo_usuario)
    salvar_usuarios()
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
        usuarios = [u for u in usuarios if u.id != usuario_id]
        salvar_usuarios()
        return True
    else:
        return False

def atualizar_usuario(usuario_id, nome, email):
    # Verifica se o email já existe em outro usuário diferente do atual
    if any(u.email == email and u.id != usuario_id for u in usuarios):
        return None

    for usuario in usuarios:
        if usuario.id == usuario_id:
            usuario.nome = nome
            usuario.email = email
            salvar_usuarios()
            return usuario
    return None
