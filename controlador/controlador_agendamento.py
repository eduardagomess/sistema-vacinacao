from tela.tela_agendamento.tela_agendamento import TelaAgendamento
from tela.tela_agendamento.tela_inserir_agendamento_dia import TelaInserirDia
from tela.tela_agendamento.tela_inserir_agendamento_hora import TelaInserirHora
from tela.tela_agendamento.tela_mudanca_agendamento import TelaMudancaAgendamento
from tela.tela_listagem import TelaListagem
from entidade.agendamento import Agendamento
from persistencia.agendamentoDAO import AgendamentoDAO
from utils import estilo
import PySimpleGUI as sg
import time


class ControladorAgendamento:

    def __init__(self, controlador_sistema):
        self.__tela_agendamento = TelaAgendamento(self)
        self.__tela_inserir_dia = TelaInserirDia(self)
        self.__tela_inserir_hora = TelaInserirHora(self)
        self.__tela_listagem = TelaListagem(self)
        self.__tela_mudanca_agendamento = TelaMudancaAgendamento(self)
        self.__controlador_sistema = controlador_sistema
        self.__agendamentoDAO = AgendamentoDAO()
        
    def inserir_agendamento(self):
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        controlador_enfermeiro = self.__controlador_sistema.controlador_enfermeiro
        paciente = controlador_paciente.buscar_paciente()
        if paciente == None:
            sg.popup("Erro", "Paciente não cadastrado!", font=("Helvetica", 15, "bold"), text_color='red')
            paciente = controlador_paciente.inserir_paciente(None, None, None, None, None, None, None, None)
            enfermeiro= controlador_enfermeiro.buscar_enfermeiro()
            if enfermeiro == None:
                sg.popup("Erro", "Enfermeiro não cadastrado!", font=("Helvetica", 15, "bold"), text_color='red')
                enfermeiro_escolhido = controlador_enfermeiro.inserir_enfermeiro(None, None, None, None)
                button, value_dia = self.__tela_inserir_dia.open()
                self.__tela_inserir_dia.close()
                dia = value_dia["dia_da_semana"].lower().capitalize()
                self.__tela_inserir_hora.init_components(self.__agendamentoDAO.get().agenda[dia])
                button, value_hora = self.__tela_inserir_hora.open()
                hora = value_hora["horario"]
                self.__tela_inserir_hora.close()
                if hora in self.__agendamentoDAO.get().agenda[dia]:
                    self.__agendamentoDAO.get().agenda[dia].remove(hora)
                    self.__agendamentoDAO.save()
                    self.__agendamentoDAO.get().agendamentos[paciente.nome] = {"paciente": paciente, "agendamento": [dia, hora], "enfermeiro": enfermeiro_escolhido}
                    self.__agendamentoDAO.save()
                    sg.popup("Agendamento realizado com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')
                else:
                    sg.popup("Data não disponível", font=("Helvetica", 15, "bold"), text_color='red')
        else:
            if paciente.nome in self.__agendamentoDAO.get().agendamentos:
                sg.popup("Paciente já possui agendamento", font=("Helvetica", 15, "bold"), text_color='red')
            else:
                enfermeiro_escolhido = controlador_enfermeiro.buscar_enfermeiro()
                if enfermeiro_escolhido == None:
                    sg.popup("Erro", "Enfermeiro não cadastrado!", font=("Helvetica", 15, "bold"), text_color='red')
                    enfermeiro_escolhido = controlador_enfermeiro.inserir_enfermeiro(None, None, None, None)
                    button, value_dia = self.__tela_inserir_dia.open()
                    self.__tela_inserir_dia.close()
                    dia = value_dia["dia_da_semana"].lower().capitalize()
                    self.__tela_inserir_hora.init_components(self.__agendamentoDAO.get().agenda[dia])
                    button, value_hora = self.__tela_inserir_hora.open()
                    hora = value_hora["horario"]
                    self.__tela_inserir_hora.close()
                    if hora in self.__agendamentoDAO.get().agenda[dia]:
                        self.__agendamentoDAO.get().agenda[dia].remove(hora)
                        self.__agendamentoDAO.get().agendamentos[paciente.nome] = {"paciente": paciente, "agendamento": [dia, hora], "enfermeiro": enfermeiro_escolhido}
                        self.__agendamentoDAO.save()
                        sg.popup("Agendamento realizado com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')
                    else:
                        sg.popup("Data não disponível", font=("Helvetica", 15, "bold"), text_color='red')
                else:
                    button, value_dia = self.__tela_inserir_dia.open()
                    self.__tela_inserir_dia.close()
                    dia = value_dia["dia_da_semana"].lower().capitalize()
                    self.__tela_inserir_hora.init_components(self.__agendamentoDAO.get().agenda[dia])
                    button, value_hora = self.__tela_inserir_hora.open()
                    hora = value_hora["horario"]
                    self.__tela_inserir_hora.close()
                    if hora in self.__agendamentoDAO.get().agenda[dia]:
                        self.__agendamentoDAO.get().agenda[dia].remove(hora)
                        self.__agendamentoDAO.get().agendamentos[paciente.nome] = {"paciente": paciente, "agendamento": [dia, hora], "enfermeiro": enfermeiro_escolhido}
                        self.__agendamentoDAO.save()
                        sg.popup("Agendamento realizado com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')
                    else:
                        sg.popup("Data não disponível", font=("Helvetica", 15, "bold"), text_color='red')

    def buscar_agendamento(self):
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        paciente = controlador_paciente.buscar_paciente()
        if paciente == None:
            sg.popup("Paciente ainda não cadastrado!", font=("Helvetica", 15, "bold"), text_color='red')
        else:
            if paciente.nome not in self.__agendamentoDAO.get().agendamentos:
                sg.popup("Paciente sem agendamento!", font=("Helvetica", 15, "bold"), text_color='red')
            else:
                agendamento = self.__agendamentoDAO.get().agendamentos[paciente.nome]
                self.__tela_listagem.init_components(agendamento, "agendamento")
                self.__tela_listagem.open()
                self.__tela_listagem.close()
                
    def editar_agendamento(self):
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        controlador_enfermeiro = self.__controlador_sistema.controlador_enfermeiro
        paciente = controlador_paciente.buscar_paciente()
        if paciente == None:
            sg.popup("Paciente não cadastrado", font=("Helvetica", 15, "bold"), text_color='red')
        else:
            if paciente.nome not in self.__agendamentoDAO.get().agendamentos:
                sg.popup("Paciente ainda não possui agendamento", font=("Helvetica", 15, "bold"), text_color='red')
            else:
                button, value = self.__tela_mudanca_agendamento.open()
                
                if value["dia"]:
                    button, value_dia = self.__tela_inserir_dia.open()
                    self.__tela_inserir_dia.close()
                    dia_novo = value_dia["dia_da_semana"].lower().capitalize()
                    hora_antiga = self.__agendamentoDAO.get().agendamentos[paciente.nome]["agendamento"][1]
                    if hora_antiga in self.__agendamentoDAO.get().agenda[dia_novo]:
                        self.__agendamentoDAO.get().agenda[dia_novo].remove(hora_antiga)
                        self.__agendamentoDAO.get().agendamentos[paciente.nome]["agendamento"][0] = dia_novo
                        self.__agendamentoDAO.save()
                    else:
                        sg.popup("Horario indisponível")
                        self.__tela_inserir_hora.init_components(self.__agendamentoDAO.get().agenda[dia])
                        hora_nova = self.__tela_inserir_hora.open()
                        if hora in self.__agendamento.agenda[dia]:
                            self.__agendamentoDAO.get().agenda[dia].remove(hora)
                            self.__agendamentoDAO.get().agendamentos[paciente.nome]["agendamento"][0] = dia_novo
                            self.__agendamentoDAO.get().agendamentos[paciente.nome]["agendamento"][1] = hora_nova
                            self.__agendamentoDAO.save()

                elif value["hora"]:
                    dia = self.__agendamentoDAO.get().agendamentos[paciente.nome]["agendamento"][0]
                    self.__agendamentoDAO.get().agenda[dia].insert(0, self.__agendamentoDAO.get().agendamentos[paciente.nome]["agendamento"][1])
                    self.__tela_inserir_hora.init_components(self.__agendamentoDAO.get().agenda[dia])
                    button, value_hora = self.__tela_inserir_hora.open()
                    self.__agendamentoDAO.get().agenda[dia].remove(value_hora["horario"])
                    self.__agendamentoDAO.save()
                    self.__tela_inserir_hora.close()
                    sg.popup("Alteração feita com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')
                   
                elif value["dia/hora"]:
                    button, value_dia = self.__tela_inserir_dia.open() 
                    self.__tela_inserir_dia.close()
                    dia = value_dia["dia_da_semana"].lower().capitalize()
                    self.__tela_inserir_hora.init_components(self.__agendamentoDAO.get().agenda[dia])
                    button, value_hora = self.__tela_inserir_hora.open()
                    hora = value_hora["horario"]
                    self.__tela_inserir_hora.close()
                    if hora in self.__agendamentoDAO.get().agenda[dia]:
                        self.__agendamentoDAO.get().agenda[dia].remove(hora)
                        self.__agendamentoDAO.get().agendamentos[paciente.nome]["agendamento"][1] = hora
                        self.__agendamentoDAO.get().agendamentos[paciente.nome]["agendamento"][0] = dia
                        self.__agendamentoDAO.save()
                    else:
                        sg.popup("Horario indisponível")
                        self.__tela_inserir_hora.init_components(self.__agendamentoDAO.get().agenda[dia])
                        hora_nova = self.__tela_inserir_hora.open()
                        if hora in self.__agendamentoDAO.get().agenda[dia]:
                            self.__agendamentoDAO.get().agenda[dia].remove(hora)
                            self.__agendamentoDAO.get().agendamentos[paciente.nome]["agendamento"][0] = dia
                            self.__agendamentoDAO.get().agendamentos[paciente.nome]["agendamento"][1] = hora_nova
                            self.__agendamentoDAO.save()
                else:
                    enfermeiro = controlador_enfermeiro.buscar_enfermeiro()
                    if enfermeiro == None:
                        enfermeiro = controlador_enfermeiro.inserir_enfermeiro(None, None, None, None)
                    self.__agendamentoDAO.get().agendamentos[paciente.nome]["enfermeiro"] = enfermeiro
                    self.__agendamentoDAO.save()

    def excluir_agendamento(self):
        controlador_paciente = self.__controlador_sistema.controlador_paciente
        paciente = controlador_paciente.buscar_paciente()
        if paciente == None:
            sg.popup("Paciente não cadastrado!", font=("Helvetica", 15, "bold"), text_color='red')
        else:
            if paciente.nome not in self.__agendamentoDAO.get().agendamentos:
                sg.popup("Paciente ainda não possui agendamento", font=("Helvetica", 15, "bold"), text_color='red')
            else:
                dia, hora = [str(w) for w in self.__agendamentoDAO.get().agendamentos[paciente.nome]["agendamento"]]
                self.__agendamentoDAO.get().agenda[dia.lower().capitalize()].append(hora)
                self.__agendamentoDAO.save()
                del self.__agendamentoDAO.get().agendamentos[paciente.nome]
                sg.popup("Agendamento excluido com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')

    def listar_agendamentos(self):
        if self.__agendamentoDAO.get().agendamentos == {}:
            sg.popup("Ainda há agendamentos!", font=("Helvetica", 15, "bold"), text_color='red')
        else:
            self.__tela_listagem.init_components(self.__agendamentoDAO.get().agendamentos, "agendamentos")
            self.__tela_listagem.open()
            self.__tela_listagem.close()

    def retornar_sistema(self):
        return self.__controlador_sistema

    def gera_relatorio(self):
        if self.__agendamentoDAO.get().agendamentos == {}:
            sg.popup("Ainda não relatório disponível", font=("Helvetica", 15, "bold"), text_color='#4682B4')
        else:
            self.__tela_listagem.init_components(self.__agendamentoDAO.get().agendamentos, "relatorio")
            self.__tela_listagem.open()
            self.__tela_listagem.close()

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
