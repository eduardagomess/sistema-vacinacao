class TelaSistema:
    def __init__(self):
        pass

    def mostra_opcoes(self):
        print("------ SISTEMA DE VACINAÇÃO --------")
        print("Escolha uma das opções abaixo:")
        print("1 - Realizar cadastro de pacientes")
        print("2 - Realizar cadastro de enfermeiros ")
        print("3 - Realizar o registro das vacinas e verificar informações sobre o estoque")
        print("4 - Registro referente ao dia em que ocorre a vacinação do paciente")
        print("5 - Realizar agendamento de vacinação")
        print("6 - Sair do sistema \n")
        return int(input("Insira o número da opção escolhida: "))
