import PySimpleGUI as sg


class TelaInicial:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('BluePurple')
        layout = [[sg.Text('Sistema de Vacinação:'), sg.Text(size=(15, 1), font='Helvetica')],
                  [sg.Radio('Área de pacientes', "AREA", key=1), sg.Radio('Área de enfermeiros', "AREA", key='2'),
                   sg.Radio('Área de estoque', "AREA", key='3'), sg.Radio('Área de prontuários', "AREA", key='4'),
                   sg.Radio('Área de agendamentos', "AREA", key='5'),
                   sg.Radio('Área de registro de vacinas', "AREA", key=6)],
                  [sg.Button('Aplicar'), sg.Button('Sair')]]

        self.__window = sg.Window("Tela inicial").layout(layout)

    def open(self):
        button, values = self.__window.Read()
        print(values)
        return button, values

    def close(self):
        self.__window.Close()

    def msg(self, msg: str):
        self.__window.MsgBoxOK(msg)


#Essa tela substitui a tela_sistema. Copiar código do init componentes e jogar no mostra_opcoes.
#1 - janelas diferentes ficam em arquivos diferentes? para msgs simples nao, mas p cada nova entidade pelo menos um arquivo
#3 - onde o singleton entraria nesse projeto? Controlador sistema. Não é obrigatório.
#4 - tipo_vacina precisa de registro? como acessaria?
#todos os daos *podem* ser singletons
#sistemas multiusuários tipicamente têm controladores singletons (flask)
