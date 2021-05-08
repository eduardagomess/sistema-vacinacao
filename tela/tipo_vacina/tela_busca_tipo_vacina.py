from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg


class TelaBuscaTipoVacina(AbstractTela):

    def __init__(self, controlador_tipo_vacina):
        super().__init__()
        self.__controlador_tipo_vacina = controlador_tipo_vacina
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('Busca de vacina', size=(20, 1), font=("Helvetica", 15))],
            [sg.Text('Nome: '), sg.InputText()],
            [sg.Button('Aplicar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema de Vacinação').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        if button == None or button =='Sair':
            self.__window.close()
        return button, values

    def close(self):
        self.__window.Close()
