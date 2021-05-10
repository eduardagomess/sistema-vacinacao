from tela.tela_abstrata import AbstractTela


class TelaVacinacao(AbstractTela):

    def __init__(self, controlador_sistema):
        super().__init__()
        self.__controlador_sistema = controlador_sistema
        self.__window  = None
        self.mostra_opcoes()

    def mostra_opcoes(self):
        layout = [
            [sg.Radio(())]
        ]

        print(self.colorir_titulo("------ ÁREA DE VACINAS --------"))
        print("Escolha uma das opções abaixo: ")
        print("1 - Incluir vacinação")
        print("2 - Listar vacinações")
        print("4 - Excluir vacinação")
        print("5 - Mostrar situação de vacina do paciente")
        print("6 - Retornar a tela principal do sistema")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5, 6])

    def mostra_opcao_tipo_vacina(self):
        print(self.colorir_titulo("------ TIPO DE VACINA --------"))
        print("Escolha uma das opções abaixo: ")
        print("1 - CoronaVac")
        print("2 - Pfizer")
        opcao  = self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2])
        tipos_vacina = {1: "CoronaVac", 2: "Pfizer"}
        return tipos_vacina[opcao]

    def mostra_vacina(self, vacinacao):
        for vacina in vacinacao:
            print("\nNome do paciente: ", self.colorir_info(vacina.paciente.nome))
            print("Nome do enfermeiro: ", self.colorir_info(vacina.enfermeiro.nome))
            print("Tipo da vacina: ", self.colorir_info(vacina.tipo_dose))
            print("Estágio da dose: ", self.colorir_info(vacina.dose))
        print(input(("\nAperte enter para continuar: ")))

    def mostra_dose_paciente(self, paciente):
        print("\n Nome do paciente: ", self.colorir_info(paciente.nome))
        print("Tipo da vacina: ", self.colorir_info(paciente.tipo_dose))
        print("Estágio da dose: ", self.colorir_info(paciente.dose))
        print(input(("\nAperte enter para continuar: ")))

