from tela.tela_paciente import TelaPaciente
from entidade.paciente import Paciente
from utils import estilo
from utils.faker.Paciente import fakePaciente
from utils.faker.Paciente import fakePaciente2
from utils.faker.Paciente import fakePaciente3


class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self.__pacientes = [fakePaciente, fakePaciente2, fakePaciente3]
        self.__tela_paciente = TelaPaciente(self)
        self.__controlador_sistema = controlador_sistema

    def inserir_paciente(self):
        estilo.clear()
        opcao_cadastro = 1
        dados_paciente = self.__tela_paciente.pega_dados_paciente(opcao_cadastro)
        print(dados_paciente)
        paciente = Paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"],
                            dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"],
                            dados_paciente["complemento"], dados_paciente["data_nascimento"])

        if paciente not in self.__pacientes:
            self.__pacientes.append(paciente)
            return paciente

    def listar_pacientes(self):
        self.__tela_paciente.mostra_dados(self.__pacientes)

    def pega_paciente_por_nome(self):
        estilo.clear()
        nome = self.__tela_paciente.busca_paciente_nome().title()
        for paciente in self.__pacientes:
            if paciente.nome == nome:
                return paciente
        self.__tela_paciente.mostra_mensagem()
        return None

    def pega_paciente_por_cpf(self):
        estilo.clear()
        cpf = self.__tela_paciente.busca_paciente_cpf()
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente
        self.__tela_paciente.mostra_mensagem()
        return None

    def tipo_de_busca_paciente(self):
        estilo.clear()
        tipo_busca = self.__tela_paciente.mostra_opcao_busca()
        if tipo_busca == 1:
            paciente_escolhido = self.pega_paciente_por_nome()
        elif tipo_busca == 2:
            paciente_escolhido = self.pega_paciente_por_cpf()
        return paciente_escolhido

    def busca_paciente(self):
        estilo.clear()
        paciente = self.tipo_de_busca_paciente()
        self.__tela_paciente.mostra_paciente(paciente)

    def editar_paciente(self):
        paciente = self.tipo_de_busca_paciente()
        if paciente == None:
            self.inserir_paciente()
        else:
            opcao_cadastro = 2
            dado_novo = self.__tela_paciente.pega_dados_paciente(opcao_cadastro)

            if dado_novo[0] == "nome":
                paciente.nome = dado_novo[1]
            elif dado_novo[0] == "telefone":
                paciente.telefone = dado_novo[1]
            elif dado_novo[0] == "cpf":
                paciente.cpf = dado_novo[1]
            elif dado_novo[0] == "endereco":
                paciente.determinar_endereco(dado_novo[1][0], dado_novo[1][1], dado_novo[1][2], dado_novo[1][3])
            elif dado_novo[0] == "data_nascimento":
                paciente.data_nascimento = dado_novo[1]
            else:
                paciente.dose = dado_novo[1]

    def excluir_paciente(self):
        paciente = self.tipo_de_busca_paciente()
        self.__pacientes.remove(paciente)

    def retornar_sistema(self):
        return self.__controlador_sistema

    def abre_tela(self):
        opcoes = {1: self.inserir_paciente, 2: self.listar_pacientes, 3: self.editar_paciente, 4: self.excluir_paciente, 5: self.busca_paciente, 6: self.retornar_sistema}
        continua = True
        while continua:
            estilo.clear()
            opcao_selecionada = self.__tela_paciente.mostra_opcoes()
            if opcao_selecionada == 6:
                continua = False
            opcoes[opcao_selecionada]()
