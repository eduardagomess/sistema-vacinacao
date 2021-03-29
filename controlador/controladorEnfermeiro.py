from entidade.enfermeiro import Enfermeiro
from tela.telaEnfermeiro import TelaEnfermeiro
from utils import estilo

class ControladorEnfermeiro:

    def __init__(self, controlador_sistema):
        self.__enfermeiros = []
        self.__tela_enfermeiro = TelaEnfermeiro()
        self.__controlador_sistema = controlador_sistema
        self.__lista_pacientes = []

    def inserir_enfermeiro(self):
        estilo.clear()
        dados_enfermeiro = self.__tela_enfermeiro.pega_dados_enfermeiro()
        enfermeiro = Enfermeiro(dados_enfermeiro["nome"], dados_enfermeiro["telefone"], dados_enfermeiro["cpf"],dados_enfermeiro["coren"])
        self.__enfermeiros.append(enfermeiro)

    def listar_enfermeiros(self):
        for enfermeiro in self.__enfermeiros:
            self.__tela_enfermeiro.mostra_dados({"nome": enfermeiro.nome, "telefone": enfermeiro.telefone, "cpf": enfermeiro.cpf, "coren": enfermeiro.coren})

    def listar_pacientes(self):
        enfermeiro = self.busca_enfermeiro()
        for paciente in enfermeiro.lista_pacientes:
            self.__tela_enfermeiro.mostra_pacientes({"nome": paciente.nome, "cpf": paciente.cpf})


    def pega_nome_enfermeiro(self):
        nome = self.__tela_enfermeiro.busca_enfermeiro_nome()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.nome == nome:
                return enfermeiro

    def pega_cpf_enfermeiro(self):
        cpf = self.__tela_enfermeiro.busca_enfermeiro_cpf()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.cpf == cpf:
                return enfermeiro

    def pega_coren_enfermeiro(self):
        coren = self.__tela_enfermeiro.busca_enfermeiro_cpf()
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
        self.__tela_enfermeiro.mostra_dados({"nome": enfermeiro.nome, "telefone": enfermeiro.telefone, "cpf": enfermeiro.cpf, "coren": enfermeiro.coren})

    def editar_enfermeiro(self):
        enfermeiro = self.busca_enfermeiro()
        tipo_de_alteracao = self.__tela_enfermeiro.mostra_opcao_alteracao_cadastro()
        dado_novo = self.__tela_enfermeiro.pega_novos_dados(tipo_de_alteracao)

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

