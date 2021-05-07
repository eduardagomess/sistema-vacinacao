class Endereco:
    def __init__(self, bairro: str, rua: str, numero: int, complemento: str):
        self.__bairro = bairro
        self.__rua = rua
        self.__numero = numero
        self.__complemento = complemento

    @property
    def bairro(self):
        return self.__bairro
    
    @property
    def rua(self):
        return self.__rua

    @property
    def numero (self):
        return self.__numero

    @property
    def complemento(self):
        return self.__complemento

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro
    
    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @complemento.setter
    def complemento(self, complemento):
        self.__complemento = complemento
    
    def mostrar_endereco(self):
        return f"{self.__bairro.title()}, {self.__rua.title()}, {self.__numero}, {self.__complemento.title()}"
