from entidade.vacinacao import Vacinacao
from entidade.paciente import Paciente
from entidade.enfermeiro import Enfermeiro
from excecao.nao_cadastrado import NaoCadastrado


class ControladorVacinacao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__vacinacoes = []


    def abre_tela(self):
        pass

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
            raise NaoCadastrado()
        if isinstance(enfermeiro, Enfermeiro):
            self.__enfermeiro = enfermeiro
        else:
            raise NaoCadastrado()

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
