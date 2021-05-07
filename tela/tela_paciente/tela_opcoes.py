import PySimpleGUI as sg 


class TelaOpcoes():

    def __init__(self, controlador_paciente):
        self.__controlador_paciente = controlador_paciente
        self.__window = None
        self.init_components()


    def init_components(self):
        sg.theme('DarkBlue')
        layout =[

            [sg.Text('Alteração do cadastrao', size=(20, 1), font=("Helvetica", 15))],
            [sg.Radio('Alterar nome', "AREA", key="nome")],
            [sg.Radio('Alterar telefone', "AREA", key="telefone")],
            [sg.Radio('Alterar cpf', "AREA", key="cpf")], 
            [sg.Radio('Alterar endereço', "AREA", key="endereco")],
            [sg.Radio('Alterar data de nascimento', "AREA", key="data_nascimento")],
            [sg.Button('Aplicar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window("Área paciente").layout(layout)
        
    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
   