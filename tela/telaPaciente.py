import time
from tela.telaAbstrata import AbstractTela


class TelaPaciente(AbstractTela):

    def __init__(self, controlador_sistema):
        super().__init__()
        self.__controlador_sistema = controlador_sistema

    def mostra_opcoes(self):
        print("------ ÁREA DE PACIENTES --------")
        print("Escolha uma das opções abaixo: ")
        print("1 - Incluir paciente")
        print("2 - Listar pacientes")
        print("3 - Alterar informações do paciente")
        print("4 - Excluir pacientes")
        print("5 - Buscar paciente")
        print("6 - Retornar a tela principal do sistema")

        opcao = self.verifica_num("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5,6])
        return opcao

    def pega_dados_paciente(self):
        print(" ---- CADASTRADO DE PACIENTES  ----")

        nome = input("Insira o nome completo do paciente: ").replace(" ", "")
        while not nome.isalpha():
            self.excecao(" ----- CAMPO NOME DEVE CONTER APENAS LETRAS -----").replace(" ", "")
            time.sleep(1)
            nome = input("Insira novamente o nome completo do paciente: ")

        telefone = input("Insira o telefone do paciente ( ddxxxxxxxxxx): ")
        while not telefone.isdigit():
            self.excecao("----- CAMPO TELEFONE DEVE CONTER APENAS NUMEROS ------")
            time.sleep(1)
            telefone = input("Insira novamente o telefone do paciente ( ddxxxxxxxxxx): ")

        cpf = input("Insira o cpf do paciente: ")
        while not cpf.isdigit():
            self.excecao(" ----- CAMPO CPF DEVE CONTER APENAS NUMEROS -----")
            time.sleep(1)
            cpf = input("Insira novamente o cpf do paciente: ")

        endereco = input("Insira  endereço do paciente: ")

        data_nascimento =  input("Insira a data de nascimento do paciente (DD/MM/AAAA): ")


        dose = input("Insira em qual estágio da dose o paciente está (0 - 1 - 2): ")
        while dose not in ["0", "1", "2"]:
            self.excecao(" ---- CAMPO DOSE DEVE SER UM NÚMERO ENTRE 0 E 2 ----")
            dose = input("Insira novamente em qual estágio da dose o paciente está (0 - 1 - 2): ")
        return {"nome": nome, "telefone": telefone, "cpf":cpf, "endereco": endereco, "data_nascimento": data_nascimento, "dose": dose}

    def mostra_dados(self, dados_paciente):
        print("Nome do paciente: ",dados_paciente["nome"])
        print("Telefone do paciente: ", dados_paciente["telefone"])
        print("CPF do paciente: ", dados_paciente["cpf"])
        print("Endereço do paciente: ", dados_paciente["endereco"])
        print("Data de nascimento do paciente: ", dados_paciente["data_nascimento"])
        print("O paciente está no estãgio ", str(dados_paciente["dose"]) + " da dose")

    def mostra_opcao_alteracao_cadastro(self):
        print("------ ALTAREÇÃO DE CADASTRO DO PACIENTE --------")
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
        return [opcoes_mudanca[opcao], dado]

    def mostra_opcao_busca(self):
        print("------ OPÇÃO DE BUSCA DE PACIENTE ----------")
        print("1 - buscar pelo nome do paciente")
        print("2 - busca pelo cpf do paciente")
        opcao = int(input("insira a opção:"))
        return opcao

    def busca_paciente_nome(self):
        return input("Insira o nome do paciente: ")

    def busca_paciente_cpf(self):
        return int(input("Insira o cpf do paciente: "))

    def excecao(self, mensagem):
        print(mensagem)