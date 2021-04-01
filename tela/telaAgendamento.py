from tela.telaAbstrata import AbstractTela

class TelaAgendamento(AbstractTela):

    def __init__(self, controlador_sistema):
        super().__init__()
        self.__controlador_sistema = controlador_sistema

    def mostra_opcoes(self):
        print("------ AGENDAMENTOS--------")
        print("Escolha a opção que você deseja alterar:  ")
        print("1 - inserir agendamento")
        print("2 - editar agendamento")
        print("3 - excluir agendamento")
        print("4 - listar agendamentos")
        print("5 - retornar_sistema")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5])

    def pegar_dados_agendamento(self):
        print("---------AGENDAMENTO--------")
        print("Escolha a opção que referente ao dia da vacina:  ")
        print("1 - segunda")
        print("2 - terça")
        print("3 - quarta")
        print("4 - quinta")
        print("5 - sexta")
        dia = {1: "segunda", 2: "terça", 3: "quarta", 4: "quinta", 5: "sexta"}
        opcao = int(input("Insira o número da opção escolhida: "))

        print("Escolha um dos horario abaixo  ")
        print(" 8:00", "8:15", "8:30", "8:45", "9", "9:15", "9:30", "9:45", "10:00", "10:15", "10:30", "10:45", "11\n","11:15", "11:30", "11:45", "12", "12:15", "12:30", "12:45", "13", \
        "13:15", "13:30", "13:45", "14\n", "14:15", "14:30", "14:45", "13", "13:15", "13:30", "13:45", "14", "14:15", "14:30", "14:45", "15\n", "15:15", "15:30", "15:45", "16", \
        "16:15", "16:30", "16:45", "17", "17:15", "17:30", "17:45", "18")

        hora = input("Insira a hora escolhida: ")
        return [dia[opcao], hora]

    def mostra_dados(self, dados):
        print("Nome do paciente: ",dados["paciente"])
        print("Informações agendamento: ", "A vacina está marcada para " + dados["agendamento"][0] + " as " + dados["agendamento"][1])
        print("Nome do Enfermeiro(a): ", dados["enfermeiro"])

    def mostra_msg_paciente_nao_castrado(self):
        print("PACIENTE NÃO ENCONTRADO, POR FAVOR, REALIZE O CADASTRO")

    def mostra_msg_enfermeiro_nao_castrado(self):
        print("ENFERMEIRO NÃO ENCONTRADO, POR FAVOR, REALIZE O CADASTRO")

    def mostra_opcao_alteracao(self):
        print("------ ALTAREÇÃO DE ANGENDAMENTO --------")
        print("Escolha a opção que você deseja alterar:  ")
        print("1 - alterar o dia da vacinação")
        print("2 - alterar o horario da vacinação")
        print("3 - alterar o dia e a horario da vacinação")
        print("4 - alterar o enfermeiro")
        return int(input("Insira o número da opção escolhida: "))

    def pega_novos_dados(self, opcao):
        print("------ Inserir novo dado para alteração do agendamento --------")
        opcoes_mudanca = {1: "dia", 2: "hora", 3: "dia e hora", 4: "enfermeiro"}
        if opcao == 4:
            return opcoes_mudanca[opcao]
        else:
            print("Insira " + opcoes_mudanca[opcao])
            dado = input()
            return [opcoes_mudanca[opcao], dado]


