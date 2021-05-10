import PySimpleGUI as sg 


class TelaAgendamento():

    def __init__(self, controlador_agendamento):
        self.__controlador_controlador_agendamento = controlador_agendamento
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout =[

            [sg.Text('Área de Agendamentos', size=(20, 1),text_color='#4682B4', font=("Helvetica", 16, 'bold'))],
            [sg.Radio('Inserir agendamento', "AREA", font=("Helvetica", 15), key=1)],
            [sg.Radio('Editar agendamento', "AREA", font=("Helvetica", 15), key=2)],
            [sg.Radio('Excluir agendamento', "AREA",font=("Helvetica", 15),  key=3)], 
            [sg.Radio('Listar agendamentos', "AREA",font=("Helvetica", 15), key=4)],
            [sg.Radio('Relatório de agendamentos', "AREA",font=("Helvetica", 15), key=5)],
            [sg.Radio('Buscar agendamento', "AREA", font=("Helvetica", 15), key=6)],
            [sg.Button('Aplicar', font=("Helvetica", 15),size=(5,1)), sg.Button('Sair', font=("Helvetica", 15),size=(5,1))]
        ]

        self.__window = sg.Window("Tela Agendamento", size=(500,280)).layout(layout)
        
    def open(self):
        
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
