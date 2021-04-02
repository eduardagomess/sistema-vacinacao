class CaracterAlfabeticoExcecao(Exception):
    def __init__(self):
        super().__init__("Telefone deve conter apenas numeros")