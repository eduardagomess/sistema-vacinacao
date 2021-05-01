from tela.tela_abstrata import AbstractTela


class TelaEstoque(AbstractTela):
    def __init__(self, controlador_estoque):
        super().__init__()
        self.__controlador_estoque = controlador_estoque


    def mostra_opcoes(self):
        print(self.colorir_titulo("------ ÁREA DE CONTROLE DE ESTOQUE --------"))
        print("Escolha uma das opções abaixo:")
        print("1 - Adicionar estoque")
        print("2 - Editar estoque")
        print("3 - Listar estoque")
        print("4 - Buscar estoque de uma vacina")
        print("5 - Excluir estoque")
        print("6 - Retornar a tela principal do sistema")

        opcao = self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5, 6])
        return opcao

    def pega_dados_estoque(self, opcao):
        dados = {0: self.pegar_nome_vacina, 1: self.pegar_num, 2: self.pegar_data_nascimento, 3: self.pegar_nome_vacina}
        mensagem = {0: "Insira o nome da vacina:", 1: "Insira a quantidade de doses recebidas: ", 2: "Insira a data de recebimento: ", 3: "Insira o número de lote: "}
        mensagem_edicao = {0: "Insira a quantidade de doses a somar: ", 1: "Insira a quantidade de doses a retirar: "}
        dados_cadastro = ["nome", "qtd", "data_recebimento", "lote"]
        dados_alteracao = {0: self.pegar_num, 1: self.pegar_num}


        if opcao == 1:
            print(self.colorir_titulo(" ----- CADASTRAR ESTOQUE ----- "))

            lista_dados = list(dados.values())
            dados_estoque = []

            for dado in range(len(lista_dados)):
                dados_estoque.append(lista_dados[dado](mensagem[dado]))
            return dict(zip(dados_cadastro, dados_estoque))

        elif opcao == 2:
            opcao_escolhida = self.mostra_opcao_alterar_quantidade()

            opcoes_mudanca = {0: "qtd_somar", 1: "qtd_subtrair"}

            dado = dados_alteracao[opcao_escolhida](mensagem_edicao[opcao_escolhida])
            self.mostra_resposta_cadastrada()
            return [opcoes_mudanca[opcao_escolhida], int(dado)]

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
        print(self.colorir_info(" Resposta cadastrada com sucesso! "))

    def mostra_mensagem_exclusao(self):
        print(self.colorir_info("ESTOQUE EXCLUÍDO COM SUCESSO!"))
        print(input("Aperte enter para continuar: "))

    def mostra_lote_existente(self):
        print(self.colorir_erro("LOTE JÁ CADASTRADO!"))
        print(input("Aperte enter para continuar: "))

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
        print(self.colorir_erro("LOTE INEXISTENTE!"))
        print(input("Aperte enter para continuar: "))

    def mostra_opcao_busca(self):
        print(" ----- MÉTODO DE BUSCA... -----")
        print("0 - Buscar através de nome")
        print("1 - Buscar através de lote")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [0, 1])

    def mostra_vacinas_insuficientes(self):
        print(self.colorir_erro("NÃO É POSSÍVEL EXCLUIR MAIS VACINAS DO QUE HÁ EM ESTOQUE!"))
