from config import db
from .turmas_model import Turmas


class Professor(db.Model):
    __tablename__ = "professores"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.String(100), nullable=True)

    turmas = db.relationship('Turmas', back_populates='professor')

    def __init__(self, nome, idade, materia, observacoes):
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'idade': self.idade, 'materia': self.materia, 'observacoes': self.observacoes}

class criarProfessorErro(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem

class ProfessorNaoEncontrado(Exception):
    pass

def getPorIdProfessor(idProfessor):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessorNaoEncontrado
    return professor.to_dict()


