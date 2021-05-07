import PySimpleGUI as sg 


class TelaSistema():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('DarkBlue')
        layout =[

            [sg.Text('Sistema de Vacinação', size=(20, 1), font=("Helvetica", 15))],
            [sg.Radio('Área de pacientes', "AREA", key=1)],
            [sg.Radio('Área de enfermeiros', "AREA", key=2)],
            [sg.Radio('Área de estoque', "AREA", key=3)], 
            [sg.Radio('Área de prontuários', "AREA", key=4)],
            [sg.Radio('Área de agendamentos', "AREA", key=5)],
            [sg.Radio('Área de registro de vacinas', "AREA", key=6)],
            [sg.Button('Aplicar'), sg.Button('Sair')]
        ]

        self.__window = sg.Window("Tela inicial").layout(layout)
    
    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
