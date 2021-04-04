from entidade.vacinacao import Vacinacao
from entidade.paciente import Paciente
from entidade.enfermeiro import Enfermeiro
from excecao.nao_cadastrado import NaoCadastrado
from utils import estilo
from tela.tela_vacinacao import TelaVacinacao


class ControladorVacinacao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_vacinacao = TelaVacinacao(self)
        self.__vacinacoes = []

    def abre_tela(self):
        opcoes = {1: self.incluir_vacinacao, 2: self.listar_vacinacao, 3: self.editar_vacinacao,
                  4: self.excluir_vacinacao, 5: self.mostrar_vacinacao_paciente, 6: self.retornar_sistema}
        continua = True
        while continua:
            estilo.clear()
            opcao_selecionada = self.__tela_vacinacao.mostra_opcoes()
            if opcao_selecionada == 6:
                continua = False
            opcoes[opcao_selecionada]()

    def mostrar_vacinacao_paciente(self):
        agendamento = self.__controlador_sistema.controlador_agendamento.buscar_agendamento()
        paciente = agendamento["paciente"]
        self.__tela_vacinacao.mostra_dose_paciente(paciente)

    def editar_vacinacao(self, paciente: Paciente, enfermeiro: Enfermeiro, dose, tipo_dose):
        if isinstance(paciente, Paciente):
            self.__paciente = paciente
        else:
            raise NaoCadastrado
        if isinstance(enfermeiro, Enfermeiro):
            self.__enfermeiro = enfermeiro
        else:
            raise NaoCadastrado

    def incluir_vacinacao(self):
        agendamento = self.__controlador_sistema.controlador_agendamento.buscar_agendamento()
        paciente = agendamento["paciente"]
        enfermeiro = agendamento["enfermeiro"]
        if paciente.dose == 0:
            paciente.dose = 1
        elif paciente.dose == 1:
            paciente.dose = 2
        tipo_dose = self.__tela_vacinacao.mostra_opcao_tipo_vacina()
        paciente.tipo_dose = tipo_dose
        vacina = Vacinacao(id, paciente, enfermeiro, paciente.dose, tipo_dose)
        self.__vacinacoes.append(vacina)

    def excluir_vacinacao(self, id):
        for vacina in self.__vacinacoes:
            if vacina.id == id:
                self.__vacinacoes.remove(vacina)
        return "A vacinação referente ao id {} foi excluído".format(id)

    def listar_vacinacao(self):
        self.__tela_vacinacao.mostra_vacina(self.__vacinacoes)

    def retornar_sistema(self):
        return self.__controlador_sistema
