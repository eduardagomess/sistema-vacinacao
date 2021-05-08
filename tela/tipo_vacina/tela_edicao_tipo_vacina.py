from tela import tipo_vacina
from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg


class TelaEditaTipoVacina(AbstractTela):
    def __init__(self, controlador_estoque):
        super().__init__()
        self.__window = None
        self.__controlador_estoque = controlador_estoque
        self.init_components()

    def init_components(self):
        self.passa_tipo_vacina(tipo_vacina)
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('Você pode editar os dados a seguir: ')],
            [sg.Text('nome', size=(15, 1)), sg.InputText(tipo_vacina_editar[1], key='nome')],
            [sg.Text( "Quantidade de doses que a vacina requer", size=(15, 1)), sg.InputText(tipo_vacina_editar[1], key='num_doses')],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Cadastro de estoque').Layout(layout)

    def passa_tipo_vacina(self, tipo_vacina):
        return tipo_vacina

    def open(self):
        button, values = self.__window.Read()
        return values

    def close(self):
        self.__window.Close()
