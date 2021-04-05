from tela.tela_tipo_vacina import TelaTipoVacina
from entidade.tipo_vacina import TipoVacina
from utils import estilo


class ControladorTipoVacina:

    def __init__(self, controlador_sistema):
        self.__tipos_de_vacinas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_tipo_vacina = TelaTipoVacina(self)

    def inserir_tipo_vacina(self):
        pass

    def editar_tipo_vacina(self):
        pass

    def listar_tipo_vacina(self):
        pass

    def buscar_tipo_vacina(self):
        pass

    def excluir_tipo_vacina(self):
        pass

    def retornar_sistema(self):
        return self.__controlador_sistema

    def abre_tela(self):
        estilo.clear()
        opcoes = {1: self.inserir_tipo_vacina, 2: self.editar_tipo_vacina, 3: self.listar_tipo_vacina,
                  4: self. buscar_tipo_vacina, 5: self.excluir_tipo_vacina, 6: self.retornar_sistema}
        continua = True
        while continua:
            opcao_selecionada = self.__tela_tipo_vacina.mostra_opcoes()
            if opcao_selecionada == 6:
                continua = False
            opcoes[opcao_selecionada]()






