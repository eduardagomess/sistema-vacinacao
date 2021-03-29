from tela.telaAgendamento import TelaAgendamento
from entidade.agendamento import Agendamento
from utils import estilo
from entidade.paciente import Paciente
from entidade.enfermeiro import Enfermeiro

class ControladorAgendamento:

    def __init__(self, controlador_sistema):
        self.__agenda = []
        self.__agendamentos = {}
        self.__tela_agendamento = TelaAgendamento()
        self.__controlador_sistema = controlador_sistema

    def pega_nome_paciente(self):
        nome = self.__tela_agendamento.paciente_nome()
        return nome

    def pega_cpf_paciente(self):
        cpf = self.__tela_agendamento.paciente_cpf()
        return cpf

    def informacao_paciente(self):
        estilo.clear()
        tipo_busca = self.__tela_agendamento.mostra_opcao_busca()
        opcao_busca = {1: [self.pega_nome_paciente, "nome"], 2: [self.pega_cpf_paciente, "cpf"]}
        paciente_escolhido = opcao_busca[tipo_busca][0]()
        return [paciente_escolhido, opcao_busca[tipo_busca][1]]


    def verificar_cadastro_nome(self):
        estilo.clear()
        dado_paciente = self.informacao_paciente()
        dado = dado_paciente[0]
        tipo_dado = dado_paciente[1]

        if tipo_dado == "nome":
            for paciente in Paciente.lista_pecientes:
                if paciente.nome == dado:
                    return True
        else:
            for paciente in Paciente.lista_pecientes:
                if paciente.cpf == dado:
                    return True


    def verificar_cadastro_cpf(self):
        pass
    def inserir_agendamento(self):
        pass


    def abre_tela(self):
        opcoes = {1: self.inserir_agendamento, 2: self.editar_agendamento, 3: self.excluir_agendamento, 4: self.excluir_paciente, 5: self.listar_agendamentos, 6: self.retornar_sistema}
        continua = True
        while continua:
            estilo.clear()
            opcao_selecionada = self.__tela_agendamento.mostra_opcoes()
            if opcao_selecionada == 6:
                continua = False
            opcoes[opcao_selecionada]()


