class TelaPaciente:

    def mostra_opcoes(self):
        print("------ CADASTRO DE PACIENTES --------")
        print("Escolha uma das opções abaixo: ")
        print("1 - Incluir paciente")
        print("2 - Listar pacientes")
        print("3 - Alterar informações do paciente")
        print("4 - Excluir pacientes")
        print("5 - Buscar paciente ")
        print("6 - Retornar a tela principal do sistema")

        return int(input("Insira o número da opção escolhida: "))

    def pega_dados_paciente(self):
        print("------ CADASTRAMENTO DO PACIENTE ------")
        nome = input("Insira o nome completo do paciente: ")
        telefone = input("Insira o telefone do paciente ( dd-xxxxxxxxxx): ")
        cpf = int(input("Insira o cpf do paciente: "))
        endereco = input("Insira o endereço do paciente: ")
        data_nascimento = int(input("Insira a data de nascimento do paciente: "))
        dose = int(input("Insira em qual estágio da dose o paciente está (0 - 1 - 2): "))

        return {"nome": nome, "telefone": telefone, "cpf":cpf, "endereco": endereco, "data_nascimento": data_nascimento, "dose": dose}

    def mostra_dados(self, dados_paciente):
        print("Nome do paciente: ",dados_paciente["nome"])
        print("Telefone do paciente: ", dados_paciente["telefone"])
        print("CPF do paciente: ", dados_paciente["cpf"])
        print("Endereço do paciente: ", dados_paciente["endereco"])
        print("Data de nascimento do paciente: ", dados_paciente["data_nascimento"])
        print("O paciente está no estãgio ", str(dados_paciente["dose"]) + " da dose")

    def mostra_opcao_alteracao_cadastro(self):
        print("------ ALTAREÇÃO DE CADASTRO --------")
        print("Escolha a opção que você deseja alterar:  ")
        print("1 - alterar o nome do paciente")
        print("2 - alterar o telefone do paciente")
        print("3 - alterar o cpf do paciente")
        print("4 - alterar o endereço do paciente")
        print("5 - alterar a data de nascimento do paciente")
        print("6 - alterar o estágio da dose do paciente")
        return int(input("Insira o número da opção escolhida: "))

    def pega_novos_dados(self, opcao):
        print("------ Inserir novo dado para alteração --------")
        opcoes_mudanca = {1: "nome", 2: "telefone", 3: "cpf ", 4: "endereco", 5: "data_nascimento", 6: "estagio_dose"}
        print("Insira " + opcoes_mudanca[opcao])
        dado = input()
        return [opcoes_mudanca[opcao],dado]

    def mostra_opcao_busca(self):
        print("------ opcao busca ----------")
        print("1 - busca pelo nome")
        print("2 - busca pelo cpf")
        opcao = int(input("insira a opcao:"))
        return opcao

    def busca_paciente_nome(self):
        nome = input("Insira o nome do paciente: ")
        return nome

    def busca_paciente_cpf(self):
        cpf = int(input("Insira o cpf do paciente: "))
        return cpf
