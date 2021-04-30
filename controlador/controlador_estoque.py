from controlador import controlador_sistema
from entidade import estoque
from entidade.estoque import Estoque
from controlador.controlador_tipo_vacina import ControladorTipoVacina
from tela.tela_estoque import TelaEstoque
from entidade.vacina import TipoVacina
from tela.tela_tipo_vacina import TelaTipoVacina

class ControladorEstoque():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_vacina = ControladorTipoVacina
        self.__vacinas_aplicadas = []
        self.__tela_estoque = TelaEstoque(controlador_estoque= ControladorEstoque)
        self.__tela_tipo_vacina = TelaTipoVacina(self)
        self.__estoque = []

    def abre_tela(self):
        opcoes = {1: self.adicionar_estoque, 2: self.editar_estoque, 3: self.listar_vacina, 4: self.buscar_vacina, 5: self.excluir_estoque, 6: self.retornar_sistema}
        continua = True
        while continua:
            opcao_selecionada = self.__tela_estoque.mostra_opcoes()
            if opcao_selecionada == 6:
                continua = False
            opcoes[opcao_selecionada]()

    def adicionar_estoque(self):
        opcao = 1
        controlador_vacina = self.__controlador_sistema.controlador_tipo_vacina
        dados_vacina = self.__tela_estoque.pega_dados_estoque(opcao)
        nao_cadastrado = True
        for tipo_de_vacina in controlador_vacina.tipos_de_vacinas:
            if tipo_de_vacina.nome == dados_vacina["nome"]:
                doses = tipo_de_vacina.num_doses
                nao_cadastrado = False
                novo_registro_estoque = Estoque(dados_vacina["nome"],  doses, dados_vacina["qtd"], dados_vacina['data_recebimento'])
                self.__estoque.append(novo_registro_estoque)
                self.__tela_estoque.mostra_resposta_cadastrada()
        if nao_cadastrado:
            self.__tela_estoque.mostra_vacina_inexistente()
        else:
            print("\n")

    def editar_estoque(self):
        tipo_vacina = self.buscar_vacina_por_nome()
        if tipo_vacina is None:
            self.__tela_estoque.mostra_vacina_inexistente()
        else:
            opcao = 2
            dado_a_editar = self.__tela_estoque.pega_dados_estoque(opcao)
            for vacina in self.__estoque:
                if vacina.nome == tipo_vacina.nome:
                    if dado_a_editar[0] == "qtd_somar":
                        vacina.qtd += int(dado_a_editar[1])
                    elif dado_a_editar[0] == "qtd_subtrair":
                        vacina.qtd -= int(dado_a_editar[1])

    def listar_vacina(self):
        self.__tela_estoque.titulo_busca()
        self.__tela_estoque.mostra_dados(self.__estoque)

    def buscar_vacina(self):
        controlador_vacina = self.__controlador_sistema.controlador_tipo_vacina
        controlador_vacina.buscar_tipo_vacina()

    def listar_vacinas_aplicadas(self):
        return self.__vacinas_aplicadas

    def retornar_sistema(self):
        return self.__controlador_sistema

    def buscar_vacina_por_nome(self):
        controlador_vacina = self.__controlador_sistema.controlador_tipo_vacina
        nome = self.__tela_tipo_vacina.busca_vacina_nome()
        for tipo_de_vacina in controlador_vacina.tipos_de_vacinas:
            if tipo_de_vacina.nome == nome:
                return tipo_de_vacina

    def buscar_tipo_vacina(self):
        tipo_vacina = self.buscar_vacina_por_nome()
        if tipo_vacina == None:
            opcao = self.__tela_tipo_vacina.pega_opcao_tipo_nao_cadastrado()
            if opcao == 1:
                tipo_vacina = self.adicionar_estoque()
                self.__tela_tipo_vacina.mostra_tipo_vacina(tipo_vacina)
            else:
                self.retornar_sistema()
        else:
            self.__tela_estoque.mostra_tipo_vacina(tipo_vacina)

    def excluir_estoque(self):
        tipo_vacina = self.buscar_vacina_por_nome()
        if tipo_vacina is None:
            opcao = self.__tela_estoque.pega_opcao_tipo_nao_cadastrado()
            if opcao == 1:
                self.__tela_estoque.mostra_vacina_inexistente()
                self.retornar_sistema()
        else:
            for vacina in self.__estoque:
                if vacina.nome == tipo_vacina.nome:
                    self.__estoque.remove(vacina)
                    self.__tela_estoque.mostra_mensagem_exclusao()
