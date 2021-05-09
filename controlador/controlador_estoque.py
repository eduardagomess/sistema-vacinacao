from entidade.estoque import Estoque
from controlador.controlador_tipo_vacina import ControladorTipoVacina
from entidade.vacina import TipoVacina
from datetime import datetime
from tela.estoque.tela_busca_estoque import TelaBuscaEstoque
from tela.estoque.tela_lista_estoque import TelaListaEstoque
from tela.estoque.tela_registro_estoque import TelaCadastraEstoque
from tela.estoque.tela_menu_estoque import TelaMenuEstoque
from tela.estoque.tela_edita_estoque import TelaEditaEstoque


class ControladorEstoque:

    def __init__(self, controlador_sistema):
        self.__tela_menu_estoque = TelaMenuEstoque(self)
        self.__tela_registro_estoque = TelaCadastraEstoque(self)
        self.__tela_busca_estoque = TelaBuscaEstoque(self)
        self.__tela_edita_estoque = TelaEditaEstoque(self)
        self.__tela_lista_estoque = TelaListaEstoque(self)
        self.__controlador_sistema = controlador_sistema
        self.__controlador_vacina = ControladorTipoVacina
        self.__vacinas_aplicadas = []
        self.__estoque = [Estoque(TipoVacina('Pfizer', 2), 2000, datetime(year=1999, month=7, day=3), 'Lll001')]

    def abre_tela(self):
        opcoes = {1: self.adicionar_estoque, 2: self.editar_estoque, 3: self.listar_vacina,
                  4: self.buscar_estoque, 5: self.excluir_estoque, 6: self.retornar_sistema}
        while True:
            button, values = self.__tela_menu_estoque.open()
            if button == "Cancel" or button is None:
                break
            else:
                index = 1
                for i in values.values():
                    if i:
                        if index == 1:
                            opcoes[index](None, None, None, None)
                        elif (index == 4 or index == 3) and self.__estoque == []:
                            self.__tela_menu_estoque.msg("Não há vacinas cadastradas!")
                        elif index == 4:
                            opcoes[index](1)
                        else:
                            opcoes[index]()
                    index += 1

    def adicionar_estoque(self, nome, qtd, data_recebimento, lote):
        self.__tela_registro_estoque.input_estoque(nome, qtd, data_recebimento, lote)
        controlador_vacina = self.__controlador_sistema.controlador_tipo_vacina
        button, dados_vacina = self.__tela_registro_estoque.open()
        if button == "Submit":
            tipo_vacina = controlador_vacina.busca_vacina(dados_vacina["nome"].title())
            self.__tela_registro_estoque.close()
            if tipo_vacina is None:
                self.__tela_menu_estoque.msg(
                    "Essa vacina não foi cadastrada no sistema! \n Cadastre-a antes de incluir estoque.")
                self.__tela_registro_estoque.close()
            else:
                # dados vacina opassa como parametro pra outro metodo do tipovacina
                nome = self.__tela_menu_estoque.pegar_nome_vacina(dados_vacina["nome"])
                qtd = self.__tela_menu_estoque.pegar_quantidade(dados_vacina['qtd'])
                data_recebimento = self.__tela_menu_estoque.pegar_data_nascimento(dados_vacina['data_recebimento'])
                lote = self.__tela_menu_estoque.pegar_nome_vacina(dados_vacina['lote'])
                self.__tela_registro_estoque.close()
                cadastrado = False
                if nome and qtd and data_recebimento and lote:
                    for estoque in self.__estoque:
                        if estoque.lote == lote and estoque.tipo_vacina.nome == nome:
                            self.__tela_menu_estoque.msg("Esse estoque já está cadastrado para essa vacina!")
                            self.__tela_menu_estoque.close()
                            cadastrado = True
                    if self.__estoque == [] or not cadastrado:
                        novo_registro_estoque = Estoque(tipo_vacina, qtd, data_recebimento, lote)
                        self.__estoque.append(novo_registro_estoque)
                        self.__tela_registro_estoque.close()
                        self.__tela_registro_estoque.msg("Estoque registrado com sucesso!")
        else:
            self.__tela_registro_estoque.close()

