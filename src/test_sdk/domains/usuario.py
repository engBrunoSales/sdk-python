from src.test_sdk.domains.domain import Domain


class Usuario(Domain):
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome