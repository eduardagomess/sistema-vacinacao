from controlador.controlador_agendamento import ControladorAgendamento
from controlador.controlador_estoque import ControladorEstoque
from entidade.vacinacao import Vacinacao
from tela.tela_vacinacao.tela_menu_vacinacao import TelaMenuVacinacao
from persistencia.vacinacaoDAO import VacinacaoDAO
from tela.estoque.tela_lista_estoques_compativeis import TelaListaEstoque


class ControladorVacinacao:
    def __init__(self, controlador_sistema):
        self.__tela_menu_vacinacao = TelaMenuVacinacao(self)
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
            self.__tela_menu_vacinacao.mostra_vacinacao(vacinacao)
        else:
            self.__tela_menu_vacinacao.msg("Vacinacao não encontrada para esse CPF")

    def incluir_vacinacao(self):
        agendamento = self.__controlador_agendamento.pega_inf_agendamento()
        if agendamento:
            # OBJETO PACIENTE
            paciente = agendamento["paciente"]
            enfermeiro = agendamento["enfermeiro"]
            segunda_vacinacao = False
            if self.__vacinacao_dao.get(paciente.cpf):
                segunda_vacinacao = self.__vacinacao_dao.get(paciente.cpf)
            if not segunda_vacinacao:
                lotes, nomes = self.__controlador_estoque.estoques_disponiveis()
                self.__tela_lista_estoques_compativeis.init_components(lotes, nomes)
                button, values = self.__tela_lista_estoques_compativeis.open()
                self.__tela_lista_estoques_compativeis.close()
                if button == "Submit":
                    for value in values:
                        if values.values():
                            tipo_dose = value
                            paciente.dose = 1
                            self.__controlador_estoque.vacina(tipo_dose)
                            vacinacao_nova = Vacinacao(paciente, enfermeiro, tipo_dose)
                            self.__controlador_estoque.vacina(tipo_dose)
                            self.__vacinacao_dao.add(paciente.cpf, vacinacao_nova)
                            success = True
                    if success:
                        self.__tela_menu_vacinacao.msg(
                            "{} recebeu a primeira dose do lote {}!".format(paciente.nome, tipo_dose))
            elif segunda_vacinacao:
                doses_da_vacina = self.__controlador_estoque.pega_doses(segunda_vacinacao.tipo_dose)
                if doses_da_vacina == '2' and segunda_vacinacao.paciente.dose < 2:
                    segunda_vacinacao.paciente.dose = 2
                    # diminuindo dose do lote
                    self.__controlador_estoque.vacina(segunda_vacinacao.tipo_dose)
                    vacinacao_nova = Vacinacao(segunda_vacinacao.paciente, segunda_vacinacao.enfermeiro,
                                               segunda_vacinacao.tipo_dose)
                    self.__vacinacao_dao.add(segunda_vacinacao.paciente.cpf, vacinacao_nova)
                    self.__tela_menu_vacinacao.msg(
                        "{} recebeu a segunda dose da vacina!".format(segunda_vacinacao.paciente.nome))
            elif paciente.dose == 1:
                doses_da_vacina = self.__controlador_estoque.pega_doses(paciente.tipo_dose)
                if doses_da_vacina == '2':
                    paciente.dose += 1
                    paciente = self.__vacinacao_dao.get(paciente.cpf)
                    self.__controlador_estoque.vacina(paciente.tipo_dose)
                    vacinacao = Vacinacao(paciente, enfermeiro, paciente.tipo_dose)
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
