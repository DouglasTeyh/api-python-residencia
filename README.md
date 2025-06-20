# 📄 Documentação - API com Python (Flask) - Residencia (ATIVIDADE)

## 🗂️ Organização:
```bash
api_flask/
│
├── app/
│   ├── __init__.py
    ├── controllers.py
    ├── data.py
    ├── models.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## Descrição dos Arquivos:
| Arquivo/Pasta        | Função                                                                            |
| -------------------- | --------------------------------------------------------------------------------- |
| `run.py`             | Ponto de entrada da aplicação Flask.                                              |
| `app/__init__.py`    | Cria e configura a instância do Flask App.                                        |
| `app/controllers.py` | Contém as funções responsáveis pelas operações feitas do CRUD.                    |
| `app/data.py`        | Simula um banco de dados em memória pra listar os usuarios.                       |
| `app/models.py`	   | Define o modelo de dados, como a classe Usuario.                                  |
| `requirements.txt`   | Lista os pacotes Python necessários                                               |
| `README.md`          | Descrição do projeto, como rodar e como usar.                                     |
| `.gitignore`         | Contem os Arquivos que não devem ir para o Repositório Remoto                     |