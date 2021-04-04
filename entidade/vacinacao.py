from entidade.enfermeiro import Enfermeiro
from entidade.paciente import Paciente

class Vacinacao:
    def __init__(self, id, paciente: Paciente, enfermeiro: Enfermeiro, dose, tipo_dose):
        self.__id = id
        self.__paciente = paciente
        self.__enfermeiro = enfermeiro
        self.__dose = dose
        self.__tipo_dose = tipo_dose

    @property
    def paciente(self):
        return self.__paciente

    @property
    def enfermeiro(self):
        return self.__enfermeiro

    @property
    def dose(self):
        return self.__dose

    @property
    def tipo_dose(self):
        return self.__tipo_dose

    @property
    def id(self):
        return self.__id
