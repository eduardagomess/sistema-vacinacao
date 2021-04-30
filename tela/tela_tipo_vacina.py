from entidade import vacina
from tela.tela_abstrata import AbstractTela
from utils import estilo

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
        print("6 - Fazer alteração de estoque")
        print("7 - Retornar a tela principal do sistema")

        opcao = self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5, 6, 7])
        return opcao

    def pega_dados_vacina(self, opcao):

        dados = {0: self.pegar_nome_vacina, 1: self.pegar_dose_vacina, 2: self.pegar_num}
        mensagem = {0: "Insira o nome da vacina:", 1: "Insira a quantidade de aplicações que a vacina requer: ", 2: "Insira a quantidade de doses recebidas: "}
        mensagem_edicao = {0: "Insira o novo nome da vacina:", 1: "Insira a nova quantidade de aplicações que a vacina requer: "}
        dados_alteracao = {0: self.pegar_num, 1: self.pegar_num}
        mensagem_alteracao = {0: "Insira a quantidade de doses a serem adicionadas ao sistema: ", 1: "Insira a quantidade de doses a serem retiradas do sistema: "}
        dados_cadastro = ["nome", "num_doses", "qtd"]

        if opcao == 1:
            print(self.colorir_titulo(" ----- CADASTRAR VACINA ----- "))

            lista_dados = list(dados.values())
            dados_vacina = []

            for dado in range(len(lista_dados)):
                dados_vacina.append(lista_dados[dado](mensagem[dado]))
            return dict(zip(dados_cadastro, dados_vacina))

        elif opcao == 2:
            opcao_escolhida  = self.mostra_opcao_editar()

            opcoes_mudanca = {0: "nome", 1: "num_doses", 2: "qtd_somar", 3: "qtd_subtrair"}

            dado = dados[opcao_escolhida](mensagem_edicao[opcao_escolhida])
            return [opcoes_mudanca[opcao_escolhida], str(dado)]

        elif opcao == 6:
            opcao_escolhida = self.mostra_opcao_alterar_quantidade()

            opcoes_mudanca = {0: "qtd_somar", 1: "qtd_subtrair"}

            dado = dados_alteracao[opcao_escolhida](mensagem_alteracao[opcao_escolhida])
            return [opcoes_mudanca[opcao_escolhida], int(dado)]


    def mostra_vacina_cadastrada(self):
        print(self.colorir_info("ESTA VACINA JÁ ESTÁ CADASTRADA!"))
        print(input("Aperte enter para continuar: "))

    def busca_vacina_nome(self):
        print(self.colorir_info("----- BUSCANDO VACINA ATRAVÉS DO NOME... -----"))
        return self.pegar_nome_vacina("Insira o nome da vacina que você procura: ")

    def mostra_dados(self, tipos_de_vacinas):
        if tipos_de_vacinas == []:
            print(self.colorir_erro("NÃO HÁ VACINAS CADASTRADAS!"))
            print(input("Aperte enter para continuar: "))
        else:
            for vacina in tipos_de_vacinas:
                print("Nome da vacina: {}".format(self.colorir_info(vacina.nome)))
                print("Número de aplicações que a vacina requer: {}".format(self.colorir_info(vacina.num_doses)))
                print("Número de doses em estoque: {}".format(self.colorir_info(vacina.qtd)))

    def mostra_opcao_busca(self):
        print(self.colorir_titulo(" ----- OPÇÃO DE BUSCA DE VACINA ----- "))
        print("1 - buscar por nome")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1])

    def pega_opcao_tipo_nao_cadastrado(self):
        print(self.colorir_erro("VACINA NÃO CADASTRADA!"))
        print(self.colorir_info("Escolha uma das opções abaixo: "))
        print("1 - Cadastrar vacina")
        print("2 - Retornar à tela principal")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2])

    def mostra_tipo_vacina(self, tipo_vacina):
        print("Nome da vacina: {}".format(self.colorir_info(tipo_vacina.nome)))
        print("Número de aplicações que a vacina requer: {}".format(self.colorir_info(tipo_vacina.num_doses)))
        print("Número de doses em estoque: {}".format(self.colorir_info(tipo_vacina.qtd)))

    def titulo_busca(self):
        print(self.colorir_info(" ----- VACINAS ENCONTRADAS -----  \n"))

    def mostra_mensagem_exclusao(self):
        print(self.colorir_info("VACINA EXCLUÍDA COM SUCESSO!"))
        print(input("Aperte enter para continuar: "))

    def mostra_vacina_inexistente(self):
        print(self.colorir_erro("ESSA VACINA NÃO FOI ENCONTRADA!"))
        print(input("Aperte enter para continuar: "))

    def mostra_opcao_editar(self):
        print(self.colorir_info(" ----- ALTERAÇÃO DE VACINA ----- "))
        print("Escolha a informação que deseja alterar")
        print("0 - Nome da vacina")
        print("1 - Aplicações que a vacina requer")
        return self.pegar_opcao("Insira o número da opção desejada: ", [0, 1])

    def mostra_resposta_cadastrada(self):
        print(self.colorir_info(" Resposta cadastrada com sucesso! "))

    def mostra_opcao_alterar_quantidade(self):
        print(self.colorir_info(" ----- ALTERAÇÃO DE ESTOQUE ----- "))
        print("Escolha a informação que deseja alterar")
        print("0 - Adicionar doss ao sistema")
        print("1 - Retirar doses do estoque")
        return self.pegar_opcao("Insira o número da opção desejada: ", [0, 1])
