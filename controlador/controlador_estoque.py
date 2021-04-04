from entidade.estoque import Estoque
from excecao import erro_de_tipo

class ControladorEstoque:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        pass

    def adiciona_vacina(self, tipo, quantidade):
        if not isinstance(tipo, str) or not isinstance(quantidade, int):
            raise erro_de_tipo
        else:
            novo_registro = Estoque(tipo, quantidade)
            return "Estoque atualizado."

    def editar_vacina(self, tipo: Estoque.tipo, quantidade: int):
        if not isinstance(tipo, str) or not isinstance(quantidade, int):
            raise erro_de_tipo
        elif Estoque.tipo == tipo:
            #Estoque.quantidade(self, quantidade)
            pass

    def listar_vacina(self):
        #dict
        pass

    def buscar_vacina(self):
        pass

    def listar_vacinas_aplicadas(self):
        return Estoque.vacinas_aplicadas
