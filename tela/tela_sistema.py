import PySimpleGUI as sg 


class TelaSistema():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit') 
        layout =[

            [sg.Text('Sistema de Vacinação', size=(20, 1),text_color='#4682B4', font=("Helvetica", 16, 'bold'))],
            [sg.Radio('Área de pacientes', "AREA", font=("Helvetica", 15), key=1)],
            [sg.Radio('Área de enfermeiros', "AREA", font=("Helvetica", 15), key=2)],
            [sg.Radio('Área de estoque', "AREA", font=("Helvetica", 15), key=3)], 
            [sg.Radio('Área de prontuários', "AREA",  font=("Helvetica", 15), key=4)],
            [sg.Radio('Área de agendamentos', "AREA",  font=("Helvetica", 15), key=5)],
            [sg.Radio('Área de registro de vacinas', "AREA",  font=("Helvetica", 15), key=6)],
            [sg.Button('Aplicar', font=("Helvetica", 15),size=(5,1)), sg.Button('Sair', font=("Helvetica", 15),size=(5,1))]
        ]

        self.__window = sg.Window("Tela inicial", size=(500,350)).layout(layout)
    
    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
