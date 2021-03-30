class TelaAgendamento:

    def __init__(self):
        pass

    def mostra_opcoes(self):
        print("------ AGENDAMENTOS--------")
        print("Escolha a opção que você deseja alterar:  ")
        print("1 - inserir agendamento")
        print("2 - editar agendamento")
        print("3 - excluir agendamento")
        print("4 - listar agendamentos")
        print("5 - retornar_sistema")
        return int(input("Insira o número da opção escolhida: "))


    def pegar_dados_agendamento(self):
        print("---------AGENDAMENTO--------")
        print("Escolha a opção que referente ao dia da vacina:  ")
        print("1 - segunda")
        print("2 - terça")
        print("3 - quarta")
        print("4 - quinta")
        print("5 - sexta")
        dia = input("Insira o número da opção escolhida: ")
        print("Escolha um dos horario abaixo  ")
        print("8", "8:15", "8:30", "8:45", "9", "9:15", "9:30", "9:45", "10", "10:15", "10:30", "10:45", "11", "11:15", "11:30", "11:45", "12", "12:15", "12:30", "12:45", "13", \
        "13:15", "13:30", "13:45", "14", "14:15", "14:30", "14:45", "13", "13:15", "13:30", "13:45", "14", "14:15", "14:30", "14:45", "15", "15:15", "15:30", "15:45", "16", \
        "16:15", "16:30", "16:45", "17", "17:15", "17:30", "17:45", "18")
        hora = input("Insira a hora escolhida: ")
        return [dia, hora]

    def mostra_dados(self, dados):
        print("Nome do paciente: ",dados["paciente"])
        print("Informações agendamento: ", "A vacina está marcada para " + dados["agendamento"][0] + " as " + dados["agendamento"][1])
        print("Nome do Enfermeiro(a): ", dados["enfermeiro"])

    def mostra_msg_paciente_nao_castrado(self):
        print("PACIENTE NÃO ENCONTRADO, POR FAVOR, REALIZE O CADASTRO")

    def mostra_msg_enfermeiro_nao_castrado(self):
        print("PACIENTE NÃO ENCONTRADO, POR FAVOR, REALIZE O CADASTRO")

    def editar_agendamento(self):
        pass

    def excluir_agendamento(self):
        pass

    def listar_agendamentos(self):
        pass
