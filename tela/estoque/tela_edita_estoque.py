from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg


class TelaEditaEstoque(AbstractTela):
    def __init__(self, controlador_estoque):
        super().__init__()
        self.__window = None
        self.__controlador_estoque = controlador_estoque
        self.mostra_opcao_alterar_quantidade()

    def mostra_opcao_alterar_quantidade(self):
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('Você pode editar os dados a seguir: ')],
            [sg.Radio('Adicionar doses ao sistema', "EDITA", size=(15, 1), key=1)],
            [sg.Radio( "Retirar doses do estoque", "EDITA", size=(15, 1), key=2)],
            [sg.Text('Quantidade: ', size = (15,1)), sg.InputText("quantidade de doses")],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Cadastro de estoque').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        print(button, values)
        return values

    def close(self):
        self.__window.Close()
