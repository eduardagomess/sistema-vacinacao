from tela.tela_abstrata import AbstractTela
import PySimpleGUI as sg


class TelaListaTipoVacina(AbstractTela):

    def __init__(self, controlador_tipo_vacina):
        super().__init__()
        self.__controlador_tipo_vacina = controlador_tipo_vacina
        self.__window = None

#BUG
    def init_components(self, tipo_vacinas):
        tps = []
        for tipo_vacina in tipo_vacinas:
            tp = "A vacina {} requer {} aplicações. ".format(tipo_vacina.nome, tipo_vacina.num_doses) + "\n"
            tps.append(tp)
        sg.Popup("Vacinas encontradas", *tps, title = "Sistema de Posto")
        return list(tps)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def msg(self, msg: str):
        sg.popup_ok(msg)

    def close(self):
        self.__window.Close()

    """       tipos_vacinas = self.mostra_tipo_vacina(tipo_vacinas)
        layout = [
            sg.Text("Vacinas encontradas:"), [
                sg.Text(vacina) for vacina in tipos_vacinas
            ]
        ]
        self.__window = sg.Window('Sistema de Posto').Layout(layout)"""
