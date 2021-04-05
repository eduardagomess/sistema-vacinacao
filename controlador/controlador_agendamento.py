from tela.tela_agendamento import TelaAgendamento
from tela.tela_relatorio import TelaRelatorio
from entidade.agendamento import Agendamento
from utils import estilo
import time


class ControladorAgendamento:

    def __init__(self, controlador_sistema):
        self.__tela_agendamento = TelaAgendamento(self)
        self.__tela_relatorio = TelaRelatorio(self)
        self.__controlador_sistema = controlador_sistema
        self.__agendamento = Agendamento()

    def inserir_agendamento(self):
        estilo.clear()
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        controlador_enfermeiro = self.__controlador_sistema.controlador_enfermeiro
        paciente = controlador_paciente.tipo_de_busca_paciente()
        if paciente == None:
            opcao = self.__tela_agendamento.pega_opcao_paciente_sem_cadastro()
            if opcao == 1:
                paciente = controlador_paciente.inserir_paciente()
            else:
                self.retornar_sistema()
        dia, hora = self.__tela_agendamento.pegar_dados_agendamento(self.__agendamento.agenda)
        dia = dia.lower().capitalize()
        enfermeiro_escolhido = controlador_enfermeiro.busca_enfermeiro()
        if enfermeiro_escolhido == None:
            estilo.clear()
            self.__tela_agendamento.mostra_msg_enfermeiro_nao_castrado()
            time.sleep(1.5)
            estilo.clear()
            enfermeiro_escolhido = controlador_enfermeiro.inserir_enfermeiro()
        if hora not in self.__agendamento.agenda[dia]:
            self.__agendamento.agenda[dia].append(hora)
            self.__agendamento.agendamentos[paciente.nome] = {"paciente": paciente, "agendamento": [dia, hora], "enfermeiro": enfermeiro_escolhido}
        estilo.clear()

    def buscar_agendamento(self):
        estilo.clear()
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        paciente = controlador_paciente.tipo_de_busca_paciente()
        if paciente == None:
            opcao = self.__tela_agendamento.pega_opcao_paciente_sem_cadastro()
            if opcao == 1:
                controlador_paciente.inserir_paciente()
            else:
                self.retornar_sistema()
        else:
            if paciente.nome not in self.__agendamento.agendamentos:
                self.__tela_agendamento.mostra_msg_sem_agendamento(paciente)
                estilo.clear()
            else:
                return self.__agendamento.agendamentos[paciente.nome]

    def editar_agendamento(self):
        estilo.clear()
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        controlador_enfermeiro = self.__controlador_sistema.controlador_enfermeiro
        paciente = controlador_paciente.tipo_de_busca_paciente()
        if paciente == None:
            opcao = self.__tela_agendamento.pega_opcao_paciente_sem_cadastro()
            if opcao == 1:
                controlador_paciente.inserir_paciente()
            else:
                self.retornar_sistema()
        else:
            if paciente.nome not in self.__agendamento.agendamentos:
                self.__tela_agendamento.mostra_msg_sem_agendamento(paciente)
                estilo.clear()
            else:
                tipo_de_alteracao = self.__tela_agendamento.mostra_opcao_alteracao()
                dado_novo = self.__tela_agendamento.pega_novos_dados(tipo_de_alteracao, self.__agendamento.agendamentos, paciente, self.__agendamento.agenda)
                hora = self.__agendamento.agendamentos[paciente.nome]["agendamento"][1]
                dia = self.__agendamento.agendamentos[paciente.nome]["agendamento"][0].lower().capitalize()
                self.__agendamento.agenda[dia].remove(hora)

                if dado_novo[0] == "dia":
                    dia_novo = dado_novo[1].lower().capitalize()
                    self.__agendamento.agenda[dia_novo].append(hora)
                    self.__agendamento.agendamentos[paciente.nome]["agendamento"][0] = dia_novo

                elif dado_novo[0] == "hora":
                    if dado_novo[1] not in self.__agendamento.agenda[dia]:
                        self.__agendamento.agenda[dia].append(dado_novo[1])
                    self.__agendamento.agendamentos[paciente.nome]["agendamento"][1] = dado_novo[1]

                elif dado_novo[0] == "dia e hora":
                    dia_novo = dado_novo[1][0].lower().capitalize()
                    self.__agendamento.agenda[dia_novo].append(hora)
                    self.__agendamento.agendamentos[paciente.nome]["agendamento"][0] = dia_novo
                    if dado_novo[1][1] not in self.__agendamento.agenda[dia]:
                        self.__agendamento.agenda[dia].append(dado_novo[1][1])
                    self.__agendamento.agendamentos[paciente.nome]["agendamento"][1] = dado_novo[1][1]

                else:
                    enfermeiro = controlador_enfermeiro.busca_enfermeiro()
                    if enfermeiro == None:
                        enfermeiro = controlador_enfermeiro.inserir_enfermeiro()
                    self.__agendamento.agendamentos[paciente.nome]["enfermeiro"] = enfermeiro

    def excluir_agendamento(self):
        estilo.clear()
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        paciente = controlador_paciente.tipo_de_busca_paciente()
        if paciente == None:
            opcao = self.__tela_agendamento.pega_opcao_paciente_sem_cadastro()
            if opcao == 1:
                controlador_paciente.inserir_paciente()
            else:
                self.retornar_sistema()
                estilo.clear()
        else:
            if paciente.nome not in self.__agendamento.agendamentos:
                self.__tela_agendamento.mostra_msg_sem_agendamento(paciente)
                estilo.clear()
            else:
                print(self.__agendamento.agendamentos)
                dia, hora = [str(w) for w in self.__agendamento.agendamentos[paciente.nome]["agendamento"]]
                self.__agendamento.agenda[dia.lower().capitalize()].remove(hora)
                del self.__agendamento.agendamentos[paciente.nome]
                self.__tela_agendamento.mostra_mensagem_agendamento_exlcuido()
                estilo.clear()

    def listar_agendamentos(self):
        estilo.clear()
        if self.__agendamento.agendamentos == {}:
            self.__tela_agendamento.mostra_msg_sem_agendamento()
        else:
            self.__tela_agendamento.mostra_dados(self.__agendamento.agendamentos)
        estilo.clear()

    def retornar_sistema(self):
        return self.__controlador_sistema

    def gera_relatorio(self):
        estilo.clear()
        if self.__agendamento.agendamentos == {}:
            self.__tela_agendamento.mostra_msg_sem_agendamento()
        else:
            self.__tela_relatorio.mostra_relatorio(self.__agendamento.agendamentos)
        estilo.clear()

    def abre_tela(self):
        estilo.clear()
        opcoes = {1: self.inserir_agendamento, 2: self.editar_agendamento, 3: self.excluir_agendamento,
                  4: self.listar_agendamentos, 5: self.gera_relatorio, 6: self.buscar_agendamento, 7: self.retornar_sistema}
        continua = True
        while continua:
            opcao_selecionada = self.__tela_agendamento.mostra_opcoes()
            if opcao_selecionada == 7:
                continua = False
            opcoes[opcao_selecionada]()
