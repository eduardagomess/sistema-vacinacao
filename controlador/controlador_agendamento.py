from tela.tela_agendamento import TelaAgendamento
from tela.tela_relatorio import TelaRelatorio
from utils import estilo
import time


class ControladorAgendamento:

    def __init__(self, controlador_sistema):
        self.__agenda = {"Segunda": [], "Terca": [], "Quarta": [],"Quinta": [], "Sexta": []}
        self.__agendamentos = {}
        self.__tela_agendamento = TelaAgendamento(self)
        self.__tela_relatorio = TelaRelatorio(self)
        self.__controlador_sistema = controlador_sistema
        self.__lista_pacientes = []
        self.__lista_enfermeiro = []

    def inserir_agendamento(self):
        estilo.clear()
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        controlador_enfermeiro = self.__controlador_sistema.controlador_enfermeiro
        paciente = controlador_paciente.tipo_de_busca_paciente()
        if paciente == None:
            estilo.clear()
            self.__tela_agendamento.mostra_msg_paciente_nao_castrado()
            time.sleep(1.5)
            estilo.clear()
            paciente = controlador_paciente.inserir_paciente()
        dia, hora = self.__tela_agendamento.pegar_dados_agendamento(self.__agenda)
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

    def buscar_agendamento(self):
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        paciente = controlador_paciente.tipo_de_busca_paciente()
        return self.__agendamentos[paciente.nome]

    def editar_agendamento(self):
        estilo.clear()
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        controlador_enfermeiro = self.__controlador_sistema.controlador_enfermeiro
        paciente = controlador_paciente.tipo_de_busca_paciente()
        tipo_de_alteracao = self.__tela_agendamento.mostra_opcao_alteracao()
        dado_novo = self.__tela_agendamento.pega_novos_dados(tipo_de_alteracao, self.__agendamentos, paciente, self.__agenda)
        hora = self.__agendamentos[paciente.nome]["agendamento"][1]
        dia = self.__agendamentos[paciente.nome]["agendamento"][0].lower().capitalize()
        self.__agenda[dia].remove(hora)

        if dado_novo[0] == "dia":
            dia_novo = dado_novo[1].lower().capitalize()
            self.__agenda[dia_novo].append(hora)
            self.__agendamentos[paciente.nome]["agendamento"][0] = dia_novo

        elif dado_novo[0] == "hora":
            if dado_novo[1] not in self.__agenda[dia]:
                self.__agenda[dia].append(dado_novo[1])
            self.__agendamentos[paciente.nome]["agendamento"][1] = dado_novo[1]

        elif dado_novo[0] == "dia e hora":
            dia_novo = dado_novo[1][0].lower().capitalize()
            self.__agenda[dia_novo].append(hora)
            self.__agendamentos[paciente.nome]["agendamento"][0] = dia_novo
            if dado_novo[1][1] not in self.__agenda[dia]:
                self.__agenda[dia].append(dado_novo[1][1])
            self.__agendamentos[paciente.nome]["agendamento"][1] = dado_novo[1][1]

        else:
            enfermeiro = controlador_enfermeiro.busca_enfermeiro()
            if enfermeiro == None:
                enfermeiro = controlador_enfermeiro.inserir_enfermeiro()
            self.__agendamentos[paciente.nome]["enfermeiro"] = enfermeiro


    def excluir_agendamento(self):
        estilo.clear()
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        paciente = controlador_paciente.tipo_de_busca_paciente()
        dia, hora = [str(w) for w in self.__agendamentos[paciente.nome]["agendamento"]]
        self.__agenda[dia.lower().capitalize()].remove(hora)
        del self.__agendamentos[paciente.nome]

    def listar_agendamentos(self):
        self.__tela_agendamento.mostra_dados(self.__agendamentos)

    def retornar_sistema(self):
        return self.__controlador_sistema

    def gera_relatorio(self):
        self.__tela_relatorio.mostra_relatorio(self.__agendamentos)

    def abre_tela(self):
        estilo.clear()
        opcoes = {1: self.inserir_agendamento, 2: self.editar_agendamento, 3: self.excluir_agendamento, 4: self.listar_agendamentos, 5: self.gera_relatorio,
                  6: self.retornar_sistema}
        continua = True
        while continua:
            opcao_selecionada = self.__tela_agendamento.mostra_opcoes()
            if opcao_selecionada == 6:
                continua = False
            opcoes[opcao_selecionada]()


