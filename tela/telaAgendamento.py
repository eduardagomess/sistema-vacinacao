from tela.telaAbstrata import AbstractTela


class TelaAgendamento(AbstractTela):

    def __init__(self, controlador_sistema):
        super().__init__()
        self.__controlador_sistema = controlador_sistema

    def mostra_opcoes(self):
        print(self.titulo("------ AGENDAMENTOS--------"))
        print("Escolha a opção que você deseja alterar:  ")
        print("1 - inserir agendamento")
        print("2 - editar agendamento")
        print("3 - excluir agendamento")
        print("4 - listar agendamentos")
        print("5 - retornar_sistema")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5])

    def pegar_dados_agendamento(self, agenda):
        print(self.titulo("---------AGENDAMENTO--------"))
        print("Escolha a opção que referente ao dia da vacina:  ")
        print("1 - segunda")
        print("2 - terça")
        print("3 - quarta")
        print("4 - quinta")
        print("5 - sexta")

        dia = {1: "segunda", 2: "terca", 3: "quarta", 4: "quinta", 5: "sexta"}
        opcao = int(self.pegar_num("Insira o número da opção escolhida: "))
        horarios_preenchidos = agenda[dia[opcao].title()]

        horarios = [{0: "8:00"}, {1: "8:15"}, {2: "8:30"}, {3: "8:45"}, {4: "9"}, {5: "9:15"}, {6: "9:30"},
                             {7: "9:45"}, {8: "10:00"}, {9: "10:15"}, {10: "10:30"}, {11: "10:45"}, {12: "11:00"},
                             {13: "11:15"}, {14: "11:30"}, {15: "11:45"},{16: "12:00"}, {17: "12:15"}, {18: "12:30"},
                             {19: "12:45"}, {20: "13:00"}, {21: "13:15"}, {22: "13:30"}, {23: "13:45"}, {24: "14:00"},
                             {25: "14:15"}, {26: "14:30"}, {27: "14:45"},{28: "15:00"}, {29: "15:15"}, {30: "15:30"},
                             {31: "15:45"}, {32: "16:00"}, {33: "17:15"},{34: "17:30"}, {35: "17:45"}, {36: "18:00"}]

        horarios_disponiveis = []
        for item in range(len(horarios)):
            horarios_disponiveis.append(horarios[item][item])

        for horario in horarios_preenchidos:
            if horario in horarios_disponiveis:
                horarios_disponiveis.remove(horario)

        count = 0
        identificador = 0
        for horario_disponivel in horarios_disponiveis:
            if count % 10 == 0:
                print(f'{self.info(f"({identificador})")} {horario_disponivel}', end=" ")
            else:
                print(f'{self.info(f"({identificador})")}  {horario_disponivel}', end=" ")
            identificador += 1
            count += 1
        hora = int(self.pegar_num("Insira o numero referente a hora escolhida: "))
        return [dia[opcao], horarios_disponiveis[hora]]


    def mostra_dados(self, dados):
        print("Nome do paciente: ", dados["paciente"])
        print("Informações agendamento: ",
              "A vacina está marcada para " + dados["agendamento"][0] + " as " + dados["agendamento"][1])
        print("Nome do Enfermeiro(a): ", dados["enfermeiro"])

    def mostra_msg_paciente_nao_castrado(self):
        print(self.erro("PACIENTE NÃO ENCONTRADO, POR FAVOR, REALIZE O CADASTRO"))

    def mostra_msg_enfermeiro_nao_castrado(self):
        print(self.erro("ENFERMEIRO NÃO ENCONTRADO, POR FAVOR, REALIZE O CADASTRO"))

    def mostra_opcao_alteracao(self):
        print(self.titulo("------ ALTAREÇÃO DE ANGENDAMENTO --------"))
        print("Escolha a opção que você deseja alterar:  ")
        print("1 - alterar o dia da vacinação")
        print("2 - alterar o horario da vacinação")
        print("3 - alterar o dia e a horario da vacinação")
        print("4 - alterar o enfermeiro")
        return int(input("Insira o número da opção escolhida: "))

    def pega_novos_dados(self, opcao):
        print(self.titulo("------ Inserir novo dado para alteração do agendamento --------"))
        opcoes_mudanca = {1: "dia", 2: "hora", 3: "dia e hora", 4: "enfermeiro"}
        if opcao == 4:
            return opcoes_mudanca[opcao]
        else:
            print("Insira " + opcoes_mudanca[opcao])
            dado = input()
            return [opcoes_mudanca[opcao], dado]
