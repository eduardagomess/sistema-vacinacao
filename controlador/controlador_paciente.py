from tela.tela_paciente import TelaPaciente
from entidade.paciente import Paciente
from tela.tela_inserir_paciente import TelaInserirPaciente
from tela.tela_opcoes import TelaOpcoesPaciente
from utils import estilo



class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self.__pacientes = []
        self.__tela_paciente = TelaPaciente(self)
        self.__tela_inserir_paciente = TelaInserirPaciente(self)
        self.__tela_opcoes = TelaOpcoesPaciente(self)
        self.__controlador_sistema = controlador_sistema

    def inserir_paciente(self):
       
        dados_paciente = self.__tela_inserir_paciente.open()
        print(dados_paciente)
        nao_cadastrado = True
        for paciente in self.__pacientes:
            if paciente.cpf == dados_paciente["cpf"]:
                nao_cadastrado = False
        if nao_cadastrado:
            novo_paciente = Paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["data_nascimento"])
            novo_paciente.determinar_endereco(dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"],dados_paciente["complemento"])
            self.__pacientes.append(novo_paciente)
            return novo_paciente
        """else
           self.__tela_paciente.mostra_msg_paciente_cadastro()"""
       

    def listar_pacientes(self):
        self.__tela_paciente.mostra_dados(self.__pacientes)

    def pega_paciente_por_nome(self):
        estilo.clear()
        nome = self.__tela_paciente.busca_paciente_nome().title()
        for paciente in self.__pacientes:
            if paciente.nome == nome:
                return paciente
        return None

    def pega_paciente_por_cpf(self):
        estilo.clear()
        cpf = self.__tela_paciente.busca_paciente_cpf()
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None

    def tipo_de_busca_paciente(self):
        
        tipo_busca = self.__tela_opcoes.open()
        print(tipo_busca)
        if tipo_busca == 1:
            paciente_escolhido = self.pega_paciente_por_nome()
        elif tipo_busca == 2:
            paciente_escolhido = self.pega_paciente_por_cpf()
        return paciente_escolhido

    def busca_paciente(self):
        estilo.clear()
        paciente = self.tipo_de_busca_paciente()
        if paciente == None:
            opcao = self.__tela_paciente.pega_opcao_paciente_sem_cadastro()
            if opcao == 1:
                paciente = self.inserir_paciente()
                self.__tela_paciente.mostra_paciente(paciente)
            else:
                self.retornar_sistema()
        else:
            self.__tela_paciente.mostra_paciente(paciente)

    def editar_paciente(self):
        paciente = self.tipo_de_busca_paciente()
        if paciente == None:
            opcao = self.__tela_paciente.pega_opcao_paciente_sem_cadastro()
            if opcao == 1:
                paciente = self.inserir_paciente()
                self.__tela_paciente.mostra_paciente(paciente)
            else:
                self.retornar_sistema()
        else:
            dado_novo = self.__tela_paciente.alterar_opcoes_paciente()
            print(dado_novo)
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

    def excluir_paciente(self):
        paciente = self.tipo_de_busca_paciente()
        if paciente == None:
            opcao = self.__tela_paciente.pega_opcao_paciente_sem_cadastro()
            if opcao == 1:
                paciente = self.inserir_paciente()
                self.__tela_paciente.mostra_paciente(paciente)
            else:
                self.retornar_sistema()
        else:
            self.__pacientes.remove(paciente)
            self.__tela_paciente.mostra_mensagem_paciente_exlcuido()

    def retornar_sistema(self):
        return self.__controlador_sistema
       
    def abre_tela(self):
        opcoes = {1: self.inserir_paciente, 2: self.listar_pacientes, 3: self.editar_paciente, 4: self.excluir_paciente, 5: self.busca_paciente}
        while True:
            button, values = self.__tela_paciente.open()
            if button == "Sair":
                self.finaliza_sistema()
            else:
                [opcoes[num]() for num in values.values() if num]
