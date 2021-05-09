import PySimpleGUI as sg 


class TelaMudancaAgendamento():

    def __init__(self, controlador_agendamento):
        self.__controlador_agendamento = controlador_agendamento
        self.__window = None
        self.init_components()


    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout =[
            [sg.Text('Alteração do agendamento', size=(20, 1), font=("Helvetica", 15))],
            [sg.Radio('alterar o dia da vacinação', "AREA", key="dia")],
            [sg.Radio('alterar o horario da vacinação', "AREA", key="hora")],
            [sg.Radio('alterar o dia e a horario da vacinação', "AREA", key="dia/hora")], 
            [sg.Radio('alterar o enfermeiro', "AREA", key="enfermeiro")],
            [sg.Button('Aplicar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window("Área paciente").layout(layout)
        
    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
   