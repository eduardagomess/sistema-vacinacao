class CpfInvalido(Exception):
    def __init__(self):
        super().__init__("Valor incorreto, o CPF deve conter apenas 11 digitos")