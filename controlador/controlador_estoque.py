from entidade.estoque import Estoque
from controlador.controlador_tipo_vacina import ControladorTipoVacina
from entidade.vacina import TipoVacina
from datetime import datetime
from tela.estoque.tela_busca_estoque import TelaBuscaEstoque
from tela.estoque.tela_lista_estoques_compativeis import TelaListaEstoque
from tela.estoque.tela_registro_estoque import TelaCadastraEstoque
from tela.estoque.tela_menu_estoque import TelaMenuEstoque
from tela.estoque.tela_edita_estoque import TelaEditaEstoque
from persistencia.estoqueDAO import EstoqueDAO


class ControladorEstoque:

    def __init__(self, controlador_sistema):
        self.__tela_lista_estoques_compativeis = TelaListaEstoque(self)
        self.__tela_menu_estoque = TelaMenuEstoque(self)
        self.__tela_registro_estoque = TelaCadastraEstoque(self)
        self.__tela_busca_estoque = TelaBuscaEstoque(self)
        self.__tela_edita_estoque = TelaEditaEstoque(self)
        self.__controlador_sistema = controlador_sistema
        self.__controlador_vacina = ControladorTipoVacina
        self.__vacinas_aplicadas = []
        self.__estoque_dao = EstoqueDAO()
        # self.__estoque = self.__estoque_dao.get_all()

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
                        elif (index == 4 or index == 3) and not self.__estoque_dao.get_all():
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
            else:
                # dados vacina passa como parametro pra outro metodo do tipovacina
                nome = self.__tela_menu_estoque.pegar_nome_vacina(dados_vacina["nome"])
                qtd = self.__tela_menu_estoque.pegar_quantidade(dados_vacina['qtd'])
                data_recebimento = self.__tela_menu_estoque.pegar_data_nascimento(dados_vacina['data_recebimento'])
                lote = self.__tela_menu_estoque.pegar_nome_vacina(dados_vacina['lote'])
                if nome and qtd and data_recebimento and lote:
                    if self.__estoque_dao.get(lote):
                        self.__tela_menu_estoque.msg("Esse estoque já está cadastrado para essa vacina!")
                        self.__tela_menu_estoque.close()
                    elif not self.__estoque_dao.get(lote) or not self.__estoque_dao.get_all():
                        novo_registro_estoque = Estoque(tipo_vacina, qtd, data_recebimento, lote)
                        self.__estoque_dao.add(lote, novo_registro_estoque)
                        self.__tela_registro_estoque.close()
                        self.__tela_registro_estoque.msg("Estoque registrado com sucesso!")
        else:
            self.__tela_registro_estoque.close()


    def editar_estoque(self):
        button, estoque, vazio = self.buscar_estoque(2)
        if estoque and button == "Submit":
            self.__tela_edita_estoque.mostra_opcao_alterar_quantidade()
            button, dado_a_editar = self.__tela_edita_estoque.open()
            qtd_valida = self.__tela_menu_estoque.pegar_quantidade(dado_a_editar[2])
            self.__tela_edita_estoque.close()
            sucesso = False
            print(button, dado_a_editar, qtd_valida)
            if qtd_valida and (dado_a_editar[0] or dado_a_editar[1]):
                if dado_a_editar[0]:
                    print('ok')
                    estoque.qtd += int(dado_a_editar[2])
                    self.__estoque_dao.add(estoque.lote, estoque)
                    self.__tela_edita_estoque.close()
                    sucesso = True
                elif dado_a_editar[1]:
                    if int(dado_a_editar[2]) > estoque.qtd:
                        self.__tela_menu_estoque.msg(
                            "NÃO É POSSÍVEL EXCLUIR MAIS VACINAS DO QUE HÁ EM ESTOQUE!")
                    else:
                        estoque.qtd -= int(dado_a_editar[2])
                        self.__estoque_dao.add(estoque.lote, estoque)
                        self.__tela_edita_estoque.close()
                        sucesso = True
                if sucesso:
                    self.__tela_menu_estoque.msg("Alteração aplicada! Atual quantidade de {}, lote {}: {}".format(
                        estoque.tipo_vacina.nome, estoque.lote, estoque.qtd))
        self.__tela_edita_estoque.close()
        self.retornar_sistema()

    def listar_vacina(self):
        self.__tela_menu_estoque.lista_estoque(self.__estoque_dao.get_all())

    def listar_vacinas_aplicadas(self):
        return self.__vacinas_aplicadas

    def registra_vacina_aplicada(self):
        pass

    def retornar_sistema(self):
        return self.__controlador_sistema

    def buscar_estoque(self, opcao):
        self.__tela_busca_estoque.init_components()
        button, valores = self.__tela_busca_estoque.open()
        if button == "Submit" and valores:
            if not valores[0] and not valores[1]:
                self.__tela_menu_estoque.msg("Você deve selecionar uma das opções.")
                self.__tela_busca_estoque.close()
                self.buscar_estoque(opcao)
            else:
                continua, estoque_por_nome, correspondentes = self.buscar_estoque_por_nome(valores)
                estoque_por_lote, busca_por_lote = self.buscar_estoque_por_lote(valores)
                nome_valido = self.__tela_menu_estoque.pegar_nome_vacina(str(estoque_por_nome))
                lote_valido = self.__tela_menu_estoque.pegar_nome_vacina(str(estoque_por_lote))
                self.__tela_busca_estoque.close()
                if estoque_por_nome and continua and not busca_por_lote:
                    if nome_valido and opcao == 1:
                        self.__tela_menu_estoque.lista_estoque(correspondentes)
                    elif nome_valido and opcao == 2:
                        self.__tela_menu_estoque.msg("Não é possível fazer essa operação usando o nome na busca!")
                        return False, False, False
                elif estoque_por_lote:
                    if lote_valido and opcao == 1:
                        self.__tela_menu_estoque.mostra_dados_estoque(estoque_por_lote)
                    elif lote_valido and opcao == 2:
                        return button, estoque_por_lote, [estoque_por_lote]
                    elif not valores[1] and opcao == 2:
                        self.__tela_menu_estoque.msg("Não é possível fazer essa operação usando o nome na busca!")
                else:
                    print(nome_valido, lote_valido, estoque_por_lote, estoque_por_nome)
                    self.__tela_menu_estoque.msg("Estoque inexistente!")
                    return False, False, False
        else:
            self.__tela_busca_estoque.close()
            self.retornar_sistema()
            button, values, dec = False, False, False
            return button, values, dec

    def buscar_estoque_por_nome(self, valores):
        correspondentes = []
        continua = False
        for estoque in self.__estoque_dao.get_all():
            if valores[2].title() == estoque.tipo_vacina.nome:
                correspondentes.append(estoque)
                continua = True
        return continua, valores[2].title(), correspondentes

    def buscar_estoque_por_lote(self, valores):
        busca_por_lote = valores[1]
        acha_lote = self.__estoque_dao.get(valores[2].title())
        if acha_lote:
            return acha_lote, busca_por_lote
        else:
            return False, busca_por_lote

    def excluir_estoque(self):
        button, estoque, compativeis = self.buscar_estoque(2)
        self.__tela_busca_estoque.close()
        if button == "Submit" and estoque:
            if len(compativeis) > 1:
                lista_compativeis = []
                print('joia', len(compativeis))
                for estoque in compativeis:
                    lista_compativeis.append(estoque.lote)
                self.__tela_lista_estoques_compativeis.init_components(lista_compativeis)
                button, values = self.__tela_lista_estoques_compativeis.open()
                print(button, values)
                if button == "Submit" and values:
                    for value in values:
                        if value:
                            self.__estoque_dao.remove(value)
            self.__estoque_dao.remove(estoque.lote)
            self.__tela_menu_estoque.msg("ESTOQUE EXCLUÍDO COM SUCESSO!")
        else:
            self.__tela_busca_estoque.close()

#usado no controladorvacinacao
    def estoques_disponiveis(self):
        self.__tela_lista_estoques_compativeis.init_components(self.__estoque_dao.get_all())