#editar_estoque com bug quando botao = cancel/none, ou apos rodar outra função
    def editar_estoque(self):
        button, estoque_por_lote = self.buscar_estoque(2)
        if estoque_por_lote and button == "Submit":
            self.__tela_edita_estoque.mostra_opcao_alterar_quantidade()
            button, dado_a_editar = self.__tela_edita_estoque.open()
            self.__tela_edita_estoque.close()
            sucesso = False
            for estoque in self.__estoque:
                if estoque.tipo_vacina.nome == estoque_por_lote.tipo_vacina.nome:
                    if dado_a_editar[0]:
                        estoque.qtd += int(dado_a_editar[2])
                        sucesso = True
                    elif dado_a_editar[1]:
                        if int(dado_a_editar[2]) > estoque.qtd:
                            self.__tela_menu_estoque.msg("NÃO É POSSÍVEL EXCLUIR MAIS VACINAS DO QUE HÁ EM ESTOQUE!")
                        else:
                            estoque.qtd -= int(dado_a_editar[2])
                            sucesso = True
                if sucesso:
                    self.__tela_menu_estoque.msg("Alteração aplicada! Atual quantidade de {}, lote {}: {}".format(
                        estoque.tipo_vacina.nome, estoque.lote, estoque.qtd))
        else:
            self.retornar_sistema()

    def listar_vacina(self):
        if not self.__estoque:
            self.__tela_menu_estoque.msg("Não há estoque cadastrado!")
        else:
            self.__tela_menu_estoque.lista_estoque(self.__estoque)

    def listar_vacinas_aplicadas(self):
        return self.__vacinas_aplicadas

    def retornar_sistema(self):
        return self.__controlador_sistema

    def buscar_estoque(self, opcao):
        button, valores = self.__tela_busca_estoque.open()
        if button == "Submit":
            estoque_por_nome = self.buscar_estoque_por_nome(valores)
            estoque_por_lote = self.buscar_estoque_por_lote(valores)
            self.__tela_busca_estoque.close()
            if not valores[0] and not valores[1]:
                self.__tela_menu_estoque.msg("Você deve selecionar uma das opções.")
                self.buscar_estoque(opcao)
            elif estoque_por_nome:
                nome_valido = self.__tela_menu_estoque.pegar_nome_vacina(estoque_por_nome.tipo_vacina.nome)
                if nome_valido and opcao == 1:
                    self.__tela_menu_estoque.mostra_dados_estoque(estoque_por_nome)
                elif nome_valido and opcao == 2:
                    return button, estoque_por_nome
            elif estoque_por_lote:
                lote_valido = self.__tela_menu_estoque.pegar_nome_vacina(estoque_por_lote.lote)
                if lote_valido and opcao == 1:
                    self.__tela_menu_estoque.mostra_dados_estoque(estoque_por_lote)
                elif lote_valido and opcao == 2:
                    return button, estoque_por_lote

    def buscar_estoque_por_nome(self, valores):
        for estoque in self.__estoque:
            if estoque.tipo_vacina.nome == valores['nome']:
                return estoque
            else:
                return False

    def buscar_estoque_por_lote(self, valores):
        for estoque in self.__estoque:
            if estoque.lote == valores[1]:
                return estoque
            else:
                return False

    def excluir_estoque(self):
        estoque_por_lote = self.buscar_estoque(2)
        if estoque_por_lote is None:
            self.__tela_menu_estoque.msg("LOTE INEXISTENTE!")
        else:
            for estoque in self.__estoque:
                if estoque_por_lote.tipo_vacina.nome == estoque.tipo_vacina.nome:
                    self.__estoque.remove(estoque)
                    self.__tela_busca_estoque.close()
                    self.__tela_menu_estoque.msg("ESTOQUE EXCLUÍDO COM SUCESSO!")

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
