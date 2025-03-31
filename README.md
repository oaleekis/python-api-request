# 📌 Python API Request

Este projeto realiza requisições a uma API de exemplo, armazena os dados em um banco de dados MySQL e fornece um procedimento armazenado para buscar usuários por e-mail.

## 🚀 Tecnologias Utilizadas

- Python 3
- MySQL
- Requests (para requisições HTTP)
- Python Dotenv (para variáveis de ambiente)

## 📂 Estrutura do Projeto
```
meu_projeto/
│── src/                      # Código-fonte principal
│   ├── __init__.py           # Indica que src é um pacote Python
│   ├── main.py               # Arquivo principal
│   ├── db.py                 # Conexão com o banco de dados
│   ├── services/             # Lógica do projeto
│   │   ├── fetch_users.py     # Código para buscar e inserir usuários
│   │   ├── create_tables.py   # Código para criar tabelas
│── .env                      # Configurações sensíveis (não deve ser versionado)
│── .env.example              # Exemplo do .env sem valores reais
│── .gitignore                # Arquivos a serem ignorados pelo Git
│── requirements.txt          # Dependências do projeto
│── README.md                 # Documentação
```

## 🔧 Como Configurar e Rodar o Projeto

### 1️⃣ Instale as Dependências
```sh
pip install -r requirements.txt
```

### 2️⃣ Configure o Banco de Dados
Antes de rodar o projeto, crie um banco de dados MySQL e um usuário com as permissões adequadas.

Crie um arquivo **`.env`** na raiz do projeto com o seguinte conteúdo:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=
```

> **Atenção:** O arquivo `.env` **não** deve ser versionado. Use `.env.example` como referência.

### 3️⃣ Execute o Projeto
```sh
python src/main.py
```
Isso criará as tabelas e inserirá os dados no banco de dados.

## 🛠 Funcionalidades

✅ Criar tabelas no banco de dados.
✅ Inserir dados de usuários a partir da API JSONPlaceholder.
✅ Criar um procedimento armazenado para buscar usuários por e-mail.
