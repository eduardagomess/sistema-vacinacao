class CorenInvalido(Exception):
    def __init__(self):
        super().__init__("Valor incorreto, o COREN deve conter apenas 6 digitos")