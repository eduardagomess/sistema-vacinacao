import PySimpleGUI as sg 


class TelaListagem():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__window = None
        self.init_components(None, None)

    def init_components(self, informacoes, tipo_pessoa):
        sg.theme('DarkBlue')

        if tipo_pessoa == "paciente":
            layout =[
                [sg.Text('Nome do paciente: ' + informacoes.nome.title(), size=(80, 1), font=("Helvetica", 15))],
                [sg.Text('Telefone do paciente: ' + informacoes.telefone, size=(80, 1), font=("Helvetica", 15))],
                [sg.Text('CPF do paciente: ' + informacoes.cpf, size=(80, 1), font=("Helvetica", 15))],
                [sg.Text('Endereço do paciente: ' + informacoes.endereco.title(), size=(80, 1), font=("Helvetica", 15))],
                [sg.Text('Data de nascimento do paciente: '+ informacoes.data_nascimento, size=(80, 1), font=("Helvetica", 15))],
                [sg.Button('Sair')]
            ]

            self.__window = sg.Window("Tela paciente").layout(layout)
        
        else:
            layout =[
                [sg.Text('Sistema de Vacinação', size=(20, 1), font=("Helvetica", 15))],
                [sg.Radio('Área de pacientes', "AREA", key=1)],
                [sg.Button('Sair')]
            ]

            self.__window = sg.Window("Tela paciente").layout(layout)
            
    
    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)