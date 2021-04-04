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
        print("5 - Mostrar situação de vacina do pacientee")
        print("6 - Retornar a tela principal do sistema")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5, 6])

    def mostra_opcao_tipo_vacina(self):
        print(self.titulo("------ TIPO DE VACINA --------"))
        print("Escolha uma das opções abaixo: ")
        print("1 - CoronaVac")
        print("2 - Pfizer")
        opcao  = self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2])
        tipos_vacina = {1: "CoronaVac", 2: "Pfizer"}
        return tipos_vacina[opcao]

    def mostra_vacina(self, vacinacao):
        for vacina in vacinacao:
            print("\nNome do paciente: ", self.info(vacina.paciente.nome))
            print("Nome do enfermeiro: ", self.info(vacina.enfermeiro.nome))
            print("Tipo da vacina: ", self.info(vacina.tipo_dose))
            print("Estágio da dose: ", self.info(vacina.dose))
        print(input(("\nAperte enter para continuar: ")))

    def mostra_dose_paciente(self, paciente):
        print("\n Nome do paciente: ", self.info(paciente.nome))
        print("Tipo da vacina: ", self.info(paciente.tipo_dose))
        print("Estágio da dose: ", self.info(paciente.dose))
        print(input(("\nAperte enter para continuar: ")))

