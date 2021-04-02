class NomeComCaracterNumerico(Exception):
    def __init__(self):
        super().__init__("Nome deve conter apenas letras")