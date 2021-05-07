import PySimpleGUI as sg 


class TelaEditarPaciente():

    def __init__(self, controlador_paciente):
        self.__controlador_paciente = controlador_paciente
        self.__window = None
        self.init_components(None)


    def init_components(self, mudanca):
        sg.theme('DarkBlue')
        if mudanca == "nome":
            layout =[
                [sg.Text('Nome', size=(30, 1)), sg.InputText('nome',  key='nome')],
                [sg.Submit(), sg.Cancel()] 
            ]
            self.__window = sg.Window("Tela Paciente").layout(layout)
        elif mudanca == "telefone":
            layout =[
                [sg.Text('Telefone', size=(30, 1)), sg.InputText('telefone',  key='telefone')],
                [sg.Submit(), sg.Cancel()] 
            ]
            self.__window = sg.Window("Tela Paciente").layout(layout)
        elif mudanca == "cpf":
            layout =[
                [sg.Text('CPF', size=(30, 1)), sg.InputText('CPF',  key='CPF')],
                [sg.Submit(), sg.Cancel()]
            ]
            self.__window = sg.Window("Tela Paciente").layout(layout)
        else:
            layout =[
                [sg.Text('Data de nascimento', size=(30, 1)), sg.InputText('data de nascimento',  key='data_nascimento')],
                [sg.Submit(), sg.Cancel()]
            ]
            self.__window = sg.Window("Tela Paciente").layout(layout)

        
    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
   
       

    