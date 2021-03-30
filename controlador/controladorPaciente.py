from tela.telaPaciente import TelaPaciente
from entidade.paciente import Paciente
from utils import estilo


class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self.__pacientes = []
        self.__tela_paciente = TelaPaciente()
        self.__controlador_sistema = controlador_sistema

    def inserir_paciente(self):
        estilo.clear()
        dados_paciente = self.__tela_paciente.pega_dados_paciente()

        paciente = Paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"],
                            dados_paciente["endereco"], dados_paciente["data_nascimento"], dados_paciente["dose"])

        if paciente not in self.__pacientes:
            self.__pacientes.append(paciente)
            return paciente

    def listar_pacientes(self):
        for paciente in self.__pacientes:
            self.__tela_paciente.mostra_dados({"nome": paciente.nome, "telefone": paciente.telefone,
                                                        "cpf": paciente.cpf, "endereco": paciente.endereco,
                                                        "data_nascimento": paciente.data_nascimento, "dose": paciente.dose})

    def pega_paciente_por_nome(self):
        estilo.clear()
        nome = self.__tela_paciente.busca_paciente_nome()
        for paciente in self.__pacientes:
            if paciente.nome == nome:
                return paciente

    def pega_paciente_por_cpf(self):
        estilo.clear()
        cpf = self.__tela_paciente.busca_paciente_cpf()
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente

    def tipo_de_busca_paciente(self):
        estilo.clear()
        tipo_busca = self.__tela_paciente.mostra_opcao_busca()
        if tipo_busca == 1:
            paciente_escolhido = self.pega_paciente_por_nome()
        else:
            paciente_escolhido = self.pega_paciente_por_cpf()
        return paciente_escolhido

    def busca_paciente(self):
        estilo.clear()
        paciente = self.tipo_de_busca_paciente()
        return paciente


    def editar_paciente(self):
        paciente = self.busca_paciente()
        tipo_de_alteracao = self.__tela_paciente.mostra_opcao_alteracao_cadastro()
        dado_novo = self.__tela_paciente.pega_novos_dados(tipo_de_alteracao)

        if dado_novo[0] == "nome":
            paciente.nome = dado_novo[1]
        elif dado_novo[0] == "telefone":
            paciente.telefone = dado_novo[1]
        elif dado_novo[0] == "cpf":
            paciente.cpf = dado_novo[1]
        elif dado_novo[0] == "endereco":
            paciente.endereco = dado_novo[1]
        elif dado_novo[0] == "data_nascimento":
            paciente.data_nascimento = dado_novo[1]
        paciente.dose = dado_novo[1]

    def excluir_paciente(self):
        paciente = self.busca_paciente()
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
