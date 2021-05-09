from tela.tela_abstrata import AbstractTela

import PySimpleGUI as sg


class TelaMenuEstoque(AbstractTela):
    def __init__(self, controlador_estoque):
        super().__init__()
        self.__controlador_estoque = controlador_estoque
        self.__window = None
        self.mostra_opcoes_estoque()

    def mostra_opcoes_estoque(self):
        sg.theme('Reddit')
        layout =[

            [sg.Text('Controle de estoque', size=(20, 1), font=("Helvetica", 15))],
            [sg.Radio('Adicionar estoque', "AREA", key=1)],
            [sg.Radio('Editar estoque', "AREA", key=2)],
            [sg.Radio('Listar estoque', "AREA", key=3)],
            [sg.Radio('Buscar estoque de uma vacina', "AREA", key=4)],
            [sg.Radio('Excluir estoque', "AREA", key=5)],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Sistema de Posto').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

#Vai para outro arquivo
    def mostra_dados(self, estoque):
            for vacina in estoque:
                print("Nome da vacina: {}".format(self.colorir_info(vacina.nome)))
                print("Número de aplicações que a vacina requer: {}".format(self.colorir_info(vacina.num_doses)))
                print("Número de doses em estoque: {}".format(self.colorir_info(vacina.qtd)))
                print("Data de recebimento de lote: {}".format(self.colorir_info((vacina.data_recebimento))))
                print("Número de lote: {}".format(self.colorir_info(vacina.lote)))

    def mostra_dados_estoque(self, estoque):
        self.msg("Vacina: {} \n Doses no sistema: {} \n Lote {} recebido em {}. \n ".format(estoque.tipo_vacina.nome, estoque.qtd, estoque.lote, estoque.data_recebimento))


    def lista_estoque(self, estoque):
        tps = []
        for estoq in estoque:
            tp = "Vacina: {} \n Doses no sistema: {} \n Lote {} recebido em {}. \n ".format(estoq.tipo_vacina.nome, estoq.qtd, estoq.lote, estoq.data_recebimento) + "\n"
            tps.append(tp)
        sg.Popup("Vacinas encontradas: \n", *tps, title = "Sistema de Posto")
        return list(tps)

#MENSAGENS
    def mostra_vacina_inexistente(self):
        self.msg("ESSA VACINA NÃO FOI ENCONTRADA! \n Cadastre-a primeiro!")

    def mostra_resposta_cadastrada(self):
        self.msg(" Resposta cadastrada com sucesso! ")

    def mostra_tipo_vacina(self, tipo_vacina):
        self.msg("Nome da vacina: {}".format(tipo_vacina.nome) +
            ("Número de aplicações que a vacina requer: {}".format(tipo_vacina.num_doses))
             + ("Número de doses em estoque: {}".format(tipo_vacina.qtd)))

    def pega_opcao_tipo_nao_cadastrado(self):
        self.msg("VACINA NÃO CADASTRADA!")

    def lote_inexistente(self):
        self.msg("LOTE INEXISTENTE!")

    def msg(self, msg: str):
        sg.popup(msg)
