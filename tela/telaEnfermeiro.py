from tela.telaAbstrata import AbstractTela


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

        #nome = self.pegar_nome("Insira o nome completo do enfermeiro: ")
        #telefone = self.pegar_telefone("Insira o telefone do enfermeiro: ")
        #cpf = self.pegar_cpf("Insira o cpf do enfermeiro: ")
        #coren = self.pegar_num("Insira o COREN do enfermeiro: ")
        #return {"nome": nome, "telefone": telefone, "cpf": cpf, "coren": coren}

        else:
            print("------ Inserir novo dado para alteração do cadastro --------")
            opcao_escolhida = self.mostra_opcao_alteracao_cadastro()
            opcoes_mudanca = {0: "nome", 1: "telefone", 2: "cpf ", 3: "coren"}
            dado = dados_requeridos[opcao_escolhida](mensagens[opcao_escolhida])
            return [opcoes_mudanca[opcao_escolhida], dado]



    def mostra_dados(self, dados_enfermeiro):
        print("Nome do enfermeiro: ", dados_enfermeiro["nome"])
        print("Telefone do enfermeiro: ", dados_enfermeiro["telefone"])
        print("CPF do enfermeiro: ", dados_enfermeiro["cpf"])
        print("COREN do enfermeiro: ", dados_enfermeiro["coren"] + "\n")

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
        coren = self.pegar_num("Insira o cpf do enfermeiro: ")
        return coren

    def mostra_opcao_alteracao_cadastro(self):
        print("Escolha a opção que você deseja alterar:  ")
        print("0 - alterar o nome do enfermeiro")
        print("1 - alterar o telefone do enfermeiro")
        print("2 - alterar o cpf do enfermeiro")
        print("3 - alterar o COREN do enfermeiro")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [0,1, 2, 3])

    def pega_novos_dados(self, opcao):
        print("------ Inserir novo dado para alteração --------")
        opcoes_mudanca = {1: "nome", 2: "telefone", 3: "cpf ", 4: "coren"}
        print("Insira " + opcoes_mudanca[opcao])
        dado = input()
        return [opcoes_mudanca[opcao], dado]

    def mostra_pacientes(self, dados_enfermeiro):
        print("Nome do paciente: ", dados_enfermeiro["nome"])

