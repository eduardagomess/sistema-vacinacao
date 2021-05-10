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

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_vacina(self, vacinacao):
        vacinacoes = []
        for vacinado in vacinacao:
            registro_vacina = "Paciente {} foi vacinado por enfermeiro(a) {}, tem a {} dose do lote {}. \n".format(vacinado.paciente.nome, vacinado.enfermeiro.nome,
                                                                                                                   vacinado.paciente.dose, vacinado.tipo_dose)
            vacinacoes.append(registro_vacina)
        sg.popup("Registros encontrados: \n", *vacinacoes, title="Sistema de Posto")
        return vacinacoes

    def mostra_vacinacao(self, vacinacao):
        sg.popup("Paciente {} foi vacinado por enfermeiro(a) {}, tem a {} dose do lote {}. \n".format(vacinacao.paciente.nome, vacinacao.enfermeiro.nome,
                                                                                                                   vacinacao.paciente.dose, vacinacao.tipo_dose))
