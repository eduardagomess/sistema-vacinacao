from entidade.enfermeiro import Enfermeiro
from tela.tela_enfermeiro.tela_inserir_enfermeiro import TelaInserirEnfermeiro
from tela.tela_paciente.tela_listagem import TelaListagem
from utils import estilo
import PySimpleGUI as sg


class ControladorEnfermeiro:

    def __init__(self, controlador_sistema):
        self.__enfermeiros = []
        self.__tela_inserir_enfermeiro = TelaInserirEnfermeiro(self)
        self.__tela_listagem = TelaListagem(self)
        self.__controlador_sistema = controlador_sistema

    def inserir_enfermeiro(self, nome, telefone, cpf, coren):
        self.__tela_inserir_enfermeiro.init_components(nome, telefone, cpf, coren)
        button, dados_enfermeiro = self.__tela_inserir_enfermeiro.open()
        cadastrado = True
         
        if button == 'Salvar':
            while cadastrado:
                nome = dados_paciente["nome"]
                try:
                    if not nome.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(nome.replace(" ", "")) < 5:
                        raise NomeInvalido  
                except NomeComCaracterNumerico:
                    sg.Popup("Nome inválido","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro(None, dados_enfermeiro["telefone"], dados_enfermeiro["cpf"], dados_enfermeiro["coren"])
                    break
                except NomeInvalido:
                    sg.Popup("Nome inválido","Preencha o nome com no mínimo 5 caracteres")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro(None, dados_enfermeiro["telefone"], dados_enfermeiro["cpf"], dados_enfermeiro["coren"])
                    break

                telefone = dados_enfermeiro["telefone"]
                try:
                    if not telefone.isdigit():
                        raise CaracterAlfabeticoExcecao
                    elif len(telefone) < 10 or (len(telefone) > 13):
                        raise TelefoneComNumeroInvalido
                except CaracterAlfabeticoExcecao:
                    sg.Popup("Telefone inválido", "Valor incorreto, insira apenas números")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro(dados_enfermeiro["nome"], None, dados_enfermeiro["cpf"], dados_enfermeiro["coren"])
                    break
                except TelefoneComNumeroInvalido:
                    sg.Popup("Telefone inválido","Valor incorreto, o número deve conter de 10 a 11 digitos (incluíndo DDD)")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro(dados_enfermeiro["nome"], None, dados_enfermeiro["cpf"], dados_enfermeiro["coren"])
                    break

                cpf = dados_enfermeiro["cpf"]
                try:
                    if not cpf.isdigit():
                        raise CaracterAlfabeticoExcecao
                    elif len(cpf) != 11:
                        raise CpfInvalido
                except CaracterAlfabeticoExcecao:
                    sg.Popup("CPF inválido","Valor incorreto, insira apenas números")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro(dados_enfermeiro["nome"],dados_enfermeiro["telefone"], None, dados_enfermeiro["coren"])
                    break
                except CpfInvalido:
                    sg.Popup("CPF inválido","Valor incorreto, o CPF deve conter 11 digitos, formatação: 12645974944")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro(dados_enfermeiro["nome"],dados_enfermeiro["telefone"], None, dados_enfermeiro["coren"])
                    break
                
                coren = dados_paciente["coren"] 
                try:
                    if not numero.isdigit():
                        raise Exception
                except Exception:
                    sg.Popup("Número inválido","Valor incorreto, insira apenas números")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro(dados_enfermeiro["nome"],dados_enfermeiro["telefone"],dados_enfermeiro["cpf"], None)
                    break
                try:
                    for enfermeiro in self.__enfermeiros:
                        if enfermeiro.coren == dados_enfermeiro["coren"]:
                             raise ValueError
                    novo_enfermeiro = Enfermeiro(dados_enfermeiro["nome"], dados_enfermeiro["telefone"], dados_enfermeiro["cpf"], dados_enfermeiro["coren"])
                    self.__enfermeiros.append(novo_enfermeiro)
                    self.__tela_inserir_enfermeiro.close()
                    sg.popup("Cadastramento", "Enfermeiro cadastrado com sucesso")  
                    cadastro = False
                    break
                
                except ValueError:
                    sg.popup("Erro", "Enfermeiro já cadastrado!")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro()
                    break

    def listar_enfermeiros(self):
        if self.__enfermeiros == []:
            sg.popup("Erro", "Ainda não há enfermeiros cadastrados")
        else:
            for enfermeiro in self.__pacientes:
                self.__tela_listagem.init_components(enfermeiro, "enfermeiro")
                self.__tela_listagem.open()
                self.__tela_listagem.close()

    def listar_pacientes(self):
        enfermeiro = self.busca_enfermeiro()
        if enfermeiro == None:
            self.__tela_enfermeiro.pega_opcao_enfermeiro_sem_cadastro()
        elif len(enfermeiro.lista_pacientes) == 0:
            self.__tela_enfermeiro.mostra_pacientes(None)
        else:
            self.__tela_enfermeiro.mostra_pacientes(enfermeiro.lista_pacientes)

    def buscar_enfermeiro(self):
        button, value = self.__tela_bucar_enfermeiro.open()
        self.__tela_bucar_paciente.close()
        if button == "Sair":
            self.controlador_sistema.tela_sistema()
        else:
            id = value[0]
            if id.isalpha():
                for paciente in self.__pacientes:
                    if paciente.nome == value[0]:
                        return paciente
                return None
            else:
                for paciente in self.__pacientes:
                    if paciente.cpf == id:
                        return paciente
                return None

    def pega_nome_enfermeiro(self):
        estilo.clear()
        nome = self.__tela_enfermeiro.busca_enfermeiro_nome()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.nome == nome:
                return enfermeiro
        return None

    def pega_cpf_enfermeiro(self):
        estilo.clear()
        cpf = self.__tela_enfermeiro.busca_enfermeiro_cpf()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.cpf == cpf:
                return enfermeiro
        return None

    def pega_coren_enfermeiro(self):
        coren = self.__tela_enfermeiro.busca_enfermeiro_coren()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.coren == coren:
                return enfermeiro
        return None

    def busca_enfermeiro(self):
        estilo.clear()
        tipo_busca = self.__tela_enfermeiro.mostra_opcao_busca()
        opcao_busca = {1: self.pega_nome_enfermeiro, 2: self.pega_cpf_enfermeiro, 3: self.pega_coren_enfermeiro}
        enfermeiro_escolhido = opcao_busca[tipo_busca]()
        return enfermeiro_escolhido

    def busca_dado_enfermeiro(self):
        estilo.clear()
        enfermeiro = self.busca_enfermeiro()
        if enfermeiro == None:
            opcao = self.__tela_enfermeiro.pega_opcao_enfermeiro_sem_cadastro()
            if opcao == 1:
                enfermeiro = self.inserir_enfermeiro()
                self.__tela_enfermeiro.mostra_enfermeiro(enfermeiro)
            else:
                self.retornar_sistema()
        else:
            self.__tela_enfermeiro.mostra_enfermeiro(enfermeiro)

    def editar_enfermeiro(self):
        enfermeiro = self.busca_enfermeiro()
        if enfermeiro == None:
            opcao = self.__tela_enfermeiro.pega_opcao_enfermeiro_sem_cadastro()
            if opcao == 1:
                enfermeiro = self.inserir_enfermeiro()
                self.__tela_enfermeiro.mostra_enfermeiro(enfermeiro)
            else:
                self.retornar_sistema()
        else:
            estilo.clear()
            dado_novo = self.__tela_enfermeiro.pega_dados_enfermeiro(2)
            if dado_novo[0] == "nome":
                enfermeiro.nome = dado_novo[1]
            elif dado_novo[0] == "telefone":
                enfermeiro.telefone = dado_novo[1]
            elif dado_novo[0] == "cpf":
                enfermeiro.cpf = dado_novo[1]
            else:
                enfermeiro.coren = dado_novo[1]

    def excluir_enfermeiro(self):
        enfermeiro = self.busca_enfermeiro()
        if enfermeiro == None:
            opcao = self.__tela_enfermeiro.pega_opcao_enfermeiro_sem_cadastro()
            if opcao == 1:
                enfermeiro = self.inserir_enfermeiro()
                self.__tela_enfermeiro.mostra_enfermeiro(enfermeiro)
            else:
                self.retornar_sistema()
        else:
            self.__enfermeiros.remove(enfermeiro)
            self.__tela_enfermeiro.mostra_mensagem_enfermeiro_exlcuido()

    def retornar_sistema(self):
        return self.__controlador_sistema

    def abre_tela(self):
        opcoes = {1: self.inserir_enfermeiro, 2: self.listar_enfermeiros, 3: self.editar_enfermeiro,
                  4: self.excluir_enfermeiro, 5: self.busca_dado_enfermeiro, 6: self.listar_pacientes, 7: self.retornar_sistema}
        continua = True
        while continua:
            estilo.clear()
            opcao_selecionada = self.__tela_enfermeiro.mostra_opcoes()
            if opcao_selecionada == 7:
                continua = False
            opcoes[opcao_selecionada]()

