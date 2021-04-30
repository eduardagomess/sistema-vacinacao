from tela.tela_tipo_vacina import TelaTipoVacina
from entidade.vacina import TipoVacina

class ControladorTipoVacina:

    def __init__(self, controlador_sistema):
        self.tipos_de_vacinas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_tipo_vacina = TelaTipoVacina(self)

    def inserir_tipo_vacina(self):
        opcao = 1
        dados_vacina = self.__tela_tipo_vacina.pega_dados_vacina(opcao)
        nao_cadastrado = True
        for tipo_de_vacina in self.tipos_de_vacinas:
            if tipo_de_vacina.nome == dados_vacina["nome"]:
                nao_cadastrado = False
        if nao_cadastrado:
            novo_tipo_vacina = TipoVacina(dados_vacina["nome"], dados_vacina["num_doses"], dados_vacina['qtd'])
            self.tipos_de_vacinas.append(novo_tipo_vacina)
            self.__tela_tipo_vacina.mostra_resposta_cadastrada()
            return novo_tipo_vacina
        else:
            print("\n")
            self.__tela_tipo_vacina.mostra_vacina_cadastrada()

    def editar_tipo_vacina(self):
        tipo_vacina = self.buscar_vacina_por_nome()
        if tipo_vacina is None:
            opcao = self.__tela_tipo_vacina.pega_opcao_tipo_nao_cadastrado()
            if opcao == 1:
                tipo_vacina = self.inserir_tipo_vacina()
                self.__tela_tipo_vacina.mostra_tipo_vacina(tipo_vacina)
            else:
                self.retornar_sistema()
        else:
            opcao = 2
            dado_a_editar = self.__tela_tipo_vacina.pega_dados_vacina(opcao)
            if dado_a_editar[0] == "nome":
                tipo_vacina.nome = str(dado_a_editar[1])
            elif dado_a_editar[0] == "num_doses":
                tipo_vacina.num_doses = str(dado_a_editar[1])
            elif dado_a_editar[0] == "qtd":
                tipo_vacina.qtd = str(dado_a_editar[1])

    def listar_tipo_vacina(self):
        self.__tela_tipo_vacina.titulo_busca()
        self.__tela_tipo_vacina.mostra_dados(self.tipos_de_vacinas)

    def buscar_vacina_por_nome(self):
        nome = self.__tela_tipo_vacina.busca_vacina_nome()
        for tipo_de_vacina in self.tipos_de_vacinas:
            if tipo_de_vacina.nome == nome:
                return tipo_de_vacina

    def buscar_tipo_vacina(self):
        tipo_vacina = self.buscar_vacina_por_nome()
        if tipo_vacina == None:
            opcao = self.__tela_tipo_vacina.pega_opcao_tipo_nao_cadastrado()
            if opcao == 1:
                tipo_vacina = self.inserir_tipo_vacina()
                self.__tela_tipo_vacina.mostra_tipo_vacina(tipo_vacina)
            else:
                self.retornar_sistema()
        else:
            self.__tela_tipo_vacina.mostra_tipo_vacina(tipo_vacina)


    def alterar_quantidade(self):
        tipo_vacina = self.buscar_vacina_por_nome()
        if tipo_vacina is None:
            opcao = self.__tela_tipo_vacina.pega_opcao_tipo_nao_cadastrado()
            if opcao == 1:
                tipo_vacina = self.inserir_tipo_vacina()
                self.__tela_tipo_vacina.mostra_tipo_vacina(tipo_vacina)
            else:
                self.retornar_sistema()
        else:
            opcao = 6
            dado_a_editar = self.__tela_tipo_vacina.pega_dados_vacina(opcao)
            if dado_a_editar[0] == "qtd_somar":
                tipo_vacina.qtd += int(dado_a_editar[1])
            elif dado_a_editar[0] == "qtd_subtrair":
                tipo_vacina.qtd -= int(dado_a_editar[1])


    def excluir_tipo_vacina(self):
        tipo_vacina = self.buscar_vacina_por_nome()
        if tipo_vacina == None:
            opcao = self.__tela_tipo_vacina.pega_opcao_tipo_nao_cadastrado()
            if opcao == 1:
                tipo_vacina = self.inserir_tipo_vacina()
                self.__tela_tipo_vacina.mostra_tipo_vacina(tipo_vacina)
            else:
                self.retornar_sistema()
        else:
            self.tipos_de_vacinas.remove(tipo_vacina)
            self.__tela_tipo_vacina.mostra_mensagem_exclusao()


    def retornar_sistema(self):
        return self.__controlador_sistema

    def abre_tela(self):
        opcoes = {1: self.inserir_tipo_vacina, 2: self.editar_tipo_vacina, 3: self.listar_tipo_vacina,
                  4: self.buscar_tipo_vacina, 5: self.excluir_tipo_vacina, 6: self.alterar_quantidade, 7: self.retornar_sistema}
        continua = True
        while continua:
            opcao_selecionada = self.__tela_tipo_vacina.mostra_opcoes()
            if opcao_selecionada == 7:
                continua = False
            opcoes[opcao_selecionada]()
