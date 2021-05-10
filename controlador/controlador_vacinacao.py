from controlador import controlador_estoque
from controlador.controlador_agendamento import ControladorAgendamento
from controlador.controlador_estoque import ControladorEstoque
from entidade.paciente import Paciente
from entidade.enfermeiro import Enfermeiro
from entidade.vacinacao import Vacinacao
from excecao.nao_cadastrado import NaoCadastrado
from entidade.vacina import TipoVacina
from utils import estilo
from tela.tela_vacinacao.tela_menu_vacinacao import TelaMenuVacinacao
from tela.tela_vacinacao.tela_registra_vacinacao import TelaRegistraVacinacao
from persistencia.vacinacaoDAO import VacinacaoDAO
from tela.estoque.tela_lista_estoques_compativeis import TelaListaEstoque


class ControladorVacinacao:
    def __init__(self, controlador_sistema):
        self.__tela_menu_vacinacao = TelaMenuVacinacao(self)
        self.__tela_registra_vacinacao = TelaRegistraVacinacao(self)
        self.__tela_lista_estoques_compativeis = TelaListaEstoque(self)
        self.__controlador_agendamento = ControladorAgendamento(self)
        self.__controlador_sistema = controlador_sistema
        self.__vacinacao_dao = VacinacaoDAO()
        self.__vacinacoes = self.__vacinacao_dao.get_all()
        self.__controlador_estoque = ControladorEstoque(self)

    def abre_tela(self):
        opcoes = {1: self.incluir_vacinacao, 2: self.listar_vacinacao, 3: self.buscar_vacinacao_paciente,
                  4: self.retornar_sistema}
        while True:
            button, values = self.__tela_menu_vacinacao.open()
            if button == "Cancel" or button is None:
                break
            else:
                index = 1
                for i in values.values():
                    if i:
                        opcoes[index]()
                    index += 1

    def buscar_vacinacao_paciente(self):
        agendamento = self.__controlador_agendamento.pega_inf_agendamento()
        paciente = agendamento["paciente"]
        if self.__vacinacao_dao.get(paciente.cpf):
            vacinacao = self.__vacinacao_dao.get(paciente.cpf)
            self.__tela_menu_vacinacao.mostra_vacinacao()
        else:
            self.__tela_menu_vacinacao.msg("Vacinacao não encontrada para esse CPF!")


    def incluir_vacinacao(self):
        agendamento = self.__controlador_agendamento.pega_inf_agendamento()
        if agendamento:
            paciente = agendamento["paciente"]
            if self.__vacinacao_dao.get(paciente.cpf):
                #paciente = self.__vacinacao_dao.get(paciente.cpf)
                vacinacao = self.__vacinacao_dao.get(paciente.cpf)
            enfermeiro = agendamento["enfermeiro"]
            if vacinacao.paciente.dose == 0:
                lotes, nomes = self.__controlador_estoque.estoques_disponiveis()
                self.__tela_lista_estoques_compativeis.init_components(lotes, nomes)
                button, values = self.__tela_lista_estoques_compativeis.open()
                self.__tela_lista_estoques_compativeis.close()
                if button == "Submit":
                    for value in values:
                        if value:
                            tipo_dose = value
                            vacinacao.paciente.dose = 1
                            print(vacinacao.paciente.dose)
                            self.__controlador_estoque.vacina(tipo_dose)
                            vacinacao = Vacinacao(paciente, enfermeiro, paciente.dose, tipo_dose)
                            self.__tela_menu_vacinacao.msg("{} recebeu a primeira dose do lote {}!".format(paciente.nome, tipo_dose))
            elif paciente.dose == 1:
                doses_da_vacina = self.__controlador_estoque.pega_doses(paciente.tipo_dose)
                if doses_da_vacina == '2':
                    paciente.dose += 1
                    paciente = self.__vacinacao_dao.get(paciente.cpf)
                    self.__controlador_estoque.vacina(paciente.tipo_dose)
                    vacinacao = Vacinacao(paciente, enfermeiro, paciente.dose, paciente.tipo_dose)
                    self.__vacinacao_dao.add(paciente.cpf, vacinacao)
                    self.__tela_menu_vacinacao.msg("{} recebeu a segunda dose da vacina!".format(paciente.nome))
                else:
                    self.__tela_menu_vacinacao.msg("Não é possível vacinar esse paciente novamente!")
            else:
                self.__tela_menu_vacinacao.msg("Não é possível vacinar esse paciente novamente!")
        self.retornar_sistema()

    def excluir_vacinacao(self, cpf):
        if self.__vacinacao_dao.get(cpf):
            self.__vacinacao_dao.remove(cpf)
            self.__tela_menu_vacinacao.msg("A vacinação referente ao paciente {} foi excluído".format(cpf))

    def listar_vacinacao(self):
        self.__tela_menu_vacinacao.mostra_vacina(self.__vacinacao_dao.get_all())

    def retornar_sistema(self):
        return self.__controlador_sistema



"""    def editar_vacinacao(self, paciente: Paciente, enfermeiro: Enfermeiro, dose, tipo_dose):
        if isinstance(paciente, Paciente):
            self.__paciente = paciente
        else:
            raise NaoCadastrado
        if isinstance(enfermeiro, Enfermeiro):
            self.__enfermeiro = enfermeiro
        else:
            raise NaoCadastrado
        dose_sistema = self.__tela_vacinacao.pegar_dose_vacina(dose)
        if isinstance(tipo_dose, TipoVacina):
            self.__tipo_dose = tipo_dose
        else:
            raise NaoCadastrado
        vacinacao_editada = Vacinacao(paciente, enfermeiro, dose, tipo_dose)
        self.__vacinacao_dao.add(paciente.cpf, vacinacao_editada)"""
