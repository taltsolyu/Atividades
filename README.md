## ⚠️ Instruções para executar o projeto
Para rodar este projeto corretamente, é necessário copiar o arquivo `app.db` para a **pasta raiz** onde o projeto foi clonado.

### 📂 Exemplo de caminho:
C:/projetos/app.db

Este arquivo já contém:

- ✅ Todas as estruturas de tabelas criadas
- 👨‍🏫 Um professor com **ID 1** cadastrado para testes

> Sem esse arquivo, o projeto pode gerar erros de integridade referencial ou falha ao acessar dados.

# 📚 Atividades API

API para gerenciamento de atividades acadêmicas, incluindo funcionalidades para cadastro de professores, alunos e controle de atividades.

---

## 🧩 Descrição da API

Esta API foi desenvolvida com o objetivo de facilitar o gerenciamento de atividades educacionais. Ela permite:

- Cadastro e gerenciamento de professores e alunos  
- Registro e acompanhamento de atividades  
- Integração com um banco de dados SQLite para persistência dos dados  

---

## 🚀 Instruções de Execução com Docker

Para executar o projeto utilizando Docker, siga os passos abaixo:

1. **Clone o repositório**
   ```bash
   git clone https://github.com/taltsolyu/Atividades.git
   cd Atividades

Copie o arquivo app.db para o diretório raiz do projeto

Certifique-se de que o arquivo app.db está localizado na raiz do projeto. Este arquivo já contém:

Todas as estruturas de tabelas criadas

Um professor com ID 1 cadastrado para testes

⚠️ Sem esse arquivo, o projeto pode gerar erros de integridade referencial ou falha ao acessar dados.

Construa a imagem Docker

docker build -t atividades-api .
Execute o container

docker run -d -p 5001:5001 --name atividades-container atividades-api
Acesse a API

A API estará disponível em: http://localhost:5001

🏗️ Arquitetura Utilizada
A aplicação segue uma arquitetura baseada em microsserviços, promovendo modularidade e escalabilidade. Os principais componentes incluem:

Flask: Framework web utilizado para criar a API RESTful.

SQLite: Banco de dados leve utilizado para persistência dos dados.

Docker: Utilizado para containerizar a aplicação, facilitando a implantação e escalabilidade.

Estrutura do Projeto

app.py            # Ponto de entrada da aplicação
controllers/      # Define as rotas e lógica de negócio
models/           # Modelos de dados da aplicação
clients/          # Interações com serviços externos (se houver)
config.py         # Configurações da aplicação
requirements.txt  # Dependências do projeto
dockerfile        # Instruções para construção da imagem Docker
🔗 Ecossistema de Microsserviços e Integração
Embora este projeto seja uma aplicação monolítica, ele foi estruturado com princípios que facilitam a transição para uma arquitetura de microsserviços. Em uma arquitetura de microsserviços:

Características dos Microsserviços
Independência: Cada serviço pode ser desenvolvido, implantado e escalado independentemente.

Especialização: Serviços são responsáveis por funcionalidades específicas, promovendo coesão.

Comunicação via APIs: Serviços interagem entre si utilizando protocolos leves, como HTTP/REST.

Integração entre Serviços
Em um ecossistema de microsserviços, a integração entre serviços pode ser gerenciada por uma malha de serviços (service mesh), que oferece:

Descoberta de Serviços: Facilita a localização de serviços dentro do ecossistema.

Balanceamento de Carga: Distribui o tráfego de forma eficiente entre as instâncias de serviço.

Segurança: Implementa autenticação, autorização e criptografia nas comunicações.

Observabilidade: Fornece métricas, logs e rastreamento distribuído para monitoramento dos serviços.


