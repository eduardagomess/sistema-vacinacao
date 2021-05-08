import PySimpleGUI as sg 


class TelaListagem():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__window = None
        self.init_components(None, None)

    def init_components(self, informacoes, tipo):
        sg.ChangeLookAndFeel('Reddit') 

        if tipo == "paciente":

            lista = [[sg.Text('Paciente(s) cadastrado(s)', justification = 'center', text_color='#4682B4', font=("Helvetica", 15))]]

            for paciente in informacoes:
                lista += [[sg.Text('Nome do paciente: ' + paciente.nome.title() + "\n" 
                + 'Telefone do paciente: ' + paciente.telefone + "\n" + 'CPF do paciente: '
                + paciente.cpf + "\n" + 'Endereço do paciente: ' + paciente.endereco.mostrar_endereco() + "\n" 
                +  'Data de nascimento do paciente: ' + paciente.data_nascimento,  font=("Helvetica", 15))]]

            layout = lista

            self.__window = sg.Window('Relatório de Pacientes', default_button_element_size=(40, 1), size=(800,800)).Layout(layout)

        
        elif tipo == "enfermeiro":

            lista = [[sg.Text('Enfermeiro(s) cadastrado(s)', justification = 'center', text_color='#4682B4', font=("Helvetica", 15))]]

            for enfermeiro in informacoes:
                lista += [[sg.Text('Nome do enfermeiro: ' + enfermeiro.nome.title() + "\n" 
                + 'Telefone do enfermeiro: ' + enfermeiro.telefone + "\n" + 'CPF do enfermeiro: ' 
                + enfermeiro.cpf + "\n" + 'COREN do enfermeiro: ' + enfermeiro.coren + "\n", font=("Helvetica", 15))]]
            
            layout = lista

            self.__window = sg.Window('Relatório de Enfermeiros', default_button_element_size=(40, 1), size=(800,800)).Layout(layout)
        
        
        elif tipo == "agendamento":

            lista = [[sg.Text('Agendamento(s) cadastrado(s)', justification = 'center', text_color='#4682B4', font=("Helvetica", 15))]]

            for agendamento in informacoes:
                lista += [[sg.Text('Nome do paciente: ' + agendamento["paciente"].nome.title() + "\n" 
                + 'A vacina está marcada para ' + agendamento["agendamento"][0] + " às " + agendamento["agendamento"][1] + "\n" 
                + 'Nome do Enfermeiro(a): ' + agendamento["enfermeiro"].nome.title() + "\n" + 
                'COREN do enfermeiro: ' + agendamento["enfermeiro"].coren + "\n", font=("Helvetica", 15))]]
            
            layout = lista

            self.__window = sg.Window('Relatório de Agendamentos', default_button_element_size=(40, 1), size=(800,800)).Layout(layout)

    def open(self):
        self.init_components(None, None)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)