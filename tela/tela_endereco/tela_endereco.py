import PySimpleGUI as sg 


class TelaEndereco():

    def __init__(self, controlador_paciente):
        self.__controlador_paciente = controlador_paciente
        self.__window = None
        self.init_components()


    def init_components(self):
        sg.theme('DarkBlue')
        layout =[
                [sg.Text('Bairro', size=(30, 1)), sg.InputText('bairro',  key='bairro')],
                [sg.Text('Rua', size=(30, 1)), sg.InputText('rua',  key='rua')],
                [sg.Text('Número', size=(30, 1)), sg.InputText('número',  key='numero')], 
                [sg.Text('Complemento', size=(30, 1)), sg.InputText('complemento',  key='complemento')],
                [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window("Tela Paciente").layout(layout)

    
    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)