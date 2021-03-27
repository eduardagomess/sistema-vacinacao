from tela.telaSistema import TelaSistema
import os
from controlador.controladorEstoque import ControladorEstoque
from controlador.controladorVacinacao import ControladorVacinacao
from controlador.controladorAgendamento import ControladorAgendamento
from controlador.controladorPaciente import ControladorPaciente
from controlador.controladorEnfermeiro import ControladorEnfermeiro
from utils import estilo
import os



class ControladorSistema:
    def __init__(self):
        self.__controlador_estoque = ControladorEstoque(self)
        self.__controlador_vacinacao = ControladorVacinacao(self)
        self.__controlador_agendamento = ControladorAgendamento(self)
        self.__controlador_paciente = ControladorPaciente(self)
        self.__controlador_enfermeiro = ControladorEnfermeiro(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def acessar_cadastro_enfermeiro(self):
        self.__controlador_enfermeiro.abre_tela()

    def acessar_cadastro_paciente(self):
        self.__controlador_paciente.abre_tela()

    def acessar_estoque(self):
        self.__controlador_estoque.abre_tela()

    def acessar_registro_vacinacao(self):
        self.__controlador_vacinacao.abre_tela()

    def acessar_agendamentos(self):
        self.__controlador_agendamento.abre_tela()

    def finaliza_sistema(self):
        exit(0)


    def abre_tela(self):
        opcoes = {1: self.acessar_cadastro_paciente, 2: self.acessar_cadastro_enfermeiro, 3: self.acessar_estoque, 4: self.acessar_registro_vacinacao,
                  5: self.acessar_agendamentos, 6: self.finaliza_sistema}
        while True:
            estilo.clear()
            opcoes[self.__tela_sistema.mostra_opcoes()]()


