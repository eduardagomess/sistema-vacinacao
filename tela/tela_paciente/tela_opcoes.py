import PySimpleGUI as sg 


class TelaOpcoes():

    def __init__(self, controlador_paciente):
        self.__controlador_paciente = controlador_paciente
        self.__window = None
        self.init_components()


    def init_components(self):
        sg.ChangeLookAndFeel('Reddit') 
        layout =[

            [sg.Text('Alteração do cadastrao', size=(20, 1),text_color='#4682B4', font=("Helvetica", 16, 'bold'))],
            [sg.Radio('Alterar nome', "AREA", font=("Helvetica", 15), key="nome")],
            [sg.Radio('Alterar telefone', "AREA", font=("Helvetica", 15),  key="telefone")],
            [sg.Radio('Alterar cpf', "AREA", font=("Helvetica", 15), key="cpf")], 
            [sg.Radio('Alterar endereço', "AREA", font=("Helvetica", 15), key="endereco")],
            [sg.Radio('Alterar data de nascimento', "AREA", font=("Helvetica", 15), key="data_nascimento")],
            [sg.Button('Aplicar', font=("Helvetica", 15),size=(5,1)), sg.Button('Sair', font=("Helvetica", 15),size=(5,1))]
        ]
        self.__window = sg.Window("Área paciente", size=(500,280)).layout(layout)
        
    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
   