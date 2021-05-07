from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg

class TelaBuscaEstoque(AbstractTela):
    def __init__(self, controlador_estoque):
        super().__init__()
        self.__window = None
        self.__controlador_estoque = controlador_estoque
        self.init_components()

    def init_components(self):
        sg.theme('DarkBlue')
        layout = [
            [sg.Text("Escolha o método de busca desejado: ")],
            [sg.Text("Busca por nome"), sg.InputText('nome')],
            [sg.Text("Busca por lote"), sg.InputText('lote')],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window("Sistema de Posto").Layout(layout)

    def open(self):
        botao, valores = self.__window.Read()
        if botao is None or botao == "Sair":
            self.close()
        return valores

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)

    #msgbox aparecendo o conteudo buscado

