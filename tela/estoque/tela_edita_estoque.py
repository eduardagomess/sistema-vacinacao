from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg


class TelaEditaEstoque(AbstractTela):
    def __init__(self, controlador_estoque):
        super().__init__()
        self.__window = None
        self.__controlador_estoque = controlador_estoque

    def mostra_opcao_alterar_quantidade(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Você pode editar os dados a seguir: ')],
            [sg.Radio('Adicionar doses ao sistema', "EDITA", size=(25, 1))],
            [sg.Radio("Retirar doses do estoque", "EDITA", size=(25, 1))],
            [sg.Text('Quantidade: ', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Cadastro de estoque').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
