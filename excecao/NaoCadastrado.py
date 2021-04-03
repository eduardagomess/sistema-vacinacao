class NaoCadastrado(Exception):
    def __init__(self):
        super().__init__("Tentou usar um objeto não cadastrado")
