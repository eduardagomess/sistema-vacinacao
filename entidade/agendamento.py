class Agendamento:

    def __init__(self):
        self.__agenda = {"Segunda": [], "Terca": [], "Quarta": [],
                         "Quinta": [], "Sexta": []}
        self.__agendamentos = {}
        self.__lista_pacientes = []
        self.__lista_enfermeiro = []

    @property
    def agendamentos(self):
        return self.__agendamentos

    @property
    def agenda(self):
        return self.__agenda
