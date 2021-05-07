from tela.tipo_vacina.tela_lista_tipo_vacina import TelaListaTipoVacina
from tela.tipo_vacina.tela_registro_tipo_vacina import TelaRegistroTipoVacina
from tela.tipo_vacina.tela_menu_tipo_vacina import TelaMenuTipoVacina
from tela.tipo_vacina.tela_busca_tipo_vacina import TelaBuscaTipoVacina
from tela.tipo_vacina.tela_edicao_tipo_vacina import TelaEditaTipoVacina
from entidade.vacina import TipoVacina
from tela.tela_abstrata import AbstractTela

class ControladorTipoVacina:

    def __init__(self, controlador_sistema):
        self.__tela_abstrata = AbstractTela
        self.__tela_lista_tipo_vacina = TelaListaTipoVacina(self)
        self.__tela_menu_tipo_vacina = TelaMenuTipoVacina(self)
        self.__tela_busca_tipo_vacina = TelaBuscaTipoVacina(self)
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
            self.__tela_registro_tipo_vacina.close()
            self.__tela_menu_tipo_vacina.msg(" Resposta cadastrada com sucesso! ")
            return novo_tipo_vacina
        else:
            print("\n")
            self.__tela_menu_tipo_vacina.msg("ESTA VACINA JÁ ESTÁ CADASTRADA!")
            self.__tela_registro_tipo_vacina.close()

    def listar_tipo_vacina(self):
        self.__tela_lista_tipo_vacina.init_components(self.tipos_de_vacinas)

    def buscar_vacina_por_nome(self):
        self.__tela_busca_tipo_vacina.init_components()
        nome = self.__tela_busca_tipo_vacina.open()
        for tipo_de_vacina in self.tipos_de_vacinas:
            if tipo_de_vacina.nome == nome:
                return tipo_de_vacina

    def buscar_tipo_vacina(self):
        self.__tela_busca_tipo_vacina.init_components()
        nome = self.__tela_busca_tipo_vacina.open()
        for tipo_de_vacina in self.tipos_de_vacinas:
            if tipo_de_vacina is None:
                self.__tela_menu_tipo_vacina.msg("Essa vacina ainda não foi cadastrada! \n Cadastre-a primeiro")
            elif tipo_de_vacina.nome == nome:
                self.__tela_menu_tipo_vacina.mostra_tipo_vacina(tipo_de_vacina)

    def excluir_tipo_vacina(self):
        tipo_vacina = self.buscar_vacina_por_nome()
        if tipo_vacina is None:
            self.__tela_menu_tipo_vacina.msg("Essa vacina não foi cadastrada! \n Cadastre-a primeiro.")
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
                self.retornar_sistema()
            else:
                count = 1
                for i in values.values():
                    if i:
                        opcoes[count]()
                    count += 1

    def editar_tipo_vacina(self):
        tipo_vacina_editar = self.buscar_vacina_por_nome()
        if tipo_vacina_editar is not None:
            self.__tela_registro_tipo_vacina.pega_dados_vacina()
            dado_a_editar = self.__tela_registro_tipo_vacina.open()
            tipo_vacina_editar.nome = str(dado_a_editar['nome'])
            tipo_vacina_editar.num_doses = str(dado_a_editar['num_doses'])
            self.__tela_menu_tipo_vacina.msg("Edição feita com sucesso!")
        else:
            self.__tela_menu_tipo_vacina.msg("Essa vacina não foi encontrada!")
