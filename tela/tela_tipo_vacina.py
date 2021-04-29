from tela.tela_abstrata import AbstractTela


class TelaTipoVacina(AbstractTela):

    def __init__(self, controlador_tipo_vacina):
        super().__init__()
        self.__controlador_tipo_vacina = controlador_tipo_vacina

    def mostra_opcoes(self):
        print(self.colorir_titulo("------ ÁREA DE INSERÇÃO DE TIPO DE VACINAS --------"))
        print("Escolha uma das opções abaixo:")
        print("1 - Incluir tipo de vacina")
        print("2 - Editar tipo de vacina")
        print("3 - Listar tipo de vacina")
        print("4 - Buscar tipo de vacina")
        print("5 - Excluir tipo de vacina")
        print("6 - Retornar a tela principal do sistema")

        opcao = self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5, 6])
        return opcao

    def pega_dados_vacina(self, opcao):

        dados = {0: self.pegar_nome, 1: self.pegar_num}
        mensagem = {0: "Insira o nome da vacina:", 1: "Insira a quantidade de doses com que a vacina trabalha: "}
        dados_cadastro = ["nome", "num_doses"]

        if opcao == 1:
            print(self.colorir_titulo(" ----- CADASTRAR VACINA ----- "))
            lista_dados = list(dados.values())
            dados_vacina = []

            for dado in range(len(lista_dados)):
                dados_vacina.append(lista_dados[dado](mensagem[dado]))
            return dict(zip(dados_cadastro, dados_vacina))

        elif opcao == 2:
            opcao_escolhida  = self.mostra_opcao_editar()
            opcoes_mudanca = {0: "nome", 1: "num_doses"}

            dado = dados[opcao_escolhida](mensagem[opcao_escolhida])
            return [opcoes_mudanca[opcao_escolhida], dado]

    def mostra_vacina_cadastrada(self):
        print(self.colorir_info("ESTA VACINA JÁ ESTÁ CADASTRADA!"))
        print(input("Aperte enter para continuar: "))

    def busca_vacina_nome(self):
        return self.pegar_nome("Insira o nome da vacina: ")

    def busca_vacina_qtd_dose(self):
        return self.pegar_num("Insira o número de doses desejadas: ")

    def mostra_dados(self, tipos_de_vacinas):
        if tipos_de_vacinas == []:
            print(self.colorir_erro("NÃO HÁ VACINAS CADASTRADAS!"))
            print(input("Aperte enter para continuar: "))
        else:
            for vacina in tipos_de_vacinas:
                print("\nNome da vacina: {}".format(self.pegar_nome(vacina.nome)))
                print("Número de doses da vacina: {}".format(self.pegar_num(vacina.num_doses)))

    def mostra_opcao_busca(self):
        print(self.colorir_titulo(" ----- OPÇÃO DE BUSCA DE VACINA ----- "))
        print("1 - buscar por nome")
        print("2 - buscar por número de doses")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2])

    def pega_opcao_tipo_nao_cadastrado(self):
        print(self.colorir_erro("VACINA NÃO CADASTRADA"))
        print(self.colorir_info("Escolha uma das opções abaixo: "))
        print("1 - Cadastrar vacina")
        print("2 - Retornar à tela principal")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2])

    def mostra_tipo_vacina(self, tipo_vacina):
        pass

    def mostra_mensagem_exclusao(self):
        print(self.colorir_info(("VACINA EXCLUÍDA COM SUCESSO!")))
        print(input("Aperte enter para continuar: "))

    def mostra_vacina_inexistente(self):
        print(self.colorir_erro("ESSA VACINA NÃO FOI ENCONTRADA!"))
        print(input("Aperte enter para continuar: "))

    def mostra_opcao_editar(self):
        print(self.colorir_info(" ----- ALTERAÇÃO DE VACINA ----- "))
        print("Escolha a opção que deseja alterar")
        print("1 - Nome da vacina")
        print("2 - Doses a serem tomadas da vacina")
        return self.pegar_opcao("Insira o número da opção desejada: ", [1, 2])
