from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg

class TelaListaEstoque(AbstractTela):
    def __init__(self, controlador_estoque):
        super().__init__()
        self.__window = None
        self.__controlador_estoque = controlador_estoque
