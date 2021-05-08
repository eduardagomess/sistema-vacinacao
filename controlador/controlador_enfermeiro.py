from entidade.enfermeiro import Enfermeiro
from tela.tela_enfermeiro.tela_inserir_enfermeiro import TelaInserirEnfermeiro
from tela.tela_listagem import TelaListagem
from tela.tela_enfermeiro.tela_busca_enf import TelaBuscaEnfermeiro
from tela.tela_enfermeiro.tela_op_mudanca import TelaOpcoesMudanca
from tela.tela_enfermeiro.tela_enfermeiro import TelaEnfermeiro
from utils import estilo
import PySimpleGUI as sg


class ControladorEnfermeiro:

    def __init__(self, controlador_sistema):
        self.__enfermeiros = []
        self.__tela_enfermeiro = TelaEnfermeiro(self)
        self.__tela_inserir_enfermeiro = TelaInserirEnfermeiro(self)
        self.__tela_buscar_enfermeiro = TelaBuscaEnfermeiro(self)
        self.__tela_listagem = TelaListagem(self)
        self.__tela_opcao_mudanca = TelaOpcoesMudanca(self)
        self.__controlador_sistema = controlador_sistema

    def inserir_enfermeiro(self, nome, telefone, cpf, coren):
        self.__tela_inserir_enfermeiro.init_components(nome, telefone, cpf, coren)
        button, dados_enfermeiro = self.__tela_inserir_enfermeiro.open()
        cadastrado = True
         
        if button == 'Salvar':
            while cadastrado:
                nome = dados_enfermeiro["nome"]
                try:
                    if not nome.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(nome.replace(" ", "")) < 5:
                        raise NomeInvalido  
                except NomeComCaracterNumerico:
                    sg.Popup("Nome inválido","Valor incorreto, insira apenas letras", size=(20,20))
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
                
                coren = dados_enfermeiro["coren"] 
                try:
                    if not coren.isdigit():
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
                    sg.popup("Cadastramento", "Enfermeiro cadastrado com sucesso!")  
                    cadastro = False
                    return novo_enfermeiro
                
                except ValueError:
                    sg.popup("Erro", "Enfermeiro já cadastrado!")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro()
                    break

    def listar_enfermeiros(self):
        if self.__enfermeiros == []:
            sg.popup("Erro", "Ainda não há enfermeiros cadastrados!")
        else:
            self.__tela_listagem.init_components(self.__enfermeiros, "enfermeiro")
            self.__tela_listagem.open()
            self.__tela_listagem.close()

    def listar_pacientes(self):
        enfermeiro = self.buscar_enfermeiro()
        if enfermeiro == None:
            sg.popup("Erro", "Enfermeiro não cadastrado", "Faça o cadastro!")
        elif len(enfermeiro.lista_pacientes) == 0:
            sg.popup("Erro", "Enfermeiro sem pacientes")
        else:
            for paciente in enfermeiro.lista_pacientes:
                sg.print(paciente.nome)
    
    def buscar_enfermeiro(self):
        button, value = self.__tela_buscar_enfermeiro.open()
        self.__tela_buscar_enfermeiro.close()
        id = value[0]
        try:
            if not id.isdigit():
                raise Exception
        except Exception:
            sg.Popup("Número inválido","Insira apenas números")
            self.busca_enfermeiro()
        if button == "Sair":
            self.controlador_sistema.tela_sistema()
        else:
            for enfermeiro in self.__enfermeiros:
                if enfermeiro.coren == id:
                    return enfermeiro
            return None

    def busca_enfermeiro(self):
        enfermeiro = self.buscar_enfermeiro()
        if enfermeiro == None:
            sg.popup("Erro", "Enfermeiro não cadastrado", "Faça o cadastro!")
        else:
            self.__tela_listagem.init_components(enfermeiro, "enfermeiro")
            self.__tela_listagem.open()
            self.__tela_listagem.close()

    def editar_enfermeiro(self):
        enfermeiro = self.buscar_enfermeiro()
        if enfermeiro == None:
            sg.popup("Erro","Enfermeiro não cadastrado")      
        else:
            button, value = self.__tela_opcao_mudanca.open()
            self.__tela_opcao_mudanca.close()
            if value["nome"]:
                self.__tela_inserir_enfermeiro.init_components(None, enfermeiro.telefone, enfermeiro.cpf, enfermeiro.coren)
                button, dados_enfermeiro = self.__tela_inserir_enfermeiro.open()
                nome = dados_enfermeiro["nome"]
                try:
                    if not nome.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(nome.replace(" ", "")) < 5:
                        raise NomeInvalido  
                except NomeComCaracterNumerico:
                    sg.Popup("Nome inválido","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro(None, enfermeiro.telefone, enfermeiro.cpf, enfermeiro.coren)
                except NomeInvalido:
                    sg.Popup("Nome inválido","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro(None, enfermeiro.telefone, enfermeiro.cpf, enfermeiro.coren)

                enfermeiro.nome = nome
                self.__tela_inserir_enfermeiro.close() 
               
            if value["telefone"]:
                self.__tela_inserir_enfermeiro.init_components(enfermeiro.nome, None, enfermeiro.cpf,enfermeiro.coren)
                button, dados_enfermeiro = self.__tela_inserir_enfermeiro.open()
                telefone = dados_enfermeiro["telefone"]
                try:
                    if not telefone.isdigit():
                        raise CaracterAlfabeticoExcecao
                    elif len(telefone) < 10 or (len(telefone) > 13):
                        raise TelefoneComNumeroInvalido
                except CaracterAlfabeticoExcecao:
                    sg.Popup("Telefone inválido",  "Valor incorreto, insira apenas números")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro(enfermeiro.nome, None, enfermeiro.cpf,enfermeiro.coren)
                        
                except TelefoneComNumeroInvalido:
                    sg.Popup("Telefone inválido", "Valor incorreto, o número deve conter de 10 a 11 digitos (incluíndo DDD)")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(enfermeiro.nome, None, enfermeiro.cpf,enfermeiro.coren)
                        
                telefone = dados_enfermeiro["telefone"]
                enfermeiro.telefone = telefone
                self.__tela_inserir_enfermeiro.close()
                
            
            if value["cpf"]:
                self.__tela_inserir_enfermeiro.init_components(enfermeiro.nome, enfermeiro.telefone, None, enfermeiro.coren)
                button, dados_enfermeiro = self.__tela_inserir_enfermeiro.open()
                cpf = dados_enfermeiro["cpf"]
                try:
                    if not cpf.isdigit():
                        raise CaracterAlfabeticoExcecao
                    elif len(cpf) != 11:
                        raise CpfInvalido
                except CaracterAlfabeticoExcecao:
                    sg.Popup("CPF inválido","Valor incorreto, insira apenas números")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro(enfermeiro.nome, enfermeiro.telefone, None, enfermeiro.coren)
                       
                except CpfInvalido:
                    sg.Popup("CPF inválido","Valor incorreto, o CPF deve conter 11 digitos, formatação: 12645974944")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro(enfermeiro.nome, enfermeiro.telefone, None, enfermeiro.coren)
                        
                enfermeiro.cpf = cpf
                self.__tela_inserir_enfermeiro.close()

                coren = dados_enfermeiro["coren"] 
                try:
                    if not coren.isdigit():
                        raise Exception
                except Exception:
                    sg.Popup("Coren inválido","Insira apenas números")
                    self.__tela_inserir_enfermeiro.close()
                    self.inserir_enfermeiro(enfermeiro.nome, enfermeiro.telefone, enfermeiro.cpf,enfermeiro.coren)
                       
                enfermeiro.coren = coren
                self.__tela_inserir_enfermeiro.close()
        
    def excluir_enfermeiro(self):
        enfermeiro = self.buscar_enfermeiro()
        if enfermeiro == None:
            sg.popup("Erro", "Enfermeiro não cadastrado!")
        else:
            self.__enfermeiros.remove(enfermeiro)
            sg.popup("Remoção", "Enfermeiro removido com sucesso!")

    def retornar_sistema(self):
        return self.__controlador_sistema

    def abre_tela(self):
        opcoes = {1: self.inserir_enfermeiro, 2: self.listar_enfermeiros, 3: self.editar_enfermeiro,
                  4: self.excluir_enfermeiro, 5: self.busca_enfermeiro, 6: self.listar_pacientes, 7: self.retornar_sistema}
        while True:
            button, values = self.__tela_enfermeiro.open()
            if button == "Sair":
                break
            else:
                index= 1
                for i in values.values():
                    if i:
                        if index == 1:
                            opcoes[index](None, None, None, None) 
                        else:
                            opcoes[index]()
                    index += 1

