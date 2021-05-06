from entidade.estoque import Estoque
from controlador.controlador_tipo_vacina import ControladorTipoVacina
from tela.estoque.tela_busca_estoque import TelaBuscaEstoque
from tela.estoque.tela_registro_estoque import TelaCadastraEstoque
from tela.estoque.tela_menu_estoque import TelaMenuEstoque
from tela.tipo_vacina.tela_menu_tipo_vacina import TelaMenuTipoVacina


class ControladorEstoque:

    def __init__(self, controlador_sistema):
        self.__tela_menu_estoque = TelaMenuEstoque(self)
        self.__tela_registro_estoque = TelaCadastraEstoque(self)
        self.__tela_busca_estoque = TelaBuscaEstoque(self)
        self.__controlador_sistema = controlador_sistema
        self.__controlador_vacina = ControladorTipoVacina
        self.__vacinas_aplicadas = []
        self.__tela_tipo_vacina = TelaMenuTipoVacina(self)
        self.__estoque = []

    def abre_tela(self):
        opcoes = {1: self.adicionar_estoque, 2: self.editar_estoque, 3: self.listar_vacina,
                  4: self.buscar_vacina_por_nome, 5: self.excluir_estoque, 6: self.retornar_sistema}
        while True:
            button, values = self.__tela_menu_estoque.open()
            if button == "Sair" or button is None:
                self.finaliza_sistema()
            else:
                count = 1
                for i in values.values():
                    if i:
                        opcoes[count]()
                    count += 1

    def adicionar_estoque(self):
        self.__tela_registro_estoque.input_estoque()
        controlador_vacina = self.__controlador_sistema.controlador_tipo_vacina
        dados_vacina = self.__tela_registro_estoque.open()
        nao_cadastrado = True
        if nao_cadastrado:
            self.__tela_menu_estoque.msg("ESSA VACINA NÃO FOI ENCONTRADA! \n Cadastre-a primeiro!")
        for tipo_de_vacina in controlador_vacina.tipos_de_vacinas:
            if tipo_de_vacina.nome == dados_vacina["nome"]:
                nao_cadastrado = False
                novo_registro_estoque = Estoque(dados_vacina["nome"], dados_vacina["qtd"],
                                                dados_vacina['data_recebimento'], dados_vacina['lote'])
                self.__estoque.append(novo_registro_estoque)
                self.__tela_menu_estoque.mostra_resposta_cadastrada()
        else:
            print("\n")

    def editar_estoque(self):
        lote = self.buscar_vacina_por_lote()
        if lote is None:
            self.__tela_menu_estoque.msg("LOTE JÁ CADASTRADO!")
        else:
            opcao = 2
            dado_a_editar = self.__tela_acoes_estoque.input_estoque()
            for vacina in self.__estoque:
                if vacina.nome == lote.nome:
                    if dado_a_editar[0] == "qtd_somar":
                        vacina.qtd += int(dado_a_editar[1])
                    elif dado_a_editar[0] == "qtd_subtrair":
                        if int(dado_a_editar[1]) > vacina.qtd:
                            self.__tela_menu_estoque.msg("NÃO É POSSÍVEL EXCLUIR MAIS VACINAS DO QUE HÁ EM ESTOQUE!")
                        else:
                            vacina.qtd -= int(dado_a_editar[1])

    def listar_vacina(self):
        self.__tela_menu_estoque.mostra_dados(self.__estoque)

    def listar_vacinas_aplicadas(self):
        return self.__vacinas_aplicadas

    def retornar_sistema(self):
        return self.__controlador_sistema

    def buscar_vacina_por_nome(self):
        nome = self.__tela_busca_estoque.open()
        for vacina in self.__estoque:
            if vacina.nome == nome:
                self.__tela_menu_estoque.mostra_dados_vacina(vacina)

    # BUG
    def buscar_vacina_por_lote(self):
        lote = self.__tela_busca_estoque.open()
        for estoque in self.__estoque:
            if estoque.lote == lote:
                return estoque

    def excluir_estoque(self):
        lote = self.buscar_vacina_por_lote()
        if lote is None:
            self.__tela_menu_estoque.msg("LOTE INEXISTENTE!")
        else:
            for estoque in self.__estoque:
                if lote.nome == estoque.nome:
                    self.__estoque.remove(estoque)
                    self.__tela_menu_estoque.mostra_mensagem_exclusao()

    def pega_vacina_nome(self):
        nome = self.__tela_busca_estoque.open()
        for estoque in self.__estoque:
            if estoque.tipo_vacina.nome == nome:
                return estoque
        return None

    def pega_vacina_lote(self):
        lote = self.__tela_busca_estoque.open().title()
        for estoque in self.__estoque:
            if estoque.lote == lote:
                return estoque
        return None

    def finaliza_sistema(self):
        exit(0)
