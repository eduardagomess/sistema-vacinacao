import PySimpleGUI as sg 


class TelaBuscaPaciente():

    def __init__(self, controlador_paciente):
        self.__controlador_paciente = controlador_paciente
        self.__window = None
        self.init_components()

    
    def init_components(self):
        layout =[
            [sg.Text('Insira o nome ou cpf do paciente', size=(30, 1)), sg.InputText()],
            [sg.Button('Aplicar'), sg.Button('Sair')]
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
   