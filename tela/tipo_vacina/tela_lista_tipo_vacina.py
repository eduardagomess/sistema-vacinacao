from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg


class TelaListaTipoVacina(AbstractTela):

    def __init__(self, controlador_tipo_vacina):
        super().__init__()
        self.__controlador_tipo_vacina = controlador_tipo_vacina
        self.__window = None
        tipo_vacinas = []
        self.init_components(tipo_vacinas)

    def init_components(self, tipo_vacinas):
        tipos_vacinas = self.mostra_tipo_vacina(tipo_vacinas)
        layout = [
            sg.Text("Vacinas encontradas:"), [
                sg.Text(vacina) for vacina in tipos_vacinas
            ]
        ]
        self.__window = sg.Window('Sistema de Posto').Layout(layout)

    def mostra_tipo_vacina(self, tipo_vacinas):
        tps = []
        for tipo_vacina in tipo_vacinas:
            tp = "Nome da vacina: {}".format(tipo_vacina.nome) + "Número de aplicações que a vacina requer: {}".format(
                tipo_vacina.num_doses) + "\n"
            tps.append(tp)
        return list(tps)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def msg(self, msg: str):
        sg.popup_ok(msg)
