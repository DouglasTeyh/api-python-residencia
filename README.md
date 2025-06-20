````markdown
# 📄 Documentação - API com Python (Flask) - Residencia (ATIVIDADE)

## 🗂️ Organização:
```bash
api_python-residencia/
│
├── app/
│   ├── __init__.py
│   ├── controllers.py
│   ├── data.py
│   ├── models.py
│   ├── routes.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
````

## Descrição dos Arquivos:

| Arquivo/Pasta        | Função                                                         |
| -------------------- | -------------------------------------------------------------- |
| `run.py`             | Ponto de entrada da aplicação Flask.                           |
| `app/__init__.py`    | Cria e configura a instância do Flask App.                     |
| `app/controllers.py` | Contém as funções responsáveis pelas operações feitas do CRUD. |
| `app/data.py`        | Simula um banco de dados em memória pra listar os usuarios.    |
| `app/models.py`      | Define o modelo de dados, como a classe Usuario.               |
| `app/routes.py`      | Define as rotas da API (endpoints)                             |
| `requirements.txt`   | Lista os pacotes Python necessários                            |
| `README.md`          | Descrição do projeto, como rodar e como usar.                  |
| `.gitignore`         | Contem os Arquivos que não devem ir para o Repositório Remoto  |

## 🌐 Endpoints para Equipe de Front-end:

| Método | Endpoint        | Descrição                    |
| ------ | --------------- | ---------------------------- |
| GET    | `/saudacao`     | Mensagem de boas-vindas      |
| POST   | `/usuarios`     | Cadastrar novo usuário       |
| GET    | `/usuarios`     | Listar todos os usuários     |
| PUT    | `/usuarios/:id` | Atualizar um usuário pelo ID |
| DELETE | `/usuarios/:id` | Deletar um usuário pelo ID   |

## 🚀 URL da API:

* Local: `http://localhost:5000`
* Remoto: `https://api-python-residencia.onrender.com/`

## 📦 Detalhes dos Endpoints:

### 🔸 GET `/saudacao`

Retorna uma mensagem de boas-vindas.

**Exemplo de resposta:**

```json
{
  "mensagem": "Bem-vindo à API de exemplo"
}
```

---

### 🔸 POST `/usuarios`

Cadastra um novo usuário.

**Body (JSON):**

```json
{
  "nome": "João Silva",
  "email": "joao@email.com"
}
```

**Exemplo de resposta:**

```json
{
  "id": 1,
  "nome": "João Silva",
  "email": "joao@email.com"
}
```

---

### 🔸 GET `/usuarios`

Lista todos os usuários cadastrados.

**Exemplo de resposta:**

```json
[
  {
    "id": 1,
    "nome": "João Silva",
    "email": "joao@email.com"
  },
  {
    "id": 2,
    "nome": "Maria Souza",
    "email": "maria@email.com"
  }
]
```

---

### 🔸 PUT `/usuarios/:id`

Atualiza um usuário existente.

**Body (JSON):**

```json
{
  "nome": "João Atualizado",
  "email": "joao.novo@email.com"
}
```

**Resposta (sucesso):**

```json
{
  "id": 1,
  "nome": "João Atualizado",
  "email": "joao.novo@email.com"
}
```

**Resposta (erro):**

```json
{
  "erro": "Usuário não encontrado"
}
```

---

### 🔸 DELETE `/usuarios/:id`

Deleta um usuário pelo ID.

**Exemplo de resposta:**

```json
{
  "mensagem": "Usuário deletado com sucesso"
}
```

## ⚠️ Observações Importantes:

* Os dados são armazenados em memória, então são resetados quando o servidor reinicia.
* A API aceita requisições de qualquer origem (CORS habilitado).
* Todos os dados devem ser enviados em formato JSON.
* Funciona localmente na porta `5000` e também na URL pública do Render.

```
```
