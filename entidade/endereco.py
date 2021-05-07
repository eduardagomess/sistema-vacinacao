class Endereco:
    def __init__(self, bairro: str, rua: str, numero: int, complemento: str):
        self.__bairro = bairro
        self.__rua = rua
        self.__numero = numero
        self.__complemento = complemento

    @property
    def bairro(self):
        retunr self.__bairro
    
    @property
    def rua(self):
        retunr self.__rua

    @property
    def numero (self):
        retunr self.__numero

    @property
    def complemento(self):
        retunr self.__complemento
    



    def mostrar_endereco(self):
        return f"{self.__bairro}, {self.__rua}, {self.__numero}, {self.__complemento}"
