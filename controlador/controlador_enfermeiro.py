from entidade.enfermeiro import Enfermeiro
from tela.tela_enfermeiro import TelaEnfermeiro
from utils import estilo
from utils.faker.Enfermeiro import fakeEnfermeiro
from utils.faker.Enfermeiro import fakeEnfermeiro2
from utils.faker.Enfermeiro import fakeEnfermeiro3

class ControladorEnfermeiro:

    def __init__(self, controlador_sistema):
        self.__enfermeiros = [fakeEnfermeiro, fakeEnfermeiro2, fakeEnfermeiro3]
        self.__tela_enfermeiro = TelaEnfermeiro(self)
        self.__controlador_sistema = controlador_sistema

    def inserir_enfermeiro(self):
        estilo.clear()
        dados_enfermeiro = self.__tela_enfermeiro.pega_dados_enfermeiro(1)
        enfermeiro = Enfermeiro(dados_enfermeiro["nome"], dados_enfermeiro["telefone"], dados_enfermeiro["cpf"], dados_enfermeiro["coren"])
        if enfermeiro not in self.__enfermeiros:
            self.__enfermeiros.append(enfermeiro)
            return enfermeiro

    def listar_enfermeiros(self):
        self.__tela_enfermeiro.mostra_dados_enfermeiros(self.__enfermeiros)

    def listar_pacientes(self):
        enfermeiro = self.busca_enfermeiro()
        if len(enfermeiro.lista_pacientes) == 0:
            self.__tela_enfermeiro.mostra_pacientes(None)
        else:
            self.__tela_enfermeiro.mostra_pacientes(enfermeiro.lista_pacientes)


    def pega_nome_enfermeiro(self):
        estilo.clear()
        nome = self.__tela_enfermeiro.busca_enfermeiro_nome()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.nome == nome:
                return enfermeiro

    def pega_cpf_enfermeiro(self):
        estilo.clear()
        cpf = self.__tela_enfermeiro.busca_enfermeiro_cpf()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.cpf == cpf:
                return enfermeiro

    def pega_coren_enfermeiro(self):
        coren = self.__tela_enfermeiro.busca_enfermeiro_coren()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.coren == coren:
                return enfermeiro

    def busca_enfermeiro(self):
        estilo.clear()
        tipo_busca = self.__tela_enfermeiro.mostra_opcao_busca()
        opcao_busca = {1: self.pega_nome_enfermeiro, 2: self.pega_cpf_enfermeiro, 3: self.pega_coren_enfermeiro}
        enfermeiro_escolhido = opcao_busca[tipo_busca]()
        return enfermeiro_escolhido

    def busca_dado_enfermeiro(self):
        estilo.clear()
        enfermeiro = self.busca_enfermeiro()
        self.__tela_enfermeiro.mostra_enfermeiro(enfermeiro)

    def editar_enfermeiro(self):
        enfermeiro = self.busca_enfermeiro()
        dado_novo = self.__tela_enfermeiro.pega_dados_enfermeiro(2)

        if dado_novo[0] == "nome":
            enfermeiro.nome = dado_novo[1]
        elif dado_novo[0] == "telefone":
            enfermeiro.telefone = dado_novo[1]
        elif dado_novo[0] == "cpf":
            enfermeiro.cpf = dado_novo[1]
        enfermeiro.dose = dado_novo[1]

    def excluir_enfermeiro(self):
        enfermeiro = self.busca_enfermeiro()
        self.__enfermeiros.remove(enfermeiro)

    def retornar_sistema(self):
        return self.__controlador_sistema

    def abre_tela(self):
        opcoes = {1: self.inserir_enfermeiro, 2: self.listar_enfermeiros, 3: self.editar_enfermeiro,
                  4: self.excluir_enfermeiro, 5: self.busca_dado_enfermeiro, 6: self.listar_pacientes, 7: self.retornar_sistema}
        continua = True
        while continua:
            estilo.clear()
            opcao_selecionada = self.__tela_enfermeiro.mostra_opcoes()
            if opcao_selecionada == 7:
                continua = False
            opcoes[opcao_selecionada]()

