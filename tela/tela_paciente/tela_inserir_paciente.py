import PySimpleGUI as sg 


class TelaInserirPaciente():

    def __init__(self, controlador_paciente):
        self.__controlador_paciente = controlador_paciente
        self.__window = None
        self.init_components(None, None, None, None, None, None, None, None)  
    
    def init_components(self, nome, telefone, cpf, bairro, rua, numero, complemento, data_nascimento):
        sg.ChangeLookAndFeel('Reddit') 
    
        layout = [
            [sg.Text('Cadastro Paciente', size=(20, 1),text_color='#4682B4', font=("Helvetica", 16, 'bold'))],  
            [sg.Text('Nome', size=(30, 1), font=("Helvetica", 15)), sg.InputText(nome,  key='nome', font=("Helvetica", 15))], 
            [sg.Text('Telefone', size=(30, 1), font=("Helvetica", 15)), sg.InputText(telefone,  key='telefone', font=("Helvetica", 15))], 
            [sg.Text('CPF', size=(30, 1), font=("Helvetica", 15)), sg.InputText(cpf,  key='cpf', font=("Helvetica", 15))],
            [sg.Text('Bairro', size=(30, 1), font=("Helvetica", 15)), sg.InputText(bairro,  key='bairro', font=("Helvetica", 15))],
            [sg.Text('Rua', size=(30, 1), font=("Helvetica", 15)), sg.InputText(rua,  key='rua', font=("Helvetica", 15))],
            [sg.Text('Número', size=(30, 1),font=("Helvetica", 15)), sg.InputText(numero,  key='numero', font=("Helvetica", 15))], 
            [sg.Text('Complemento',size=(30, 1), font=("Helvetica", 15)), sg.InputText(complemento,  key='complemento', font=("Helvetica", 15))],
            [sg.Text('Data de nascimento(DD/MM/AAAA)', size=(30, 1),font=("Helvetica", 15)), sg.InputText(data_nascimento,  key='data_nascimento', font=("Helvetica", 15))], 
            [sg.Button('Salvar', font=("Helvetica", 15),size=(5,1)), sg.Button('Sair', font=("Helvetica", 15),size=(5,1))]
        ] 
        self.__window = sg.Window('Cadastramento', size=(800,330)).layout(layout)
    

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)
   

   
    
   