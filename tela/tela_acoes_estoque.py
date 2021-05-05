from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg

class TelaAcoesEstoque(AbstractTela):
    def __init__(self, controlador_estoque):
        super().__init__()
        self.__controlador_estoque = controlador_estoque
        self.pega_dados_estoque()

    def pega_dados_estoque(self, opcao):
        layout = [
         [sg.Text('Insira os dados a seguir')],
         [sg.Text('Nome da vacina: ', size=(15, 1)), sg.InputText('nome')],
         [sg.Text('Quantidade de doses recebidas: ', size=(15, 1)), sg.InputText('qtd')],
         [sg.Text('Data de recebimento: ', size=(15, 1)), sg.InputText('data_recebimento')],
         [sg.Text('Número de lote: ', size=(15, 1)), sg.InputText('lote')],
         [sg.Submit(), sg.Cancel()]
         ]
        window = sg.Window('Cadastro de estoque').Layout(layout)
        button, values = window.Read()

        self.__window = sg.Window("Tela inicial").layout(layout)
