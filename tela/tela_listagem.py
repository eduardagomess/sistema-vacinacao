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
        
        
        elif tipo == "agendamentos":

            lista = [[sg.Text('Agendamento(s) cadastrado(s)', justification = 'center', text_color='#4682B4', font=("Helvetica", 15))]]

            for agendamento in informacoes:
                lista += [[sg.Text('Nome do paciente: ' + informacoes[agendamento]["paciente"].nome.title() + "\n" 
                + 'A vacina está marcada para ' + informacoes[agendamento]["agendamento"][0] + " às " + informacoes[agendamento]["agendamento"][1] + "\n" 
                + 'Nome do Enfermeiro(a): ' + informacoes[agendamento]["enfermeiro"].nome.title() + "\n" + 
                'COREN do enfermeiro: ' + informacoes[agendamento]["enfermeiro"].coren + "\n", font=("Helvetica", 15))]]
            
            layout = lista

            self.__window = sg.Window('Relatório de Agendamentos', default_button_element_size=(40, 1), size=(800,800)).Layout(layout)


        elif tipo == "agendamento":

            lista = [[sg.Text('Informações Agendamento', justification = 'center', text_color='#4682B4', font=("Helvetica", 15))]]

            lista += [[sg.Text('Nome do paciente: ' + informacoes["paciente"].nome.title() + "\n" 
                + 'A vacina está marcada para ' + informacoes["agendamento"][0] + " às " + informacoes["agendamento"][1] + "\n" 
                + 'Nome do Enfermeiro(a): ' + informacoes["enfermeiro"].nome.title() + "\n" + 
                'COREN do enfermeiro: ' + informacoes["enfermeiro"].coren + "\n", font=("Helvetica", 15))]]
            
            layout = lista

            self.__window = sg.Window('Informações Agendamento', default_button_element_size=(40, 1), size=(800,800)).Layout(layout)


        elif tipo == "paciente_relatorio":
            
            lista = [[sg.Text('Informação paciente', justification = 'center', text_color='#4682B4', font=("Helvetica", 15))]]

            lista += [[sg.Text('Nome do paciente: ' + informacoes["paciente"].nome.title() + "\n" 
                + 'Telefone do paciente: ' + informacoes["paciente"].telefone + "\n" + 'CPF do paciente: '
                + informacoes["paciente"].cpf + "\n" + 'Endereço do paciente: ' +informacoes["paciente"].endereco.mostrar_endereco() + "\n" 
                +  'Data de nascimento do paciente: ' + informacoes["paciente"].data_nascimento,  font=("Helvetica", 15))]]

            layout = lista

            self.__window = sg.Window('Relatório de Paciente', default_button_element_size=(40, 1), size=(800,800)).Layout(layout)
        

        elif tipo == "enfermeiro-relatorio":

            lista = [[sg.Text('Informação enfermeiro', justification = 'center', text_color='#4682B4', font=("Helvetica", 15))]]

            lista += [[sg.Text('Nome do enfermeiro: ' + informacoes.nome.title() + "\n" 
                + 'Telefone do enfermeiro: ' + informacoes.telefone + "\n" + 'CPF do enfermeiro: ' 
                + informacoes.cpf + "\n" + 'COREN do enfermeiro: ' + informacoes.coren + "\n", font=("Helvetica", 15))]]
            
            layout = lista
            self.__window = sg.Window('Relatório de Enfermeiros', default_button_element_size=(40, 1), size=(800,800)).Layout(layout)


        elif tipo == "lista_pacientes":
            lista = [[sg.Text('Paciente(s) do enfermeiro(a)' + informacoes.nome.title(), justification = 'center', text_color='#4682B4', font=("Helvetica", 15))]]

            for paciente in informacoes.lista_pacientes:
                lista += [[sg.Text('Nome do paciente: ' + paciente.nome.title() + "\n" , font=("Helvetica", 15))]]
            
            layout = lista
            self.__window = sg.Window('Relatório de Pacientes', default_button_element_size=(40, 1), size=(800,800)).Layout(layout)

        elif tipo == "relatorio":
            lista = [[sg.Text('Relatório Geral', justification = 'center', text_color='#4682B4', font=("Helvetica", 15))]]

            for agendamento in informacoes:
             
                if informacoes[agendamento]["paciente"].dose == 0:
                    lista += [[sg.Text('Nome do paciente: ' + informacoes[agendamento]["paciente"].nome.title() + "\n" 
                    + 'Telefone do paciente: ' + informacoes[agendamento]["paciente"].telefone + "\n" + 
                    'CPF do paciente: ' + informacoes[agendamento]["paciente"].cpf + "\n" +
                    'Endereço do paciente: ' + informacoes[agendamento]["paciente"].endereco.mostrar_endereco() + "\n" 
                    + 'Data de nascimento do paciente: ' + informacoes[agendamento]["paciente"].data_nascimento + "\n" +
                    "Informações do agendamento:  " + "A vacina está marcada para " + informacoes[agendamento]["agendamento"][0] + " às " + 
                    informacoes[agendamento]["agendamento"][1] + "\n" + "Status da vacinação: " +  "Paciente ainda não foi vacinado",font=("Helvetica", 15))]]

                    layout = lista
                    self.__window = sg.Window('Relatório de Pacientes', default_button_element_size=(40, 1), size=(800,800)).Layout(layout)  

                elif informacoes[agendamento]["paciente"].dose == 1:
                    
                    lista += [[sg.Text('Nome do paciente: ' + informacoes[agendamento]["paciente"].nome.title() + "\n" 
                    + 'Telefone do paciente: ' + informacoes[agendamento]["paciente"].telefone + "\n" + 'CPF do paciente: ' +
                    informacoes[agendamento]["paciente"].cpf + "\n" + 'Endereço do paciente: ' + informacoes[agendamento]["paciente"].endereco.mostrar_endereco()
                    + "\n" + 'Data de nascimento do paciente: ' + informacoes[agendamento]["paciente"].data_nascimento + "\n" + "Informações do agendamento:  " + 
                    "A vacina está marcada para " + informacoes[agendamento]["agendamento"][0] + " às " + informacoes[agendamento]["agendamento"][1] + 
                    "\n" + "Status da vacinação: " +  "Paciente já tomou a primeira dose da vacina" + "\n" +
                    "Tipo da dose: " + informacoes[agendamento]["paciente"].tipo_dose,font=("Helvetica", 15))]]

                    layout = lista
                    self.__window = sg.Window('Relatório de Pacientes', default_button_element_size=(40, 1), size=(800,800)).Layout(layout)  

                elif informacoes[agendamento]["paciente"].dose == 2:
                    
                    lista += [[sg.Text('Nome do paciente: ' + informacoes[agendamento]["paciente"].nome.title() + "\n" 
                    + 'Telefone do paciente: ' + informacoes[agendamento]["paciente"].telefone + "\n" + 'CPF do paciente: ' +
                    informacoes[agendamento]["paciente"].cpf + "\n" + 'Endereço do paciente: ' + informacoes[agendamento]["paciente"].endereco.mostrar_endereco()
                    + "\n" + 'Data de nascimento do paciente: ' + informacoes[agendamento]["paciente"].data_nascimento + "\n" + "Informações do agendamento:  " + 
                    "A vacina está marcada para " + informacoes[agendamento]["agendamento"][0] + " às " + informacoes[agendamento]["agendamen+==to"][1] + "\n" +
                    "Nome do Enfermeiro(a): " + informacoes[agendamento]["enfermeiro"].nome + "\n" + "COREN do Enfermeiro(a): " + informacoes[agendamento]["enfermeiro"].coren +
                    "\n" + "Status da vacinação: " +  "Paciente já recebeu todas as doses" + "\n" +
                    "Tipo da dose: " + informacoes[agendamento]["paciente"].tipo_dose,font=("Helvetica", 15))]]
                
                    layout = lista
                    self.__window = sg.Window('Relatório de Pacientes', default_button_element_size=(40, 1), size=(800,800)).Layout(layout)  

    def open(self):
        self.init_components(None, None)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)