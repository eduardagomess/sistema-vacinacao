import PySimpleGUI as sg 


class TelaBuscaEnfermeiro():

    def __init__(self, controlador_enfermeiro):
        self.__controlador_enfermeiro = controlador_enfermeiro
        self.__window = None
        self.init_components()
    
    def init_components(self):
        layout =[
                [sg.Text('Insira o coren do enfermeiro', size=(25, 1), font=("Helvetica", 15)), sg.InputText(font=("Helvetica", 15))],
                [sg.Button('Aplicar', font=("Helvetica", 15),size=(5,1)), sg.Button('Sair', font=("Helvetica", 15),size=(5,1))]
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
   