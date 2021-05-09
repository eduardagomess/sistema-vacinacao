import PySimpleGUI as sg 


class TelaAgendamento():

    def __init__(self, controlador_agendamento):
        self.__controlador_enfermeiro = controlador_agendamento
        self.__window = None
        self.init_components()


    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout =[

            [sg.Text('Área de Agendamentos', size=(20, 1), font=("Helvetica", 15))],
            [sg.Radio('Inserir agendamento', "AREA", key=1)],
            [sg.Radio('Editar agendamento', "AREA", key=2)],
            [sg.Radio('Excluir agendamento', "AREA", key=3)], 
            [sg.Radio('Listar agendamentos', "AREA", key=4)],
            [sg.Radio('Relatório de agendamentos', "AREA", key=5)],
            [sg.Radio('Buscar agendamento', "AREA", key=6)],
            [sg.Button('Aplicar'), sg.Button('Sair')]
        ]

        self.__window = sg.Window("Tela Agendamento").layout(layout)
        
    def open(self):
        
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
   
       

    