from persistencia.vacinaDAO import VacinaDAO
from tela.tipo_vacina.tela_lista_tipo_vacina import TelaListaTipoVacina
from tela.tipo_vacina.tela_registro_tipo_vacina import TelaRegistroTipoVacina
from tela.tipo_vacina.tela_menu_tipo_vacina import TelaMenuTipoVacina
from tela.tipo_vacina.tela_busca_tipo_vacina import TelaBuscaTipoVacina
from entidade.vacina import TipoVacina

# pipenv install mypy
# cmd -> mypy typehints-exemplo3.py


class ControladorTipoVacina:

    def __init__(self, controlador_sistema):
        self.__tela_lista_tipo_vacina = TelaListaTipoVacina(self)
        self.__tela_menu_tipo_vacina = TelaMenuTipoVacina(self)
        self.__tela_busca_tipo_vacina = TelaBuscaTipoVacina(self)
        self.__tela_registro_tipo_vacina = TelaRegistroTipoVacina(self)
        self.__vacina_dao = VacinaDAO()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        opcoes = {1: self.inserir_tipo_vacina, 2: self.editar_tipo_vacina, 3: self.listar_tipo_vacina,
                  4: self.buscar_tipo_vacina, 5: self.excluir_tipo_vacina, 6: self.retornar_sistema}
        while True:
            button, values = self.__tela_menu_tipo_vacina.open()
            if button == "Sair" or button is None:
                break
            else:
                index = 1
                for i in values.values():
                    if i:
                        if index == 1:
                            opcoes[index](None, None)
                        elif index == 4 and self.__vacina_dao.get_all():
                            opcoes[index](1)
                        elif (index == 4 or index == 3) and not self.__vacina_dao.get_all():
                            self.__tela_menu_tipo_vacina.msg("Não há vacinas cadastradas!")
                        else:
                            opcoes[index]()
                    index += 1

    def inserir_tipo_vacina(self, nome, num_doses):
        self.__tela_registro_tipo_vacina.pega_dados_vacina(nome, num_doses)
        button, dados_vacina = self.__tela_registro_tipo_vacina.open()
        nao_cadastrado = True
        if button == 'Submit':
            if self.__vacina_dao.get(dados_vacina["nome"].title()):
                self.__tela_menu_tipo_vacina.msg("Essa vacina já está cadastrada!")
                nao_cadastrado = False
                self.__tela_registro_tipo_vacina.close()
            if not self.__vacina_dao.get_all() or nao_cadastrado:
                nome = self.__tela_menu_tipo_vacina.pegar_nome_vacina(dados_vacina["nome"])
                num_doses = self.__tela_menu_tipo_vacina.pegar_dose_vacina(dados_vacina["num_doses"])
                self.__tela_registro_tipo_vacina.close()
                if nome and num_doses:
                    self.__vacina_dao.add(nome, TipoVacina(nome, num_doses))
                    self.__tela_menu_tipo_vacina.msg("Resposta cadastrada com sucesso! ")
        else:
            self.retornar_sistema()

    def buscar_tipo_vacina(self, opcao):
        self.__tela_busca_tipo_vacina.init_components()
        button, nome = self.__tela_busca_tipo_vacina.open()
        if button == "Aplicar":
            self.__tela_busca_tipo_vacina.close()
            if not self.__vacina_dao.get_all():
                self.__tela_menu_tipo_vacina.msg("Não há vacinas cadastradas!!")
            else:
                nome = self.__tela_menu_tipo_vacina.pegar_nome_vacina(nome[0])
                tipo_vacina = self.__vacina_dao.get(nome)
                if tipo_vacina and opcao == 1:
                    self.__tela_menu_tipo_vacina.mostra_tipo_vacina(tipo_vacina)
                elif tipo_vacina and opcao == 2:
                    return button, tipo_vacina
                elif not tipo_vacina and opcao == 1:
                    self.__tela_menu_tipo_vacina.msg("Não foi possível achar a vacina.")
                elif not nome:
                    self.retornar_sistema()
                    button, values = False, False
                    return button, values
        else:
            self.retornar_sistema()
            button, values = False, False
            return button, values

    def editar_tipo_vacina(self):
        button, tipo_vacina_editar = self.buscar_tipo_vacina(2)
        if tipo_vacina_editar and button == "Aplicar":
            self.__tela_registro_tipo_vacina.pega_dados_vacina(tipo_vacina_editar.nome, tipo_vacina_editar.num_doses)
            button, vacina_nova = self.__tela_registro_tipo_vacina.open()
            print((button, vacina_nova))
            self.__tela_registro_tipo_vacina.close()
            if button == "Submit":
                nome = self.__tela_menu_tipo_vacina.pegar_nome_vacina(vacina_nova["nome"])
                num_doses = self.__tela_menu_tipo_vacina.pegar_dose_vacina(vacina_nova["num_doses"])
                cadastrado = self.busca_vacina(nome)
                if nome and num_doses and cadastrado is None:
                    self.__vacina_dao.remove(tipo_vacina_editar.nome)
                    self.__vacina_dao.add(nome, TipoVacina(nome, num_doses))
                    self.__tela_menu_tipo_vacina.msg("Edição feita com sucesso!")
                    self.__tela_busca_tipo_vacina.close()
                elif nome and num_doses and cadastrado != None:
                    self.__tela_menu_tipo_vacina.msg("Esse nome já está cadastrado!")
                    self.retornar_sistema()
        self.__tela_busca_tipo_vacina.close()
        self.retornar_sistema()

    def excluir_tipo_vacina(self):
        button, tipo_vacina = self.buscar_tipo_vacina(2)
        if button == "Aplicar":
            if tipo_vacina is None:
                self.__tela_menu_tipo_vacina.msg("Essa vacina não foi cadastrada! \n Cadastre-a primeiro.")
                self.retornar_sistema()
            elif not tipo_vacina:
                self.retornar_sistema()
            else:
                if self.__vacina_dao.get(tipo_vacina.nome):
                    self.__vacina_dao.remove(tipo_vacina.nome)
                    self.__tela_menu_tipo_vacina.msg("VACINA EXCLUÍDA COM SUCESSO!")
                else:
                    self.__vacina_dao.remove(tipo_vacina.nome)
                    self.__vacina_dao.remove(tipo_vacina)
                    print(tipo_vacina, tipo_vacina.nome, self.__vacina_dao.get(tipo_vacina.nome))
                    print(self.__vacina_dao.remove(tipo_vacina), self.__vacina_dao.remove(tipo_vacina.nome))
                    self.__tela_menu_tipo_vacina.msg("Houve um erro ao encontrar a vacina.")
            self.retornar_sistema()
        else:
            self.retornar_sistema()

    # método retorna tipovacina encontrado pelo nome para ser usado no controlador_estoque
    def busca_vacina(self, nome: str):
         return self.__vacina_dao.get(nome)

    def listar_tipo_vacina(self):
        if not self.__vacina_dao.get_all():
            self.__tela_menu_tipo_vacina.msg("Não há vacinas cadastradas!")
        else:
            self.__tela_lista_tipo_vacina.init_components(self.__vacina_dao.get_all())

    def retornar_sistema(self):
        return self.__controlador_sistema
