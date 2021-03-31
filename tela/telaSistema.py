class TelaSistema:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def mostra_opcoes(self):
        print("------ SISTEMA DE VACINAÇÃO --------")
        print("Escolha uma das opções abaixo:")
        print("1 - Área de pacientes")
        print("2 - Área de enfermeiros")
        print("3 - Área de vacinas")
        print("4 - Área de prontuário")
        print("5 - Área de agendamentos")
        print("6 - Sair do sistema \n")
        return int(input("Insira o número da opção escolhida: "))
