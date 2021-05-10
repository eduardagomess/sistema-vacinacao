from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg


class TelaListaEstoque(AbstractTela):
    def __init__(self, controlador_estoque):
        super().__init__()
        self.__window = None
        self.__controlador_estoque = controlador_estoque

    def init_components(self, compativeis, estoque):
        layout = [*[[sg.Text("Escolha uma dos lotes da vacina {} abaixo: ".format(opcao)),] for opcao in estoque],
                  *[[[sg.Radio(str(opcao), 1, key=opcao), ] for opcao in compativeis]],
                  [[sg.Submit(), sg.Cancel()]]
                  ]
        self.__window = sg.Window("Sistema de Posto", layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
