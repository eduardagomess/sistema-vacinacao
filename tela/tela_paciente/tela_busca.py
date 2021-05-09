import PySimpleGUI as sg 


class TelaBuscaPaciente():

    def __init__(self, controlador_paciente):
        self.__controlador_paciente = controlador_paciente
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit') 
        layout =[

                [sg.Text('Insira o cpf do paciente', size=(20, 1), font=("Helvetica", 16)), sg.InputText(font=("Helvetica", 15))],
                [sg.Button('Aplicar', font=("Helvetica", 15),size=(5,1)), sg.Button('Sair', font=("Helvetica", 15),size=(5,1))]
            ]
        self.__window = sg.Window("Tela Paciente").layout(layout)

    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
   