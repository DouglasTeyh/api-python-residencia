import random

ids_existentes = set()

class Usuario:
    def __init__(self, id: int, nome: str, email: str):
        self.id = gerar_id()
        self.nome = nome
        self.email = email

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }
    
def gerar_id() -> int:
    while True:
        novo_id = random.randint(100_000, 999_999_999)
        if novo_id not in ids_existentes:
            ids_existentes.add(novo_id)
            return novo_id