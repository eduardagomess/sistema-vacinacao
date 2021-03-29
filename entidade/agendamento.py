class Agendamento:

    def __init__(self):
        self.__agedamentos = {}
        self.__agenda = []

    @property
    def agendamentos(self):
        return self.__agedamentos

    @property
    def agenda(self):
        return self.__agenda