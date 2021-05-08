from tela.tela_relatorio import TelaRelatorio
from tela.tela_agendamento.tela_agendamentoo import TelaAgendamento
from tela.tela_agendamento.tela_inserir_agendamento_dia import TelaInserirDia
from tela.tela_agendamento.tela_inserir_agendamento_hora import TelaInserirHora
from tela.tela_agendamento.tela_mudanca_agendamento import TelaMudancaAgendamento
from tela.tela_paciente.tela_listagem import TelaListagem
from entidade.agendamento import Agendamento
from utils import estilo
import PySimpleGUI as sg
import time


class ControladorAgendamento:

    def __init__(self, controlador_sistema):
        self.__tela_agendamento = TelaAgendamento(self)
        self.__tela_relatorio = TelaRelatorio(self)
        self.__tela_inserir_dia = TelaInserirDia(self)
        self.__tela_inserir_hora = TelaInserirHora(self)
        self.__tela_listagem = TelaListagem(self)
        self.__tela_mudanca_agendamento = TelaMudancaAgendamento(self)
        self.__controlador_sistema = controlador_sistema
        self.__agendamento = Agendamento()

    def inserir_agendamento(self):
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        controlador_enfermeiro = self.__controlador_sistema.controlador_enfermeiro
        paciente = controlador_paciente.buscar_paciente()
        if paciente == None:
            sg.popup("Erro", "Paciente não cadastrado!")
            paciente = controlador_paciente.inserir_paciente(None, None, None, None, None, None, None, None)
            enfermeiro= controlador_enfermeiro.buscar_enfermeiro()
            if enfermeiro == None:
                sg.popup("Erro", "Enfermeiro não cadastrado!")
                enfermeiro_escolhido = controlador_enfermeiro.inserir_enfermeiro(None, None, None, None)
                button, value_dia = self.__tela_inserir_dia.open()
                self.__tela_inserir_dia.close()
                dia = value_dia["dia_da_semana"].lower().capitalize()
                self.__tela_inserir_hora.init_components(self.__agendamento.agenda[dia])
                button, value_hora = self.__tela_inserir_hora.open()
                hora = value_hora["horario"]
                self.__tela_inserir_hora.close()
                if hora in self.__agendamento.agenda[dia]:
                    self.__agendamento.agenda[dia].remove(hora)
                    self.__agendamento.agendamentos[paciente.nome] = {"paciente": paciente, "agendamento": [dia, hora], "enfermeiro": enfermeiro_escolhido}
                    sg.popup("Agendamento realizado com sucesso!")
                else:
                    sg.popup("Data não disponível")
        else:
            if paciente.nome in self.__agendamento.agendamentos:
                sg.popup("Paciente já possui agendamento")
            else:
                enfermeiro_escolhido = controlador_enfermeiro.buscar_enfermeiro()
                if enfermeiro_escolhido == None:
                    sg.popup("Erro", "Enfermeiro não cadastrado!")
                    enfermeiro_escolhido = controlador_enfermeiro.inserir_enfermeiro(None, None, None, None)
                    button, value_dia = self.__tela_inserir_dia.open()
                    self.__tela_inserir_dia.close()
                    dia = value_dia["dia_da_semana"].lower().capitalize()
                    self.__tela_inserir_hora.init_components(self.__agendamento.agenda[dia])
                    button, value_hora = self.__tela_inserir_hora.open()
                    hora = value_hora["horario"]
                    self.__tela_inserir_hora.close()
                    print(self.__agendamento.agenda[dia])
                    if hora in self.__agendamento.agenda[dia]:
                        self.__agendamento.agenda[dia].remove(hora)
                        self.__agendamento.agendamentos[paciente.nome] = {"paciente": paciente, "agendamento": [dia, hora], "enfermeiro": enfermeiro_escolhido}
                        print(self.__agendamento.agendamentos)
                        print(self.__agendamento.agendamentos[paciente.nome])
                        sg.popup("Agendamento realizado com sucesso!")
                    else:
                        sg.popup("Data não disponível")

    def buscar_agendamento(self):
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        paciente = controlador_paciente.buscar_paciente()
        if paciente == None:
            sg.popup("Paciente ainda não cadastrado!")
        else:
            if paciente.nome not in self.__agendamento.agendamentos:
                sg.popup("Paciente sem agendamento!")
            else:
                agendamento = self.__agendamento.agendamentos[paciente.nome]
                self.__tela_listagem.init_components(agendamento, "agendamento")
                self.__tela_listagem.open()
                self.__tela_listagem.close()
                

    def editar_agendamento(self):
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        controlador_enfermeiro = self.__controlador_sistema.controlador_enfermeiro
        paciente = controlador_paciente.buscar_paciente()
        if paciente == None:
            sg.popup("Paciente não cadastrado")
        else:
            if paciente.nome not in self.__agendamento.agendamentos:
                sg.popup("Paciente ainda não possui agendamento")
            else:
                button, value = self.__tela_mudanca_agendamento.open()
                
                if value["dia"]:
                    button, value_dia = self.__tela_inserir_dia.open()
                    self.__tela_inserir_dia.close()
                    dia_novo = value_dia["dia_da_semana"].lower().capitalize()
                    hora_antiga = self.__agendamento.agendamentos[paciente.nome]["agendamento"][1]
                    if hora_antiga in self.__agendamento.agenda[dia_novo]:
                        self.__agendamento.agenda[dia_novo].remove(hora_antiga)
                        self.__agendamento.agendamentos[paciente.nome]["agendamento"][0] = dia_novo
                    else:
                        sg.popup("Horario indisponível")
                        self.__tela_inserir_hora.init_components(self.__agendamento.agenda[dia])
                        hora_nova = self.__tela_inserir_hora.open()
                        if hora in self.__agendamento.agenda[dia]:
                            self.__agendamento.agenda[dia].remove(hora)
                            self.__agendamento.agendamentos[paciente.nome]["agendamento"][0] = dia_novo
                            self.__agendamento.agendamentos[paciente.nome]["agendamento"][1] = hora_nova


                elif value["hora"]:
                    dia = self.__agendamento.agendamentos[paciente.nome]["agendamento"][0]
                    self.__agendamento.agenda[dia].insert(0, self.__agendamento.agendamentos[paciente.nome]["agendamento"][1])
                    self.__tela_inserir_hora.init_components(self.__agendamento.agenda[dia])
                    button, value_hora = self.__tela_inserir_hora.open()
                    self.__agendamento.agenda[dia].remove(value_hora["horario"])
                    self.__tela_inserir_hora.close()
                    sg.popup("Alteração feita com sucesso!")
                   

                elif value["dia/hora"]:
                    button, value_dia = self.__tela_inserir_dia.open() 
                    self.__tela_inserir_dia.close()
                    dia = value_dia["dia_da_semana"].lower().capitalize()
                    self.__tela_inserir_hora.init_components(self.__agendamento.agenda[dia])
                    button, value_hora = self.__tela_inserir_hora.open()
                    hora = value_hora["horario"]
                    self.__tela_inserir_hora.close()
                    if hora in self.__agendamento.agenda[dia]:
                        self.__agendamento.agenda[dia].remove(hora)
                        self.__agendamento.agendamentos[paciente.nome]["agendamento"][1] = hora
                        self.__agendamento.agendamentos[paciente.nome]["agendamento"][0] = dia
                    else:
                        sg.popup("Horario indisponível")
                        self.__tela_inserir_hora.init_components(self.__agendamento.agenda[dia])
                        hora_nova = self.__tela_inserir_hora.open()
                        if hora in self.__agendamento.agenda[dia]:
                            self.__agendamento.agenda[dia].remove(hora)
                            self.__agendamento.agendamentos[paciente.nome]["agendamento"][0] = dia
                            self.__agendamento.agendamentos[paciente.nome]["agendamento"][1] = hora_nova

                else:
                    enfermeiro = controlador_enfermeiro.buscar_enfermeiro()
                    if enfermeiro == None:
                        enfermeiro = controlador_enfermeiro.inserir_enfermeiro(None, None, None, None)
                    self.__agendamento.agendamentos[paciente.nome]["enfermeiro"] = enfermeiro

    def excluir_agendamento(self):
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        paciente = controlador_paciente.buscar_paciente()
        if paciente == None:
            sg.popup("Paciente não cadastrado!")
        else:
            if paciente.nome not in self.__agendamento.agendamentos:
                sg.popup("Paciente ainda não possui agendamento")
            else:
                dia, hora = [str(w) for w in self.__agendamento.agendamentos[paciente.nome]["agendamento"]]
                self.__agendamento.agenda[dia.lower().capitalize()].remove(hora)
                del self.__agendamento.agendamentos[paciente.nome]
                sg.popup("Agendamento excluido com sucesso!")

    def listar_agendamentos(self):
        if self.__agendamento.agendamentos == {}:
            sg.popup("Ainda há agendamentos!")
        else:
            for agendamento in self.__agendamento.agendamentos:
                print(self.__agendamento.agendamentos[agendamento])
                self.__tela_listagem.init_components(self.__agendamento.agendamentos[agendamento], "agendamento")
                self.__tela_listagem.open()
                self.__tela_listagem.close()

    def retornar_sistema(self):
        return self.__controlador_sistema

    def gera_relatorio(self):
        estilo.clear()
        if self.__agendamento.agendamentos == {}:
            self.__tela_agendamento.mostra_msg_sem_relatorio()
        else:
            self.__tela_relatorio.mostra_relatorio(self.__agendamento.agendamentos)
        estilo.clear()

    def abre_tela(self):
        opcoes = {1: self.inserir_agendamento, 2: self.editar_agendamento, 3: self.excluir_agendamento,
                  4: self.listar_agendamentos, 5: self.gera_relatorio, 6: self.buscar_agendamento, 7: self.retornar_sistema}
        
        while True:
            button, values = self.__tela_agendamento.open()
            if button == "Sair":
                break
            else:
                index= 1
                for i in values.values():
                    if i:
                        opcoes[index]()
                    index += 1
