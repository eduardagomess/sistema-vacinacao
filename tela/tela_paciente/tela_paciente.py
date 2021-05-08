import PySimpleGUI as sg 


class TelaPaciente():

    def __init__(self, controlador_paciente):
        self.__controlador_paciente = controlador_paciente
        self.__window = None
        self.init_components()


    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout =[

            [sg.Text('Área de Pacientes', size=(20, 1), font=("Helvetica", 15))],
            [sg.Radio('Incluir paciente', "AREA", key=1)],
            [sg.Radio('Listar pacientes', "AREA", key=2)],
            [sg.Radio('Alterar informações do paciente', "AREA", key=3)], 
            [sg.Radio('Excluir pacientes', "AREA", key=4)],
            [sg.Radio('Buscar paciente', "AREA", key=5)],
            [sg.Button('Aplicar'), sg.Button('Sair')]
        ]

        self.__window = sg.Window("Tela Paciente").layout(layout)
        
    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
    