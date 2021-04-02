class TelefoneComNumeroInvalido(Exception):
    def __init__(self):
        super().__init__("Numero de telefone deve conter de 10 a 11 digitos")