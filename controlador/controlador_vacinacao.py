from entidade.vacinacao import Vacinacao
from entidade.paciente import Paciente
from entidade.enfermeiro import Enfermeiro
from excecao.nao_cadastrado import NaoCadastrado
from utils import estilo
from tela.tela_vacinacao import TelaVacinacao


class ControladorVacinacao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_vacinacao = TelaVacinacao(self)
        self.__vacinacoes = []

    def abre_tela(self):
        opcoes = {1: self.incluir_vacinacao, 2: self.listar_vacinacao, 3: self.editar_vacinacao,
                  4: self.excluir_vacinacao, 5: self.retornar_sistema}
        continua = True
        while continua:
            estilo.clear()
            opcao_selecionada = self.__tela_vacinacao.mostra_opcoes()
            if opcao_selecionada == 5:
                continua = False
            opcoes[opcao_selecionada]()

    def verificar_dose(self, paciente: Paciente):
        return paciente.dose()

    #verifica fabricante
    def verificar_tipo_dose(self, paciente: Paciente):
        if paciente.dose == None:
            return "{} ainda não tomou nenhuma vacina".format(paciente)
        else:
            #faltando tipo da vacina
            paciente.dose += 1
            return "{} deve tomar a {} dose da vacina {}".format(paciente, paciente.dose, paciente.tipo_dose)

    def editar_vacinacao(self, id, paciente: Paciente, enfermeiro: Enfermeiro, numero_dose, tipo_dose):
        if isinstance(paciente, Paciente):
            self.__paciente = paciente
        else:
            raise NaoCadastrado
        if isinstance(enfermeiro, Enfermeiro):
            self.__enfermeiro = enfermeiro
        else:
            raise NaoCadastrado

    def incluir_vacinacao(self, id, paciente: Paciente, enfermeiro: Enfermeiro, dose: int, tipo_dose: str):
        vacina = Vacinacao(id, paciente, enfermeiro, dose, tipo_dose)
        self.__vacinacoes.append(vacina)

    def excluir_vacinacao(self, id):
        for vacina in self.__vacinacoes:
            if vacina.id == id:
                self.__vacinacoes.remove(vacina)
        return "A vacinação referente ao id {} foi excluído".format(id)

    def listar_vacinacao(self):
        return Vacinacao.vacinacoes

    def retornar_sistema(self):
        return self.__controlador_sistema
