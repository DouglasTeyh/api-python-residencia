from flask import request, jsonify
from app import app
from app.controllers import adicionar_usuario, listar_usuarios, deletar_usuario, atualizar_usuario

#rota saudacao
@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({"mensagem": "Bem-vindo à API de exemplo"})

#Rota para adicionar um usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    '''a fazer'''

#rota para listar usuários
@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    '''a fazer'''

#rota para deletar um usuário
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    '''a fazer'''

#rota para atualizar um usuário
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    '''a fazer'''