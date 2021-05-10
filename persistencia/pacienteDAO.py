from persistencia.DAO import DAO
from entidade.paciente import Paciente


class PacienteDAO(DAO):
    def __init__(self):
        super().__init__('paciente.pkl')

    def add(self, paciente: Paciente):
        if (paciente is not None) and (isinstance(paciente, Paciente)) and (isinstance(paciente.cpf, str)):
            super().add(paciente.cpf, paciente)

    def remove(self, paciente: Paciente):
        if (paciente is not None) and (isinstance(paciente, Paciente)) and  (isinstance(paciente.cpf, str)):
            super().remove(paciente.cpf)