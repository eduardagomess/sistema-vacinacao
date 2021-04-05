from tela.tela_abstrata import AbstractTela


class TelaSistema(AbstractTela):

    def __init__(self, controlador_sistema):
        super().__init__()
        self.__controlador_sistema = controlador_sistema

    def mostra_opcoes(self):
        print(self.colorir_titulo("------ SISTEMA DE VACINAÇÃO --------"))
        print("Escolha uma das opções abaixo:")
        print("1 - Área de pacientes")
        print("2 - Área de enfermeiros")
        print("3 - Área de estoque")
        print("4 - Área de prontuários")
        print("5 - Área de agendamentos")
        print("6 - Área de registro de tipo vacina")
        print("7 - Sair do sistema \n")

        opcao = self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5, 6, 7])
        return opcao
