import PySimpleGUI as sg 


class TelaInserirEnfermeiro():

    def __init__(self, controlador_enfermeiro):
        self.__controlador_enfermeiro = controlador_enfermeiro
        self.__window = None
        self.init_components(None, None, None, None) 
    
    def init_components(self, nome, telefone, cpf, coren):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Cadastro enfermeiro', size=(20, 1),text_color='#4682B4', font=("Helvetica", 16, 'bold'))],
            [sg.Text('Nome', size=(30, 1), font=("Helvetica", 15)), sg.InputText(nome,  key='nome', font=("Helvetica", 15))], 
            [sg.Text('Telefone',size=(30, 1), font=("Helvetica", 15)), sg.InputText(telefone,  key='telefone', font=("Helvetica", 15))], 
            [sg.Text('CPF', size=(30, 1), font=("Helvetica", 15)), sg.InputText(cpf,  key='cpf', font=("Helvetica", 15))],
            [sg.Text('COREN', size=(30, 1), font=("Helvetica", 15)), sg.InputText(coren,  key='coren', font=("Helvetica", 15))],
            [sg.Button('Salvar', font=("Helvetica", 15),size=(5,1)), sg.Button('Sair', font=("Helvetica", 15),size=(5,1))]
        ] 
        self.__window = sg.Window('Cadastro').Layout(layout) 
    

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
   