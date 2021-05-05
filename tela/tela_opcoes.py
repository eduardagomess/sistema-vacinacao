import PySimpleGUI as sg 


class TelaOpcoesPaciente():

    def __init__(self, controlador_paciente):
        self.__controlador_paciente = controlador_paciente
        self.__window = None
        self.mostra_opcao_busca()

    
    def mostra_opcao_busca(self):
        layout =[
            [sg.Text('Editar Pacientes', size=(20, 1), font=("Helvetica", 15))],
            [sg.Radio('Nome', "AREA", key=1)],
            [sg.Radio('CPF', "AREA", key=2)],
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
   