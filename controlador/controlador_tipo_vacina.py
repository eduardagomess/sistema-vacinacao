from tela.tipo_vacina.tela_lista_tipo_vacina import TelaListaTipoVacina
from tela.tipo_vacina.tela_registro_tipo_vacina import TelaRegistroTipoVacina
from tela.tipo_vacina.tela_menu_tipo_vacina import TelaMenuTipoVacina
from entidade.vacina import TipoVacina

class ControladorTipoVacina:

    def __init__(self, controlador_sistema):
        self.__tela_lista_tipo_vacina = TelaListaTipoVacina(self)
        self.__tela_menu_tipo_vacina = TelaMenuTipoVacina(self)
        self.tipos_de_vacinas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_registro_tipo_vacina = TelaRegistroTipoVacina(self)

    def inserir_tipo_vacina(self):
        self.__tela_registro_tipo_vacina.pega_dados_vacina()
        dados_vacina = self.__tela_registro_tipo_vacina.open()
        nao_cadastrado = True
        for tipo_de_vacina in self.tipos_de_vacinas:
            if tipo_de_vacina.nome == dados_vacina["nome"]:
                nao_cadastrado = False
        if nao_cadastrado:
            novo_tipo_vacina = TipoVacina(dados_vacina["nome"], dados_vacina["num_doses"])
            self.tipos_de_vacinas.append(novo_tipo_vacina)
            self.__tela_menu_tipo_vacina.msg(" Resposta cadastrada com sucesso! ")
            return novo_tipo_vacina
        else:
            print("\n")
            self.__tela_menu_tipo_vacina.msg("ESTA VACINA JÁ ESTÁ CADASTRADA!")

    def listar_tipo_vacina(self):
        self.__tela_lista_tipo_vacina.init_components(self.tipos_de_vacinas)

    def buscar_vacina_por_nome(self):
        nome = self.__tela_menu_tipo_vacina.busca_vacina_nome()
        for tipo_de_vacina in self.tipos_de_vacinas:
            if tipo_de_vacina.nome == nome:
                return tipo_de_vacina

    def buscar_tipo_vacina(self):
        tipo_vacina = self.buscar_vacina_por_nome()
        if tipo_vacina == None:
            opcao = self.__tela_menu_tipo_vacina.pega_opcao_tipo_nao_cadastrado()
            if opcao == 1:
                tipo_vacina = self.inserir_tipo_vacina()
                self.__tela_menu_tipo_vacina.mostra_tipo_vacina(tipo_vacina)
            else:
                self.retornar_sistema()
        else:
            self.__tela_menu_tipo_vacina.mostra_tipo_vacina(tipo_vacina)

    def excluir_tipo_vacina(self):
        tipo_vacina = self.buscar_vacina_por_nome()
        if tipo_vacina == None:
            opcao = self.__tela_menu_tipo_vacina.pega_opcao_tipo_nao_cadastrado()
            if opcao == 1:
                tipo_vacina = self.inserir_tipo_vacina()
                self.__tela_menu_tipo_vacina.mostra_tipo_vacina(tipo_vacina)
            else:
                self.retornar_sistema()
        else:
            self.tipos_de_vacinas.remove(tipo_vacina)
            self.__tela_menu_tipo_vacina.msg("VACINA EXCLUÍDA COM SUCESSO!")

    def retornar_sistema(self):
        return self.__controlador_sistema

    def abre_tela(self):
        opcoes = {1: self.inserir_tipo_vacina, 2: self.editar_tipo_vacina, 3: self.listar_tipo_vacina,
                  4: self.buscar_tipo_vacina, 5: self.excluir_tipo_vacina, 6: self.retornar_sistema}
        while True:
            button, values = self.__tela_menu_tipo_vacina.open()
            if button == "Sair" or button is None:
                self.finaliza_sistema()
            else:
                count = 1
                for i in values.values():
                    if i:
                        opcoes[count]()
                    count += 1

    def finaliza_sistema(self):
        exit(0)

    def editar_tipo_vacina(self):
        pass
        """
        tipo_vacina = self.buscar_vacina_por_nome()
        if tipo_vacina is None:
            opcao = self.__tela_menu_tipo_vacina.pega_opcao_tipo_nao_cadastrado()
            if opcao == 1:
                tipo_vacina = self.inserir_tipo_vacina()
                self.__tela_menu_tipo_vacina.mostra_tipo_vacina(tipo_vacina)
            else:
                self.retornar_sistema()
        else:
            opcao = 2
            dado_a_editar = self.__tela_menu_tipo_vacina.pega_dados_vacina(opcao)
            if dado_a_editar[0] == "nome":
                tipo_vacina.nome = str(dado_a_editar[1])
            elif dado_a_editar[0] == "num_doses":
                tipo_vacina.num_doses = str(dado_a_editar[1])
"""
