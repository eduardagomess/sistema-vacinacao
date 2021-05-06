from tela.tela_sistema import TelaSistema
from controlador.controlador_estoque import ControladorEstoque
from controlador.controlador_vacinacao import ControladorVacinacao
from controlador.controlador_agendamento import ControladorAgendamento
from controlador.controlador_paciente import ControladorPaciente
from controlador.controlador_enfermeiro import ControladorEnfermeiro
from controlador.controlador_tipo_vacina import ControladorTipoVacina


class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema(self)
        self.__controlador_vacinacao = ControladorVacinacao(self)
        self.__controlador_estoque = ControladorEstoque(self)
        self.__controlador_agendamento = ControladorAgendamento(self)
        self.__controlador_paciente = ControladorPaciente(self)
        self.__controlador_enfermeiro = ControladorEnfermeiro(self)
        self.__controlador_tipo_vacina = ControladorTipoVacina(self)

    def inicializa_sistema(self):
        self.abre_tela()

    def acessar_area_paciente(self):
        self.__controlador_paciente.abre_tela()

    def acessar_area_enfermeiro(self):
        self.__controlador_enfermeiro.abre_tela()

    def acessar_estoque(self):
        self.__controlador_estoque.abre_tela()

    def acessar_registro_vacinacao(self):
        self.__controlador_vacinacao.abre_tela()

    def acessar_agendamentos(self):
        self.__controlador_agendamento.abre_tela()

    def acessar_tipo_vacina(self):
        self.__controlador_tipo_vacina.abre_tela()

    @staticmethod
    def finaliza_sistema():
        exit(0)

    @property
    def controlador_estoque(self):
        return self.__controlador_estoque

    @property
    def controlador_vacinacao(self):
        return self.__controlador_vacinacao

    @property
    def controlador_agendamento(self):
        return self.__controlador_agendamento

    @property
    def controlador_paciente(self):
        return self.__controlador_paciente

    @property
    def controlador_enfermeiro(self):
        return self.__controlador_enfermeiro

    @property
    def controlador_tipo_vacina(self):
        return self.__controlador_tipo_vacina

    @property
    def tela_sistema(self):
        return self.__tela_sistema

    def abre_tela(self):
        opcoes = {1: self.acessar_area_paciente, 2: self.acessar_area_enfermeiro,
                  3: self.acessar_estoque, 4: self.acessar_registro_vacinacao,
                  5: self.acessar_agendamentos, 6: self.acessar_tipo_vacina}
        while True:
            button, values = self.__tela_sistema.open()
            if button == "Sair" or button is None:
                self.__tela_sistema.close()
            else:
                count = 1
                for i in values.values():
                    if i:
                        opcoes[count]()
                    count += 1
