import random

ids_existentes = set()

def gerar_id() -> int:
    while True:
        novo_id = random.randint(100_000, 999_999_999)
        if novo_id not in ids_existentes:
            ids_existentes.add(novo_id)
            return novo_id

class Usuario:
    def __init__(self, id: int = None, nome: str = "", email: str = ""):
        if id is None:
            self.id = gerar_id()
        else:
            self.id = id
            ids_existentes.add(id)
        self.nome = nome
        self.email = email

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }
