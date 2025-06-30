import json
import os
from app.models import Usuario, ids_existentes

CAMINHO_JSON = os.path.join(os.path.dirname(__file__), 'usuarios.json')
usuarios = []

def carregar_usuarios():
    global usuarios
    if os.path.exists(CAMINHO_JSON):
        try:
            with open(CAMINHO_JSON, 'r', encoding='utf-8') as f:
                conteudo = f.read().strip()
                if conteudo:
                    dados = json.loads(conteudo)
                    usuarios = [Usuario(d['id'], d['nome'], d['email']) for d in dados]
                    ids_existentes.clear()
                    for u in usuarios:
                        ids_existentes.add(u.id)
                else:
                    usuarios = []
        except json.JSONDecodeError as e:
            print(f"Erro ao carregar JSON: {e}")
            usuarios = []
    else:
        usuarios = []

def salvar_usuarios():
    with open(CAMINHO_JSON, 'w', encoding='utf-8') as f:
        json.dump([u.to_dict() for u in usuarios], f, indent=4, ensure_ascii=False)
