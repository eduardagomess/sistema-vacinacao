from tela.telaAgendamento import TelaAgendamento
from utils import estilo
import time

class ControladorAgendamento:

    def __init__(self, controlador_sistema):
        self.__agenda = {"Segunda": [], "Terca": [], "Quarta": [],"Quinta": [], "Sexta": []}
        self.__agendamentos = {}
        self.__tela_agendamento = TelaAgendamento()
        self.__controlador_sistema = controlador_sistema
        self.__lista_pacientes = []
        self.__lista_enfermeiro = []


    def inserir_agendamento(self):
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        controlador_enfermeiro = self.__controlador_sistema.controlador_enfermeiro
        paciente = controlador_paciente.busca_paciente()
        if paciente == None:
            estilo.clear()
            self.__tela_agendamento.mostra_msg_paciente_nao_castrado()
            time.sleep(1.5)
            estilo.clear()
            paciente = controlador_paciente.inserir_paciente()
        dia, hora = self.__tela_agendamento.pegar_dados_agendamento()
        dia = dia.lower().capitalize()
        enfermeiro_escolhido = controlador_enfermeiro.busca_enfermeiro()
        if enfermeiro_escolhido == None:
            estilo.clear()
            self.__tela_agendamento.mostra_msg_enfermeiro_nao_castrado()
            time.sleep(1.5)
            estilo.clear()
            enfermeiro_escolhido = controlador_enfermeiro.inserir_enfermeiro()
        if hora not in self.__agenda[dia]:
            self.__agenda[dia].append(hora)
            self.__agendamentos[paciente.nome] = {"paciente": paciente, "agendamento": [dia, hora], "enfermeiro": enfermeiro_escolhido}

    def editar_agendamento(self):
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        controlador_enfermeiro = self.__controlador_sistema.controlador_enfermeiro
        paciente = controlador_paciente.busca_paciente()
        enfermeiro = controlador_enfermeiro.busca_enfermeiro()
        tipo_de_alteracao = self.__tela_agendamento.mostra_opcao_alteracao()
        dado_novo = self.__tela_agendamento.pega_novos_dados(tipo_de_alteracao)

        if dado_novo[0] == "dia":
            pass
        elif dado_novo[0] == "hora":
            pass
        elif dado_novo[0] == "enfermeiro":
            pass
        pass

    def excluir_agendamento(self):
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        paciente = controlador_paciente.busca_paciente()
        print(paciente)
        print(self.__agendamentos[paciente.nome])
        dia, hora = [str(w) for w in self.__agendamentos[paciente.nome]["agendamento"]]
        self.__agenda[dia.lower().capitalize()].remove(hora)
        del self.__agendamentos[paciente.nome]

    def listar_agendamentos(self):
        estilo.clear()
        for agendamento in self.__agendamentos:
            self.__tela_agendamento.mostra_dados({"paciente": self.__agendamentos[agendamento]["paciente"].nome, "agendamento": self.__agendamentos[agendamento]["agendamento"],
                                                       "enfermeiro": self.__agendamentos[agendamento]["enfermeiro"].nome})


    def retornar_sistema(self):
        return self.__controlador_sistema


    def abre_tela(self):
        estilo.clear()
        opcoes = {1: self.inserir_agendamento, 2: self.editar_agendamento, 3: self.excluir_agendamento, 4: self.listar_agendamentos, 5: self.retornar_sistema}
        continua = True
        while continua:
            opcao_selecionada = self.__tela_agendamento.mostra_opcoes()
            if opcao_selecionada == 5:
                continua = False
            opcoes[opcao_selecionada]()


