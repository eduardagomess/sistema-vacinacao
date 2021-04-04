from excecao import erro_de_tipo


class Estoque:
    def __init__(self, tipo: str, quantidade: int):
        if isinstance(tipo, str):
            self.__tipo = tipo
        else:
            raise erro_de_tipo
        if isinstance(quantidade, int):
            self.__quantidade = quantidade
        else:
            raise erro_de_tipo
        self.__vacinas_aplicadas = []
        self.__vacinas_total = []

    @property
    def tipo(self):
        return self.__tipo

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def vacinas_aplicadas(self):
        return self.__vacinas_aplicadas

    @tipo.setter
    def tipo(self, tipo):
        if isinstance(tipo, str):
            self.__tipo = tipo
        else:
            raise erro_de_tipo

    @quantidade.setter
    def quantidade(self, quantidade):
        if isinstance(quantidade, int):
            self.__quantidade = quantidade
        else:
            raise erro_de_tipo

    @vacinas_aplicadas.setter
    def vacinas_aplicadas(self, vacinas_aplicadas):
        if isinstance(vacinas_aplicadas, int):
            self.__vacinas_aplicadas = vacinas_aplicadas
        else:
            raise erro_de_tipo
