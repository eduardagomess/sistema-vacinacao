class TelaSistema:
    def __init__(self):
        pass

    def mostra_opcoes(self):
        print("------ SISTEMA DE VACINAÇÃO --------")
        print("Escolha uma das opções abaixo:")
        print("1 - Realizar cadastro de pacientes")
        print("1 - Realizar cadastro de enfermeiros ")
        print("2 - Realizar o registro das vacinas e verificar informações sobre o estoque")
        print("3 - Registro referente ao dia em que ocorre a vacinação do paciente")
        print("4 - Realizar agendamento de vacinação")
        print("5 - Sair do sistema \n")
        return int(input("Insira o número da opção escolhida: "))
