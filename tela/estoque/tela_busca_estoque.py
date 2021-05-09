from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg


class TelaBuscaEstoque(AbstractTela):
    def __init__(self, controlador_estoque):
        super().__init__()
        self.__window = None
        self.__controlador_estoque = controlador_estoque
        self.init_components()

    def init_components(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text("Escolha o método de busca desejado: ")],
            [sg.Radio('Nome', 'BUSCA'), sg.Radio('Lote', 'BUSCA')],
            [sg.InputText('Pfizer', key='nome')],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window("Sistema de Posto").Layout(layout)

    def open(self):
        button, valores = self.__window.Read()
        if button is None or button == "Sair":
            self.close()
        return button, valores

    def close(self):
        self.__window.Close()
