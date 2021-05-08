import PySimpleGUI as sg 


class TelaListagem():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__window = None
        self.init_components(None, None)

    def init_components(self, informacoes, tipo):
        sg.ChangeLookAndFeel('Reddit') 

        if tipo == "paciente":
            
            layout =[
                [sg.Text('Nome do paciente: ' + informacoes.nome.title(), size=(80, 1), font=("Helvetica", 15))],
                [sg.Text('Telefone do paciente: ' + informacoes.telefone, size=(80, 1), font=("Helvetica", 15))],
                [sg.Text('CPF do paciente: ' + informacoes.cpf, size=(80, 1), font=("Helvetica", 15))],
                [sg.Text('Endereço do paciente: ' + informacoes.endereco.mostrar_endereco(), size=(80, 1), font=("Helvetica", 15))],
                [sg.Text('Data de nascimento do paciente: '+ informacoes.data_nascimento, size=(80, 1), font=("Helvetica", 15))],
                [sg.Button('Sair')]
            ]

            self.__window = sg.Window("Tela paciente").layout(layout)
        
        elif tipo == "enfermeiro":
            layout =[
                [sg.Text('Nome do enfermeiro: ' + informacoes.nome.title(), size=(80, 1), font=("Helvetica", 15))],
                [sg.Text('Telefone do enfermeiro: ' + informacoes.telefone, size=(80, 1), font=("Helvetica", 15))],
                [sg.Text('CPF do enfermeiro: ' + informacoes.cpf, size=(80, 1), font=("Helvetica", 15))],
                [sg.Text('COREN do enfermeiro: ' + informacoes.coren, size=(80, 1), font=("Helvetica", 15))],
                [sg.Button('Sair')]
            ]

            self.__window = sg.Window("Tela enfermeiro").layout(layout)
        
        elif tipo == "agendamento":
            layout =[

                [sg.Text("Nome do paciente: " + informacoes["paciente"].nome.title(), size=(80, 1), font=("Helvetica", 15))],
                [sg.Text("A vacina está marcada para " + informacoes["agendamento"][0] + " às " + informacoes["agendamento"][1], size=(80, 1), font=("Helvetica", 15))],
                [sg.Text("Nome do Enfermeiro(a): " + informacoes["enfermeiro"].nome.title(), size=(80, 1), font=("Helvetica", 15))],
                [sg.Text('COREN do enfermeiro: ' + informacoes["enfermeiro"].coren, size=(80, 1), font=("Helvetica", 15))],
                [sg.Button('Sair')]
            ]

            self.__window = sg.Window("Tela enfermeiro").layout(layout)

    
    def open(self):
        self.init_components(None, None)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)