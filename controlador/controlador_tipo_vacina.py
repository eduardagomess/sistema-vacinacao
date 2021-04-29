from tela.tela_tipo_vacina import TelaTipoVacina
from entidade.vacina import TipoVacina
from utils import estilo


class ControladorTipoVacina:

    def __init__(self, controlador_sistema):
        self.__tipos_de_vacinas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_tipo_vacina = TelaTipoVacina(self)

    def inserir_tipo_vacina(self):
        opcao = 1
        dados_vacina = self.__tela_tipo_vacina.pega_dados_vacina(opcao)
        nao_cadastrado = True
        for tipo_de_vacina in self.__tipos_de_vacinas:
            if tipo_de_vacina.nome == dados_vacina["nome"]:
                nao_cadastrado = False
        if nao_cadastrado:
            novo_tipo_vacina = TipoVacina(dados_vacina["nome"], dados_vacina["num_doses"])
            self.__tipos_de_vacinas.append(novo_tipo_vacina)
        else:
            print("\n")
            self.__tela_tipo_vacina.mostra_vacina_cadastrada()
            estilo.clear()

    def editar_tipo_vacina(self):
        tipo_vacina = self.tipo_busca_tipo_vacina()
        if tipo_vacina == None:
            opcao = self.__tela_tipo_vacina.pega_opcao_tipo_nao_cadastrado()
            if opcao == 1:
                tipo_vacina = self.inserir_tipo_vacina()
                self.__tela_tipo_vacina.mostra_tipo_vacina(tipo_vacina)
            else:
                self.retornar_sistema()
        else:
            opcao = 2
            dado_a_editar = self.__tela_tipo_vacina.pega_dados_vacina(opcao)
            print(dado_a_editar)
            print(dado_a_editar[0])
            print(dado_a_editar[1])
            if dado_a_editar[0] == "nome":
                tipo_vacina.nome = str(dado_a_editar[1])
            elif dado_a_editar[0] == "num_doses":
                tipo_vacina.num_doses = str(dado_a_editar[1])

    def listar_tipo_vacina(self):
        self.__tela_tipo_vacina.mostra_dados(self.__tipos_de_vacinas)

    def buscar_vacina_por_nome(self):
        nome = self.__tela_tipo_vacina.busca_vacina_nome()
        for tipo_de_vacina in self.__tipos_de_vacinas:
            if tipo_de_vacina.nome == nome:
                return tipo_de_vacina

    def buscar_vacina_por_qtd_dose(self):
        dose = self.__tela_tipo_vacina.busca_vacina_qtd_dose()
        for tipo_de_vacina in self.__tipos_de_vacinas:
            if tipo_de_vacina.num_doses == dose:
                return tipo_de_vacina

    def tipo_busca_tipo_vacina(self):
        tipo_busca = self.__tela_tipo_vacina.mostra_opcao_busca()
        if tipo_busca == 1:
            tipo_de_vacina_desejada = self.buscar_vacina_por_nome()
        elif tipo_busca == 2:
            tipo_de_vacina_desejada = self.buscar_vacina_por_qtd_dose()
        return tipo_de_vacina_desejada

    def buscar_tipo_vacina(self):
        tipo_vacina = self.tipo_busca_tipo_vacina()
        if tipo_vacina == None:
            opcao = self.__tela_tipo_vacina.pega_opcao_tipo_nao_cadastrado()
            if opcao == 1:
                tipo_vacina = self.inserir_tipo_vacina()
                self.__tela_tipo_vacina.mostra_tipo_vacina(tipo_vacina)
            else:
                self.retornar_sistema()
        else:
            self.__tela_tipo_vacina.mostra_tipo_vacina(tipo_vacina)

    def excluir_tipo_vacina(self):
        tipo_vacina = self.tipo_busca_tipo_vacina()
        if tipo_vacina == None:
            opcao = self.__tela_tipo_vacina.pega_opcao_tipo_nao_cadastrado()
            if opcao == 1:
                tipo_vacina = self.inserir_tipo_vacina()
                self.__tela_tipo_vacina.mostra_tipo_vacina(tipo_vacina)
            else:
                self.retornar_sistema()
        else:
            self.__tipos_de_vacinas.remove(tipo_vacina)
            self.__tela_tipo_vacina.mostra_mensagem_exclusao()


    def retornar_sistema(self):
        return self.__controlador_sistema

    def abre_tela(self):
        opcoes = {1: self.inserir_tipo_vacina, 2: self.editar_tipo_vacina, 3: self.listar_tipo_vacina,
                  4: self.buscar_tipo_vacina, 5: self.excluir_tipo_vacina, 6: self.retornar_sistema}
        continua = True
        while continua:
            opcao_selecionada = self.__tela_tipo_vacina.mostra_opcoes()
            if opcao_selecionada == 6:
                continua = False
            opcoes[opcao_selecionada]()






