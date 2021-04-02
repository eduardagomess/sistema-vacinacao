class NomeInvalido(Exception):
    def __init__(self):
        super().__init__("Nome deve conter mais de 5 caracteres")