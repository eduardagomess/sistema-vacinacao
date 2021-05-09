import PySimpleGUI as sg 


class TelaBuscaEnfermeiro():

    def __init__(self, controlador_enfermeiro):
        self.__controlador_enfermeiro = controlador_enfermeiro
        self.__window = None
        self.init_components()

    
    def init_components(self):
        layout =[
                [sg.Text('Insira o coren do enfermeiro', size=(30, 1)), sg.InputText()],
                [sg.Button('Aplicar'), sg.Button('Sair')]
            ]
        self.__window = sg.Window("Tela Enfermeiro").layout(layout)
 
    
    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
   