from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg

class TelaCadastraEstoque(AbstractTela):
    def __init__(self, controlador_estoque):
        super().__init__()
        self.__window = None
        self.__controlador_estoque = controlador_estoque
        self.exclui_estoque()

    def exclui_estoque(self):
        sg.theme('DarkBlue')
        self.__window.close()

    def close(self):
        self.__window.Close()
