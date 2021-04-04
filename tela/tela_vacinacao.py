from tela.tela_abstrata import AbstractTela


class TelaVacinacao(AbstractTela):

    def __init__(self, controlador_sistema):
        super().__init__()
        self.__controlador_sistema = controlador_sistema


    def mostra_opcoes(self):
        print(self.titulo("------ ÁREA DE VACINAS --------"))
        print("Escolha uma das opções abaixo: ")
        print("1 - Incluir vacina")
        print("2 - Listar vacinas")
        print("3 - Editar vacina")
        print("4 - Excluir vacina")
        print("5 - Retornar a tela principal do sistema")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5])
