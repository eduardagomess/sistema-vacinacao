from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg

class TelaListaEstoque(AbstractTela):
    def __init__(self, controlador_estoque):
        super().__init__()
        self.__window = None
        self.__controlador_estoque = controlador_estoque
        self.init_components()

    def init_components(self):
        self.__window.close()

    def close(self):
        self.__window.Close()
