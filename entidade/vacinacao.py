from entidade.enfermeiro import Enfermeiro
from entidade.paciente import Paciente

class Vacinacao:
    def __init__(self, paciente: Paciente, enfermeiro: Enfermeiro, tipo_dose):
        self.__paciente = paciente
        self.__enfermeiro = enfermeiro
        self.__tipo_dose = tipo_dose

    @property
    def paciente(self):
        return self.__paciente

    def pega_dose(self):
        return self.__paciente.dose

    @property
    def enfermeiro(self):
        return self.__enfermeiro

    @property
    def tipo_dose(self):
        return self.__tipo_dose
