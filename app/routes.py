from flask import request, jsonify
from app import app
from app.controllers import adicionar_usuario, listar_usuarios, deletar_usuario, atualizar_usuario

#rota saudacao
@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({"mensagem": "Seja bem-vindo ao sistema de gerenciamento de usuários!"})

#Rota para adicionar um usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    if not nome or not email:
        return jsonify({"erro": "Nome e email são obrigatórios"}), 400
    usuario = adicionar_usuario(nome, email)
    return jsonify(usuario.to_dict()), 201

#rota para listar usuários
@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    return jsonify(listar_usuarios())

#rota para deletar um usuário
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar(id):
    deletar_usuario(id)
    return jsonify({"mensagem": "Usuário deletado com sucesso"})

#rota para atualizar um usuário
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    usuario = atualizar_usuario(id, nome, email)
    if usuario:
        return jsonify(usuario.to_dict())
    else:
        return jsonify({"erro": "Usuário não encontrado"}), 404