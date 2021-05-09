import PySimpleGUI as sg 


class TelaInserirDia():

    def __init__(self, controlador_agendamento):
        self.__controlador_agendamento = controlador_agendamento
        self.__window = None
        self.init_components() 
    
    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')        
        layout = [
            [sg.Text('Selecione o dia',size=(30, 1),  font =("Helvetica",15),justification='left', pad=(0,1))],
            [sg.Combo(['Segunda','Terca','Quarta', 'Quinta','Sexta'],key='dia_da_semana', size=(40,1), font =("Helvetica",15), pad=(0,10))],
            [sg.Button('Salvar', font=("Helvetica", 15),size=(5,1)), sg.Button('Sair', font=("Helvetica", 15),size=(5,1))]
        ]  
        
        self.__window = sg.Window('Cadastramento').Layout(layout) 
    

    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
   