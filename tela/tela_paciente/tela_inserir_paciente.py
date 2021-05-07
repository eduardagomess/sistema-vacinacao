import PySimpleGUI as sg 


class TelaInserirPaciente():

    def __init__(self, controlador_paciente):
        self.__controlador_paciente = controlador_paciente
        self.__window = None
        self.init_components(None, None, None, None, None, None, None, None)  
    
    def init_components(self, nome, telefone, cpf, bairro, rua, numero, complemento, data_nascimento):
        sg.ChangeLookAndFeel('Reddit')
    
        layout = [
            [sg.Text('Preencha os campos a seguir')],  
            [sg.Text('Nome', size=(30, 1)), sg.InputText(nome,  key='nome')], 
            [sg.Text('Telefone', size=(30, 1)), sg.InputText(telefone,  key='telefone')], 
            [sg.Text('CPF', size=(30, 1)), sg.InputText(cpf,  key='cpf')],
            [sg.Text('Bairro', size=(30, 1)), sg.InputText(bairro,  key='bairro')],
            [sg.Text('Rua', size=(30, 1)), sg.InputText(rua,  key='rua')],
            [sg.Text('Número', size=(30, 1)), sg.InputText(numero,  key='numero')], 
            [sg.Text('Complemento', size=(30, 1)), sg.InputText(complemento,  key='complemento')],
            [sg.Text('Data de nascimento(DD/MM/AAAA)', size=(30, 1)), sg.InputText(data_nascimento,  key='data_nascimento')], 
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
   

   
    
   