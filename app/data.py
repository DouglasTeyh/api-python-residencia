import json
import os
from app.models import Usuario

CAMINHO_JSON = 'app/usuarios.json'
usuarios = []

def carregar_usuarios():
    global usuarios
    if os.path.exists(CAMINHO_JSON):
        with open(CAMINHO_JSON, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            usuarios = [Usuario(d['id'], d['nome'], d['email']) for d in dados]
    else:
        usuarios = []

def salvar_usuarios():
    with open(CAMINHO_JSON, 'w', encoding='utf-8') as f:
        json.dump([u.to_dict() for u in usuarios], f, indent=4, ensure_ascii=False)
