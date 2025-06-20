from flask import request, jsonify
from app import app

@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({"mensagem": "Bem-vindo à API de exemplo"})
