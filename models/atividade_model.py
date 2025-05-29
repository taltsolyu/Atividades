from config import db
from sqlalchemy.inspection import inspect
from . import professores_model as professor
 
class Atividade(db.Model):
    __tablename__ = "atividades"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_disciplina = db.Column(db.String(100))
    enunciado = db.Column(db.String(100),nullable=False)
    respostas = db.Column(db.JSON,nullable=False)
    id_professor = db.Column(db.Integer)
    
    def __init__(self, nome_disciplina, enunciado, respostas, id_professor):
        self.nome_disciplina = nome_disciplina
        self.enunciado = enunciado
        self.respostas = respostas
        self.id_professor = id_professor

    def to_dict(self):
        return {'id': self.id, 'nome_disciplina': self.nome_disciplina, 'enunciado': self.enunciado, 'respostas': self.respostas, "id_professor": self.id_professor}

class criarAtividadeErro(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem

class AtividadeNotFound(Exception):
    pass

def listar_atividades():
    atividades = Atividade.query.all()
    return [atividade.to_dict() for atividade in atividades]

def criarAtividade(dados):
    if not dados.get('nome_disciplina') or not dados.get('enunciado') or not dados.get('respostas') or not dados.get('id_professor'):
        raise criarAtividadeErro("Campos obrigatórios ausentes ou inválidos.")
    print("ID do professor recebido:", dados.get("id_professor"))
    professor.getPorIdProfessor(dados["id_professor"])

    nova_atividade = Atividade(
        nome_disciplina=dados["nome_disciplina"],
        enunciado=dados["enunciado"],
        respostas=dados["respostas"],
        id_professor=dados["id_professor"]
    )
    print(nova_atividade)
    db.session.add(nova_atividade)
    db.session.commit()
    return nova_atividade.to_dict()


def obter_atividade(id_atividade):
    for atividade in Atividade.query.all():
        if atividade['id_atividade'] == id_atividade:
            return atividade
    raise AtividadeNotFound

def attAtividade(id, novaAtividade):
    atividade = Atividade.query.get(id)
    if not atividade:
        raise AtividadeNotFound
    atividade = merge_objects(atividade, Atividade(**novaAtividade))
    db.session.commit()
    return atividade.to_dict()

def merge_objects(obj1, obj2):
    for attr in inspect(obj1).mapper.column_attrs:
        key = attr.key
        new_value = getattr(obj2, key)

        if new_value is not None and new_value != getattr(obj1, key):
            setattr(obj1, key, new_value)

    return obj1

def deletarAtividade(idAtividade):
    atividade = Atividade.query.get(idAtividade)
    if not atividade:
        raise AtividadeNotFound
    db.session.delete(atividade)
    db.session.commit()
    return atividade.to_dict()