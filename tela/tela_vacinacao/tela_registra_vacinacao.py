from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg


class TelaRegistraVacinacao(AbstractTela):
    def __init__(self, controlador_vacinacao):
        super().__init__()
        self.__window = None
        self.__controlador_estoque = controlador_vacinacao
        self.init_components(None, None, None, None)

    def init_components(self, paciente, enfermeiro, dose, tipo_vacina):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Insira os dados a seguir')],
            [sg.Text('Nome do paciente:  ', size=(15, 1)), sg.InputText(paciente, key='paciente')],
            [sg.Text('Nome do Enfermeiro: ', size=(15, 1)), sg.InputText(enfermeiro, key='enfermeiro')],
            [sg.Text('Dose: ', size=(15, 1)), sg.InputText(dose, key='dose')],
            [sg.Text('Fabricante da vacina: ', size=(15, 1)), sg.InputText(tipo_vacina, key='tipo_vacina')],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Cadastro de estoque').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
