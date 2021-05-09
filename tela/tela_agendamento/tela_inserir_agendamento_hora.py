import PySimpleGUI as sg 


class TelaInserirHora():

    def __init__(self, controlador_agendamento):
        self.__controlador_agendamento = controlador_agendamento
        self.__window = None
        self.init_components(None) 
    
    def init_components(self, lista_horarios):
        sg.ChangeLookAndFeel('Reddit')        
        layout = [
            [sg.Text('Selecione o horario',size=(30, 1),  font =("Helvetica",15),justification='left', pad=(0,1))],
            [sg.Combo(lista_horarios,key='horario', size=(40,1), font =("Helvetica",15), pad=(0,10))],
            [sg.Button('Salvar'), sg.Button('Sair')]
        ]  
        
        self.__window = sg.Window('Cadastramento').Layout(layout) 
    

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
   