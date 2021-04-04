from tela.tela_abstrata import AbstractTela


class TelaEnfermeiro(AbstractTela):

    def __init__(self, controlador_sistema):
        super().__init__()
        self.__controlador_sistema = controlador_sistema

    def mostra_opcoes(self):
        print(self.titulo("------ ÁREA DE ENFERMEIROS --------"))
        print("Escolha uma das opções abaixo: ")
        print("1 - Incluir enfermeiro")
        print("2 - Listar enfermeiros")
        print("3 - Alterar informações do enfermeiro")
        print("4 - Excluir enfermeiro")
        print("5 - Buscar enfermeiro")
        print("6 - Buscar pacientes do enfermeiro")
        print("7 - Retornar a tela principal do sistema")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5, 6, 7])

    def pega_dados_enfermeiro(self, opcao):

        dados_requeridos = {0: self.pegar_nome, 1: self.pegar_telefone, 2: self.pegar_cpf, 3: self.pegar_num}

        mensagens = {0: "Insira o nome do enfermeiro: ", 1: "Insira o telefone do enfermeiro: ",
                     2: "Insira o cpf do enfermeiro: ", 3: "Insira o COREN do enfermeiro: "}

        dados_cadastro = ["nome", "telefone", "cpf", "coren"]

        if opcao == 1:
            print(" ---- CADASTRAR ENFERMEIRO ----")
            lista_dados_requeridos = list(dados_requeridos.values())
            dados_enfermeiro = []
            for dado in range(len(lista_dados_requeridos)):
                dados_enfermeiro.append(lista_dados_requeridos[dado](mensagens[dado]))
            return dict(zip(dados_cadastro, dados_enfermeiro))
        else:
            print("------ Inserir novo dado para alteração do cadastro --------")
            opcao_escolhida = self.mostra_opcao_alteracao_cadastro()
            opcoes_mudanca = {0: "nome", 1: "telefone", 2: "cpf ", 3: "coren"}
            dado = dados_requeridos[opcao_escolhida](mensagens[opcao_escolhida])
            return [opcoes_mudanca[opcao_escolhida], dado]

    def mostra_dados_enfermeiros(self, lista_enfermeiros):
        for enfermeiro in lista_enfermeiros:
            print("Nome do enfermeiro: ", self.info(enfermeiro.nome))
            print("Telefone do enfermeiro: ", self.info(enfermeiro.telefone))
            print("CPF do enfermeiro: ", self.info(enfermeiro.cpf))
            print("COREN do enfermeiro: ", self.info(str(enfermeiro.coren)) + "\n")
        print(input(("\nAperte enter para continuar: ")))

    def mostra_enfermeiro(self, enfermeiro):
        print("\nNome do enfermeiro: ", self.info(enfermeiro.nome))
        print("Telefone do enfermeiro: ", self.info(enfermeiro.telefone))
        print("CPF do enfermeiro: ", self.info(enfermeiro.cpf))
        print("COREN do enfermeiro: ", self.info(str(enfermeiro.coren)))
        print(input(("\nAperte enter para continuar: ")))

    def mostra_opcao_busca(self):
        print("------ OPÇÃO DE BUSCA DO ENFERMEIRO ----------")
        print("1 - buscar pelo nome")
        print("2 - buscar pelo cpf")
        print("3 - buscar pelo COREN")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3])

    def busca_enfermeiro_nome(self):
        nome = self.pegar_nome("Insira o nome do enfermeiro: ")
        return nome

    def busca_enfermeiro_cpf(self):
        cpf = self.pegar_cpf("Insira o cpf do enfermeiro: ")
        return cpf

    def busca_enfermeiro_coren(self):
        coren = self.pegar_num("Insira o COREN do enfermeiro: ")
        return int(coren)

    def mostra_opcao_alteracao_cadastro(self):
        print("Escolha a opção que você deseja alterar:  ")
        print("0 - alterar o nome do enfermeiro")
        print("1 - alterar o telefone do enfermeiro")
        print("2 - alterar o cpf do enfermeiro")
        print("3 - alterar o COREN do enfermeiro")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [0,1, 2, 3])

    def mostra_pacientes(self, pacientes):
        if pacientes == None:
            print(self.erro("Ainda não há pacientes atendidos pelo enfermeiro"))
        else:
            for paciente in pacientes:
                print("Nome do paciente: ", self.info(paciente.nome))
                print("Nome do paciente: ", self.info(paciente.cpf))
        print(input(("\nAperte enter para continuar: ")))


