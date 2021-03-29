class TelaAgendamento:

    def __init__(self):
        pass

    def mostra_opcoes(self):
        print("------ AGENDAMENTOS--------")

    def mostra_opcao_busca(self):
        print("------ opcao busca ----------")
        print("1 - busca pelo nome")
        print("2 - busca pelo cpf")
        opcao = int(input("insira a opcao:"))
        return opcao

    def paciente_nome(self):
        nome = input("Insira o nome do paciente: ")
        return nome

    def paciente_cpf(self):
        cpf = int(input("Insira o cpf do paciente: "))
        return cpf




    def inserir_agendamento(self):
        pass

    def editar_agendamento(self):
        pass

    def excluir_agendamento(self):
        pass

    def listar_agendamentos(self):
        pass
