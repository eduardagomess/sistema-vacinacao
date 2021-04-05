from tela.tela_abstrata import AbstractTela


class TelaTipoVacina(AbstractTela):

    def __init__(self, controlador_tipo_vacina):
        super().__init__()
        self.__controlador_tipo_vacina = controlador_tipo_vacina

    def mostra_opcoes(self):
        print(self.colorir_titulo("------ ÁREA DE INSERÇÃO DE TIPO DE VACINAS --------"))
        print("Escolha uma das opções abaixo:")
        print("1 - Incluir tipo de vacina")
        print("2 - Editar tipo de vacina")
        print("3 - Listar tipo de vacina")
        print("4 - Buscar tipo de vacina")
        print("5 - Excluir tipo de vacina")
        print("6 - Retornar a tela principal do sistema")

        opcao = self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5, 6])
        return opcao
