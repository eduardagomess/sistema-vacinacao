import PySimpleGUI as sg 


class TelaEnfermeiro():

    def __init__(self, controlador_enfermeiro):
        self.__controlador_enfermeiro = controlador_enfermeiro
        self.__window = None
        self.init_components()


    def init_components(self):
        sg.ChangeLookAndFeel('Reddit') 
        layout =[

            [sg.Text('Área de Enfermeiro', size=(20, 1), font=("Helvetica", 15))],
            [sg.Radio('Incluir enfermeiro', "AREA", key=1)],
            [sg.Radio('Listar enfermeiros', "AREA", key=2)],
            [sg.Radio('Alterar informações do enfermeiro', "AREA", key=3)], 
            [sg.Radio('Excluir enfermeiro', "AREA", key=4)],
            [sg.Radio('Buscar enfermeiro', "AREA", key=5)],
            [sg.Radio('Listar pacientes do enfermeiro', "AREA", key=6)],
            [sg.Button('Aplicar'), sg.Button('Sair')]
        ]

        self.__window = sg.Window("Tela Enfermeiro").layout(layout)
        
    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
   
       

    