import PySimpleGUI as sg


class TelaRegistroTipoVacina:

    def __init__(self, controlador_tipo_vacina):
        self.__controlador_tipo_vacina = controlador_tipo_vacina
        self.__window = None
        self.pega_dados_vacina()

    def pega_dados_vacina(self):
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('Insira os dados a seguir')],
            [sg.Text('Nome da vacina: ', size=(15, 1)), sg.InputText('nome', key='nome')],
            [sg.Text('Quantidade de doses que a vacina requer: ', size=(15, 1)),
             sg.InputText('número de doses', key='num_doses')],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Sistema de Vacinação').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return values


"""            for dado in range(len(lista_dados)):
                dados_vacina.append(lista_dados[dado](mensagem[dado]))
            return dict(zip(dados_cadastro, dados_vacina))

        elif opcao == 2:
            opcao_escolhida  = self.mostra_opcao_editar()

            opcoes_mudanca = {0: "nome", 1: "num_doses"}

            dado = dados[opcao_escolhida](mensagem_edicao[opcao_escolhida])
            return [opcoes_mudanca[opcao_escolhida], str(dado)]
"""
