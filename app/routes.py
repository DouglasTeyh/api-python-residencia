from flask import request, jsonify, render_template
from app import app
from app.controllers import adicionar_usuario, listar_usuarios, deletar_usuario, atualizar_usuario

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({"mensagem": "Bem-vindo à API de exemplo."})

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')

    if not nome or not email:
        return jsonify({'erro': 'Nome e email são obrigatórios'}), 400

    novo_usuario = adicionar_usuario(nome, email)
    if novo_usuario is None:
        return jsonify({'erro': 'Email já cadastrado'}), 400
    return jsonify(novo_usuario.to_dict()), 201

@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    return jsonify(listar_usuarios())

@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
def obter_usuario_por_id(usuario_id):
    from app.data import usuarios
    usuario = next((u for u in usuarios if u.id == usuario_id), None)
    if usuario:
        return jsonify(usuario.to_dict())
    return jsonify({"erro": "Usuário não encontrado"}), 404


@app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def deletar(usuario_id):
    sucesso = deletar_usuario(usuario_id)
    if sucesso:
        return jsonify({"mensagem": "Usuário deletado com sucesso"})
    else:
        return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def atualizar(usuario_id):
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')

    if not nome or not email:
        return jsonify({"erro": "Nome e email são obrigatórios"}), 400

    usuario = atualizar_usuario(usuario_id, nome, email)
    if usuario is None:
        return jsonify({"erro": "Email já cadastrado"}), 400

    return jsonify(usuario.to_dict())
