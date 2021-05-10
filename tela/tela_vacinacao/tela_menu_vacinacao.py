from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg


class TelaMenuVacinacao(AbstractTela):

    def __init__(self, controlador_sistema):
        super().__init__()
        self.__controlador_sistema = controlador_sistema
        self.__window = None
        self.mostra_opcoes()

    def mostra_opcoes(self):
        layout = [
            [sg.Text('Tela de vacinações', size=(20, 1), font=("Helvetica", 15))],
            [sg.Radio('Registrar vacinacação', "AREA", key=1)],
            [sg.Radio('Listar vacinacações', "AREA", key=2)],
            [sg.Radio('Mostrar a vacinacao de um paciente', "AREA", key =3)],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Tela da vacinações').Layout(layout)

    def mostra_opcao_tipo_vacina(self):
        print(self.colorir_titulo("------ TIPO DE VACINA --------"))
        print("Escolha uma das opções abaixo: ")
        print("1 - CoronaVac")
        print("2 - Pfizer")
        opcao = self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2])
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
