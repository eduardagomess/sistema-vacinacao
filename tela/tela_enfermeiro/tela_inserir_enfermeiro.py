import PySimpleGUI as sg 


class TelaInserirEnfermeiro():

    def __init__(self, controlador_enfermeiro):
        self.__controlador_enfermeiro = controlador_enfermeiro
        self.__window = None
        self.init_components(None, None, None, None) 
    
    def init_components(self, nome, telefone, cpf, coren):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Preencha os campos a seguir')],  
            [sg.Text('Nome', size=(30, 1)), sg.InputText(nome,  key='nome')], 
            [sg.Text('Telefone', size=(30, 1)), sg.InputText(telefone,  key='telefone')], 
            [sg.Text('CPF', size=(30, 1)), sg.InputText(cpf,  key='cpf')],
            [sg.Text('COREN', size=(30, 1)), sg.InputText(coren,  key='coren')],
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
   