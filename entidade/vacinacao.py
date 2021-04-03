from entidade.enfermeiro import Enfermeiro
from entidade.paciente import Paciente
from excecao import NaoCadastrado

class Vacinacao:
    def __init__(self, id, paciente: Paciente, enfermeiro: Enfermeiro, numero_dose, tipo_dose):
        if isinstance(paciente, Paciente):
            self.__paciente = paciente
        else:
            raise NaoCadastrado()
        if isinstance(enfermeiro, Enfermeiro):
            self.__enfermeiro = enfermeiro
        else:
            raise NaoCadastrado()
        #teste de id
        self.__id = id
        if self.__numero_dose == "1" or "2":
            self.__numero_dose = numero_dose
        """else: 
            return "O número da dose precisa ser igual a 1 ou 2."""
        if isinstance(tipo_dose, str):
            self.__tipo_dose = tipo_dose
        else:
            return "Tipo da dose deve ser string"


    @property
    def paciente(self):
        return self.__paciente

    @property
    def enfermeiro(self):
        return self.__enfermeiro

    @property
    def numero_dose(self):
        return self.__numero_dose

    @property
    def tipo_dose(self):
        return self.__tipo_dose

    @property
    def vacinacoes(self):
        return self.__vacinacoes

    @property
    def id(self):
        return self.__id
