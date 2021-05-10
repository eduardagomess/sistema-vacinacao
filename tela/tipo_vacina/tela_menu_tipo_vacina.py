from tela.tela_abstrata import AbstractTela
from utils import estilo
import PySimpleGUI as sg


class TelaMenuTipoVacina(AbstractTela):

    def __init__(self, controlador_tipo_vacina):
        super().__init__()
        self.__controlador_tipo_vacina = controlador_tipo_vacina
        self.__window = None
        self.mostra_opcoes()

    def mostra_opcoes(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Registro de vacina', size=(20, 1), font=("Helvetica", 15))],
            [sg.Radio('Registrar vacina', "AREA", key=1)],
            [sg.Radio('Editar registro de vacina', "AREA", key=2)],
            [sg.Radio('Listar vacinas', "AREA", key=3)],
            [sg.Radio('Buscar registro de uma vacina', "AREA", key=4)],
            [sg.Radio('Excluir registro', "AREA", key=5)],
            [sg.Button('Aplicar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema de Posto').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def msg(self, msg: str):
        sg.popup_ok(msg)

    def mostra_dados(self, tipos_de_vacinas):
        if not tipos_de_vacinas:
            sg.popup_ok("NÃO HÁ VACINAS CADASTRADAS!")
        else:
            for vacina in tipos_de_vacinas:
                sg.Text(("Nome da vacina: {}".format(self.colorir_info(vacina.nome)) +
                         ("Número de aplicações que a vacina requer: {}".format(self.colorir_info(vacina.num_doses)))))

    def mostra_tipo_vacina(self, tipo_vacina):
        self.msg(
            ("Nome da vacina: {}".format(tipo_vacina.nome)) + "\n" + "Número de aplicações que a vacina requer: {}".format(tipo_vacina.num_doses) + "\n")
        return tipo_vacina

    def mostra_vacina_inexistente(self):
        print(self.colorir_erro("ESSA VACINA NÃO FOI ENCONTRADA!"))
        print(input("Aperte enter para continuar: "))

    def mostra_opcao_editar(self):
        print(self.colorir_info(" ----- ALTERAÇÃO DE VACINA ----- "))
        print("Escolha a informação que deseja alterar")
        print("0 - Nome da vacina")
        print("1 - Aplicações que a vacina requer")
        return self.pegar_opcao("Insira o número da opção desejada: ", [0, 1])
