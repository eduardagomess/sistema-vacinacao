import PySimpleGUI as sg 


class TelaEnfermeiro():

    def __init__(self, controlador_enfermeiro):
        self.__controlador_enfermeiro = controlador_enfermeiro
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit') 
        layout =[

            [sg.Text('Área de Enfermeiro', size=(20, 1),text_color='#4682B4', font=("Helvetica", 16, 'bold'))],
            [sg.Radio('Incluir enfermeiro', "AREA", font=("Helvetica", 15), key=1)],
            [sg.Radio('Listar enfermeiros', "AREA", font=("Helvetica", 15), key=2)],
            [sg.Radio('Alterar informações do enfermeiro', "AREA", font=("Helvetica", 15), key=3)], 
            [sg.Radio('Excluir enfermeiro', "AREA", font=("Helvetica", 15),  key=4)],
            [sg.Radio('Buscar enfermeiro', "AREA",font=("Helvetica", 15),  key=5)],
            [sg.Radio('Listar pacientes do enfermeiro', "AREA",font=("Helvetica", 15),  key=6)],
            [sg.Button('Aplicar', font=("Helvetica", 15),size=(5,1)), sg.Button('Sair', font=("Helvetica", 15),size=(5,1))]
        ]

        self.__window = sg.Window("Tela Enfermeiro", size=(500,280)).layout(layout)
        
    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
   