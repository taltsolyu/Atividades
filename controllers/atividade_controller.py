from clients.pessoa_service_client import verifica_relacao_professor_disciplina as permissao_professor
from config import db
from flask import Blueprint, jsonify, request
from models import atividade_model as modelo
from models import professores_model as professor

atividades_api = Blueprint("atividades_api", __name__)

# Listagem geral
@atividades_api.get("/")
def exibir_todas():
    lista = modelo.listar_atividades()
    return jsonify(lista)

# Buscar por ID
@atividades_api.get("/<int:atividade_id>")
def buscar_por_id(atividade_id):
    atividade = modelo.obter_atividade(atividade_id)
    if atividade is None:
        return {"erro": "Atividade não encontrada"}, 404
    return atividade

# Buscar por ID + filtro professor
@atividades_api.get("/<int:atividade_id>/professor/<int:prof_id>")
def buscar_para_professor(atividade_id, prof_id):
    atividade = modelo.obter_atividade(atividade_id)
    if not atividade:
        return jsonify({"erro": "Registro de atividade não encontrado"}), 404

    autorizado = permissao_professor(prof_id, atividade.get("id_disciplina"))

    if not autorizado:
        atividade_filtrada = {
            chave: valor for chave, valor in atividade.items() if chave != "respostas"
        }
        return jsonify(atividade_filtrada)
    return jsonify(atividade)

@atividades_api.post("/")
def criarAtividade():
    try:
        dados = request.get_json()
        return modelo.criarAtividade(dados)
    except professor.ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 400

@atividades_api.route("/<int:id>", methods=['PUT'])
def attAtividade(id):
    dados = request.json
    try:
        return jsonify(modelo.attAtividade(id, dados))
    except modelo.AtividadeNotFound:
        return jsonify({'message': 'Atividade não encontrada'}), 400

@atividades_api.route("/<int:id>", methods=['DELETE'])
def deleteAtividade(id):
    try:
        return jsonify(modelo.deletarAtividade(id)), 200
    except modelo.AtividadeNotFound:
            return jsonify({'message': 'Professor não encontrado'}), 400