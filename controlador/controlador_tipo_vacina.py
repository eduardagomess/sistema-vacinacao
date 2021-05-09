from tela.tipo_vacina.tela_lista_tipo_vacina import TelaListaTipoVacina
from tela.tipo_vacina.tela_registro_tipo_vacina import TelaRegistroTipoVacina
from tela.tipo_vacina.tela_menu_tipo_vacina import TelaMenuTipoVacina
from tela.tipo_vacina.tela_busca_tipo_vacina import TelaBuscaTipoVacina
from tela.tipo_vacina.tela_edicao_tipo_vacina import TelaEditaTipoVacina
from entidade.vacina import TipoVacina
import PySimpleGUI as sg
#pipenv install mypy
# cmd -> mypy typehints-exemplo3.py


class ControladorTipoVacina:

    def __init__(self, controlador_sistema):
        self.__tela_lista_tipo_vacina = TelaListaTipoVacina(self)
        self.__tela_menu_tipo_vacina = TelaMenuTipoVacina(self)
        self.__tela_busca_tipo_vacina = TelaBuscaTipoVacina(self)
        # self.__tipos_de_vacinas = [] vai pra classe TiposVacinaDAO
        self.__tipos_de_vacinas = [TipoVacina('Pfizer', 2)]
        self.__controlador_sistema = controlador_sistema
        self.__tela_registro_tipo_vacina = TelaRegistroTipoVacina(self)

    def inserir_tipo_vacina(self, nome, num_doses):
        self.__tela_registro_tipo_vacina.pega_dados_vacina(nome,num_doses)
        button, dados_vacina = self.__tela_registro_tipo_vacina.open()
        nao_cadastrado = True
        if button == 'Submit':
            for tipo_de_vacina in self.__tipos_de_vacinas:
                if tipo_de_vacina.nome == dados_vacina["nome"].title():
                    self.__tela_menu_tipo_vacina.msg("Essa vacina já está cadastrada!")
                    nao_cadastrado = False
                    self.__tela_registro_tipo_vacina.close()
            if (self.__tipos_de_vacinas == []) or nao_cadastrado:
                nome = self.__tela_menu_tipo_vacina.pegar_nome_vacina(dados_vacina["nome"])
                num_doses = self.__tela_menu_tipo_vacina.pegar_dose_vacina(dados_vacina["num_doses"])
                self.__tela_registro_tipo_vacina.close()
                if nome and num_doses:
                    novo_tipo_vacina = TipoVacina(nome, num_doses)
                    self.__tipos_de_vacinas.append(novo_tipo_vacina)
                    self.__tela_menu_tipo_vacina.msg("Resposta cadastrada com sucesso! ")
        else:
            self.retornar_sistema()

    def editar_tipo_vacina(self):
        button, tipo_vacina_editar = self.buscar_tipo_vacina(2)
        if tipo_vacina_editar and button == "Aplicar":
            self.__tela_registro_tipo_vacina.pega_dados_vacina(tipo_vacina_editar.nome, tipo_vacina_editar.num_doses)
            button, dado_a_editar = self.__tela_registro_tipo_vacina.open()
            self.__tela_registro_tipo_vacina.close()
            if button == "Submit":
                nome = self.__tela_menu_tipo_vacina.pegar_nome_vacina(dado_a_editar["nome"])
                num_doses = self.__tela_menu_tipo_vacina.pegar_dose_vacina(dado_a_editar["num_doses"])
                cadastrado = self.busca_vacina(nome)
                if nome and num_doses and cadastrado == None:
                    tipo_vacina_editar.nome = str(nome)
                    tipo_vacina_editar.num_doses = str(num_doses)
                    self.__tela_menu_tipo_vacina.msg("Edição feita com sucesso!")
                    self.__tela_busca_tipo_vacina.close()
                elif nome and num_doses and cadastrado != None:
                    self.__tela_menu_tipo_vacina.msg("Esse nome já está cadastrado!")
                    self.retornar_sistema()
        self.__tela_busca_tipo_vacina.close()
        self.retornar_sistema()

#método retorna tipovacina encontrado pelo nome para ser usado no controlador_estoque
    def busca_vacina(self, nome: str):
        for vacina in self.__tipos_de_vacinas:
            if vacina.nome == nome:
                return vacina
        return None

    def listar_tipo_vacina(self):
        if self.__tipos_de_vacinas == []:
            self.__tela_menu_tipo_vacina.msg("Não há vacinas cadastradas!")
        else:
            self.__tela_lista_tipo_vacina.init_components(self.__tipos_de_vacinas)

    def buscar_tipo_vacina(self, opcao):
        self.__tela_busca_tipo_vacina.init_components()
        button, nome = self.__tela_busca_tipo_vacina.open()
        if button == "Aplicar":
            self.__tela_busca_tipo_vacina.close()
            if self.__tipos_de_vacinas == []:
                    self.__tela_menu_tipo_vacina.msg("Não há vacinas cadastradas!!")
            else:
                nome = self.__tela_menu_tipo_vacina.pegar_nome_vacina(nome[0])
                for tipo_de_vacina in self.__tipos_de_vacinas:
                    if tipo_de_vacina.nome == nome and opcao == 1:
                        self.__tela_menu_tipo_vacina.mostra_tipo_vacina(tipo_de_vacina)
                    elif tipo_de_vacina.nome == nome and opcao == 2:
                        return button, tipo_de_vacina
                    elif not nome:
                        self.__tela_busca_tipo_vacina.close()
                        tipo_de_vacina = False
                        return button, tipo_de_vacina
                    else:
                        self.__tela_menu_tipo_vacina.msg("Essa vacina ainda não foi cadastrada! \n Cadastre-a primeiro")
        else:
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
                self.__tipos_de_vacinas.remove(tipo_vacina)
                self.__tela_menu_tipo_vacina.msg("VACINA EXCLUÍDA COM SUCESSO!")
        else:
            self.retornar_sistema()

    def retornar_sistema(self):
        return self.__controlador_sistema

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
                        elif index == 4 and self.__tipos_de_vacinas != []:
                            opcoes[index](1)
                        elif (index == 4 or index == 3) and self.__tipos_de_vacinas == []:
                            self.__tela_menu_tipo_vacina.msg("Não há vacinas cadastradas!")
                        else:
                            opcoes[index]()
                    index += 1


