from entidade.enfermeiro import Enfermeiro
from tela.tela_enfermeiro import TelaEnfermeiro
from utils import estilo


class ControladorEnfermeiro:

    def __init__(self, controlador_sistema):
        self.__enfermeiros = []
        self.__tela_enfermeiro = TelaEnfermeiro(self)
        self.__controlador_sistema = controlador_sistema

    def inserir_enfermeiro(self):
        estilo.clear()
        dados_enfermeiro = self.__tela_enfermeiro.pega_dados_enfermeiro(1)
        nao_cadastrado = True

        for enfermeiro in self.__enfermeiros:
            if enfermeiro.coren == dados_enfermeiro["coren"]:
                nao_cadastrado = False

        if nao_cadastrado:
            novo_enfermeiro = Enfermeiro(dados_enfermeiro["nome"], dados_enfermeiro["telefone"], dados_enfermeiro["cpf"], dados_enfermeiro["coren"])
            self.__enfermeiros.append(novo_enfermeiro)
            return novo_enfermeiro
        else:
            estilo.clear()
            self.__tela_enfermeiro.mostra_msg_enfermeiro_cadastro()
            estilo.clear()

    def listar_enfermeiros(self):
        if len(self.__enfermeiros) == 0:
            estilo.clear()
            self.__tela_enfermeiro.mostra_mgs_sem_enfermeiros()
            estilo.clear()
        else:
            estilo.clear()
            self.__tela_enfermeiro.mostra_dados_enfermeiros(self.__enfermeiros)

    def listar_pacientes(self):
        enfermeiro = self.busca_enfermeiro()
        if enfermeiro == None:
            self.__tela_enfermeiro.pega_opcao_enfermeiro_sem_cadastro()
        elif len(enfermeiro.lista_pacientes) == 0:
            self.__tela_enfermeiro.mostra_pacientes(None)
        else:
            self.__tela_enfermeiro.mostra_pacientes(enfermeiro.lista_pacientes)

    def pega_nome_enfermeiro(self):
        estilo.clear()
        nome = self.__tela_enfermeiro.busca_enfermeiro_nome()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.nome == nome:
                return enfermeiro
        return None

    def pega_cpf_enfermeiro(self):
        estilo.clear()
        cpf = self.__tela_enfermeiro.busca_enfermeiro_cpf()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.cpf == cpf:
                return enfermeiro
        return None

    def pega_coren_enfermeiro(self):
        coren = self.__tela_enfermeiro.busca_enfermeiro_coren()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.coren == coren:
                return enfermeiro
        return None

    def busca_enfermeiro(self):
        estilo.clear()
        tipo_busca = self.__tela_enfermeiro.mostra_opcao_busca()
        opcao_busca = {1: self.pega_nome_enfermeiro, 2: self.pega_cpf_enfermeiro, 3: self.pega_coren_enfermeiro}
        enfermeiro_escolhido = opcao_busca[tipo_busca]()
        return enfermeiro_escolhido

    def busca_dado_enfermeiro(self):
        estilo.clear()
        enfermeiro = self.busca_enfermeiro()
        if enfermeiro == None:
            opcao = self.__tela_enfermeiro.pega_opcao_enfermeiro_sem_cadastro()
            if opcao == 1:
                enfermeiro = self.inserir_enfermeiro()
                self.__tela_enfermeiro.mostra_enfermeiro(enfermeiro)
            else:
                self.retornar_sistema()
        else:
            self.__tela_enfermeiro.mostra_enfermeiro(enfermeiro)

    def editar_enfermeiro(self):
        enfermeiro = self.busca_enfermeiro()
        if enfermeiro == None:
            opcao = self.__tela_enfermeiro.pega_opcao_enfermeiro_sem_cadastro()
            if opcao == 1:
                enfermeiro = self.inserir_enfermeiro()
                self.__tela_enfermeiro.mostra_enfermeiro(enfermeiro)
            else:
                self.retornar_sistema()
        else:
            estilo.clear()
            dado_novo = self.__tela_enfermeiro.pega_dados_enfermeiro(2)
            if dado_novo[0] == "nome":
                enfermeiro.nome = dado_novo[1]
            elif dado_novo[0] == "telefone":
                enfermeiro.telefone = dado_novo[1]
            elif dado_novo[0] == "cpf":
                enfermeiro.cpf = dado_novo[1]
            else:
                enfermeiro.coren = dado_novo[1]

    def excluir_enfermeiro(self):
        enfermeiro = self.busca_enfermeiro()
        if enfermeiro == None:
            opcao = self.__tela_enfermeiro.pega_opcao_enfermeiro_sem_cadastro()
            if opcao == 1:
                enfermeiro = self.inserir_enfermeiro()
                self.__tela_enfermeiro.mostra_enfermeiro(enfermeiro)
            else:
                self.retornar_sistema()
        else:
            self.__enfermeiros.remove(enfermeiro)
            self.__tela_enfermeiro.mostra_mensagem_enfermeiro_exlcuido()

    def retornar_sistema(self):
        return self.__controlador_sistema

    def abre_tela(self):
        opcoes = {1: self.inserir_enfermeiro, 2: self.listar_enfermeiros, 3: self.editar_enfermeiro,
                  4: self.excluir_enfermeiro, 5: self.busca_dado_enfermeiro, 6: self.listar_pacientes, 7:self.listar_pacientes, 8: self.retornar_sistema}
        continua = True
        while continua:
            estilo.clear()
            opcao_selecionada = self.__tela_enfermeiro.mostra_opcoes()
            if opcao_selecionada == 8:
                continua = False
            opcoes[opcao_selecionada]()

