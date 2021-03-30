class Agendamento:

    def __init__(self, paciente, enfermeiro):
        self.__agedamentos = {}
        self.__agenda = []
        self.__paciente = paciente
        self.__enfermeiro = enfermeiro

    @property
    def agendamentos(self):
        return self.__agedamentos

    @property
    def agenda(self):
        return self.__agenda