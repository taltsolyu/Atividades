import requests

URL_BASE = "http://localhost:5001/pessoas"

def verifica_relacao_professor_disciplina(professor_id, disciplina_id):
    endereco = f"{URL_BASE}/leciona/{professor_id}/{disciplina_id}"
    
    try:
        resposta = requests.get(endereco)
        if resposta.status_code == 200:
            conteudo = resposta.json()
            if conteudo.get("isok", False):
                return conteudo.get("leciona", False)
    except requests.exceptions.RequestException as erro:
        print("Erro ao consultar serviço de pessoas:", erro)
    
    return False
