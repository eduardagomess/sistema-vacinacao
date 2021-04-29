class TipoVacina():
    def __init__(self, nome: str, num_doses: int):
        self.__nome = nome
        self.__num_doses = num_doses

    @property
    def nome(self):
        return self.__nome

    @property
    def num_doses(self):
        return self.__num_doses
