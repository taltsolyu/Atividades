from config import db
from datetime import datetime, date
from . import professores_model as professor

class Turmas(db.Model):
    __tablename__ = "turmas"

    id_turma = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'))
    professor = db.relationship('Professor', back_populates='turmas')

    def __init__(self, nome, descricao, ativo, professor_id):
        self.nome = nome
        self.descricao = descricao
        self.ativo = ativo
        self.professor_id = professor_id

    def to_dict(self):
        return {
            'id': self.id_turma,
            'nome': self.nome,
            'descricao': self.descricao,
            'ativo': self.ativo,
            'professor_id': self.professor_id
        }

class Turma_nao_encontrada(Exception):
    pass

def turma_por_id(id_turma):
    turma = Turmas.query.get(id_turma)
    if not turma:
        raise Turma_nao_encontrada(f'Turma não encontrada.')
    return turma.to_dict()

def lista_turmas():
    turmas = Turmas.query.all()
    return [turma.to_dict() for turma in turmas]

