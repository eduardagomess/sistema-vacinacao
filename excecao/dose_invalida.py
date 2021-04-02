class DoseInvalida(Exception):
    def __init__(self):
        super().__init__("Valor incorreto, o estágio da dose deve ser um valor inteiro entre 0,1 e 2")