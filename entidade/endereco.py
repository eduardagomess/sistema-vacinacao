class Endereco:
    def __init__(self, bairro: str, rua: str, numero: str, complemento: str):
        self.__bairro = bairro
        self.__rua = rua
        self.__numero = numero
        self.__complemento = complemento

    def mostrar_endereco(self):
        return f"{self.__bairro}, {self.__rua}, {self.__numero}, {self.__complemento}"
