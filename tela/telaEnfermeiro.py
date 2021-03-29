class TelaEnfermeiro:
    def __init__(self):
        pass

    def mostra_opcoes(self):
        print("------ CADASTRO DE ENFERMEIROS --------")
        print("Escolha uma das opções abaixo: ")
        print("1 - Incluir enfermeiro")
        print("2 - Listar enfermeiros")
        print("3 - Alterar informações do enfermeiro")
        print("4 - Excluir enfermeiro")
        print("5 - Buscar enfermeiro")
        print("6 - Buscar pacientes do enfermeiro")
        print("7 - Retornar a tela principal do sistema")

        return int(input("Insira o número da opção escolhida: "))

    def pega_dados_enfermeiro(self):
        print("------ CADASTRAMENTO DE ENFERMEIROS ------")
        nome = input("Insira o nome completo do enfermeiro: ")
        telefone = input("Insira o telefone do enfermeiro ( dd-xxxxxxxxxx): ")
        cpf = int(input("Insira o cpf do enfermeiro: "))
        coren = input("Insira o COREN do enfermeiro: ")

        return {"nome": nome, "telefone": telefone, "cpf":cpf, "coren": coren}

    def mostra_dados(self, dados_enfermeiro):
        print("Nome do enfermeiro: ",dados_enfermeiro["nome"])
        print("Telefone do enfermeiro: ", dados_enfermeiro["telefone"])
        print("CPF do enfermeiro: ", dados_enfermeiro["cpf"])
        print("COREN do enfermeiro: ", dados_enfermeiro["coren"] + "\n")

    def mostra_opcao_busca(self):
        print("------ Opção de busca ----------")
        print("1 - buscar pelo nome")
        print("2 - buscar pelo cpf")
        print("3 - buscar pelo COREN")
        opcao = int(input("insira a opcao:"))
        return opcao

    def busca_enfermeiro_nome(self):
        nome = input("Insira o nome do enfermeiro: ")
        return nome

    def busca_enfermeiro_cpf(self):
        cpf = int(input("Insira o cpf do enfermeiro: "))
        return cpf

    def busca_enfermeiro_coren(self):
        coren = int(input("Insira o cpf do enfermeiro: "))
        return coren

    def mostra_opcao_alteracao_cadastro(self):
        print("------ ALTAREÇÃO DE CADASTRO --------")
        print("Escolha a opção que você deseja alterar:  ")
        print("1 - alterar o nome do enfermeiro")
        print("2 - alterar o telefone do enfermeiro")
        print("3 - alterar o cpf do enfermeiro")
        print("4 - alterar o COREN do enfermeiro")
        return int(input("Insira o número da opção escolhida: "))

    def pega_novos_dados(self, opcao):
        print("------ Inserir novo dado para alteração --------")
        opcoes_mudanca = {1: "nome", 2: "telefone", 3: "cpf ", 4: "coren"}
        print("Insira " + opcoes_mudanca[opcao])
        dado = input()
        return [opcoes_mudanca[opcao], dado]

    def mostra_pacientes(self, dados_enfermeiro):
        print("Nome do paciente: ",dados_enfermeiro["nome"])


