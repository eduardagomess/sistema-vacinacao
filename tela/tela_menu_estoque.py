from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg


class TelaMenuEstoque(AbstractTela):
    def __init__(self, controlador_estoque):
        super().__init__()
        self.__controlador_estoque = controlador_estoque
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('DarkBlue')
        layout =[

            [sg.Text('Sistema de Vacinação', size=(20, 1), font=("Helvetica", 15))],
            [sg.Radio('Adicionar estoque', "AREA", key=1)],
            [sg.Radio('Editar estoque', "AREA", key=2)],
            [sg.Radio('Listar estoque', "AREA", key=3)],
            [sg.Radio('Buscar estoque de uma vacina', "AREA", key=4)],
            [sg.Radio('Excluir estoque', "AREA", key=5)],
            [sg.Button('Aplicar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Controle de Estoque').Layout(layout)

    def mostra_opcoes(self):
        botao, valores = self.__window.Read()
        if botao is None or botao == "Sair":
            botao = 6
        return int(botao)

    def buscar_vacina_nome(self):
        print(self.colorir_info("----- BUSCANDO VACINA ATRAVÉS DO NOME... -----"))
        return self.pegar_nome_vacina("Insira o nome da vacina que você procura: ")

    def buscar_vacina_lote(self):
        print(self.colorir_info("----- BUSCANDO VACINA ATRAVÉS DO LOTE... -----"))
        return self.pegar_nome_vacina("Insira o lote da vacina que você procura: ")

    def mostra_vacina_inexistente(self):
        print(self.colorir_erro("ESSA VACINA NÃO FOI ENCONTRADA!"))
        print(self.colorir_erro("Cadastre-a primeiro."))
        print(input("Aperte enter para continuar: "))

#Vai para outro arquivo
    def mostra_dados(self, estoque):
        if estoque == []:
            print(self.colorir_erro("O ESTOQUE ESTÁ VAZIO!"))
            print(input("Aperte enter para continuar: "))
        else:
            for vacina in estoque:
                print("Nome da vacina: {}".format(self.colorir_info(vacina.nome)))
                print("Número de aplicações que a vacina requer: {}".format(self.colorir_info(vacina.num_doses)))
                print("Número de doses em estoque: {}".format(self.colorir_info(vacina.qtd)))
                print("Data de recebimento de lote: {}".format(self.colorir_info((vacina.data_recebimento))))
                print("Número de lote: {}".format(self.colorir_info(vacina.lote)))

    def mostra_dados_vacina(self, vacina):
            print("Nome da vacina: {}".format(self.colorir_info(vacina.nome)))
            print("Número de aplicações que a vacina requer: {}".format(self.colorir_info(vacina.num_doses)))
            print("Número de doses em estoque: {}".format(self.colorir_info(vacina.qtd)))
            print("Data de recebimento de lote: {}".format(self.colorir_info((vacina.data_recebimento))))
            print("Número de lote: {}".format(self.colorir_info(vacina.lote)))

    def mostra_opcao_alterar_quantidade(self):
        print(self.colorir_info(" ----- ALTERAÇÃO DE ESTOQUE ----- "))
        print("Escolha a informação que deseja alterar")
        print("0 - Adicionar doses ao sistema")
        print("1 - Retirar doses do estoque")
        return self.pegar_opcao("Insira o número da opção desejada: ", [0, 1])

    def mostra_resposta_cadastrada(self):
        AbstractTela.msg(self, " Resposta cadastrada com sucesso! ")

    def mostra_mensagem_exclusao(self):
        AbstractTela.msg(self, "ESTOQUE EXCLUÍDO COM SUCESSO!")

    def mostra_lote_existente(self):
        AbstractTela.msg(self, "LOTE JÁ CADASTRADO!")

#rever
    def titulo_busca(self):
        print(self.colorir_info(" ----- VACINAS ENCONTRADAS -----  \n"))

    def mostra_tipo_vacina(self, tipo_vacina):
        print("Nome da vacina: {}".format(self.colorir_info(tipo_vacina.nome)))
        print("Número de aplicações que a vacina requer: {}".format(self.colorir_info(tipo_vacina.num_doses)))
        print("Número de doses em estoque: {}".format(self.colorir_info(tipo_vacina.qtd)))

    def pega_opcao_tipo_nao_cadastrado(self):
        print(self.colorir_erro("VACINA NÃO CADASTRADA!"))
        print(self.colorir_info("Escolha uma das opções abaixo: "))
        print("1 - Cadastrar vacina")
        print("2 - Retornar à tela principal")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2])

    def lote_inexistente(self):
        AbstractTela.msg(self,"LOTE INEXISTENTE!")

    def mostra_opcao_busca(self):
        print(" ----- MÉTODO DE BUSCA... -----")
        print("0 - Buscar através de nome")
        print("1 - Buscar através de lote")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [0, 1])

    def mostra_vacinas_insuficientes(self):
        AbstractTela.msg(self, "NÃO É POSSÍVEL EXCLUIR MAIS VACINAS DO QUE HÁ EM ESTOQUE!")


"""    def pega_dados_estoque(self):
        layout = [
         [sg.Text('Insira os dados a seguir')],
         [sg.Text('Nome da vacina: ', size=(15, 1)), sg.InputText('nome')],
         [sg.Text('Quantidade de doses recebidas: ', size=(15, 1)), sg.InputText('qtd')],
         [sg.Text('Data de recebimento: ', size=(15, 1)), sg.InputText('data_recebimento')],
         [sg.Text('Número de lote: ', size=(15, 1)), sg.InputText('lote')]
         [sg.Submit(), sg.Cancel()]
         ]
        window = sg.Window('Cadastro de estoque').Layout(layout)
        button, values = window.Read()

        self.__window = sg.Window("Tela inicial").layout(layout)"""
