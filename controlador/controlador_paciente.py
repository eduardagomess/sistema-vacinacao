from tela.tela_paciente.tela_paciente import TelaPaciente
from tela.tela_paciente.tela_inserir_paciente import TelaInserirPaciente
from tela.tela_paciente.tela_busca import TelaBuscaPaciente
from tela.tela_paciente.tela_listagem import TelaListagem
from tela.tela_paciente.tela_opcoes import TelaOpcoes
from tela.tela_paciente.tela_editar_paciente import TelaEditarPaciente
from tela.tela_endereco.tela_endereco import TelaEndereco
from entidade.paciente import Paciente
from excecao.nome_invalido import NomeInvalido
from excecao.caracter_numerico import NomeComCaracterNumerico
from excecao.caracter_alfabetico import CaracterAlfabeticoExcecao
from excecao.telefone_invalido import TelefoneComNumeroInvalido
from excecao.coren_invalido import CorenInvalido
from excecao.cpf_invalido import CpfInvalido
from excecao.dose_invalida import DoseInvalida
import PySimpleGUI as sg



class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self.__pacientes = []
        self.__tela_paciente = TelaPaciente(self)
        self.__tela_inserir_paciente = TelaInserirPaciente(self)
        self.__tela_bucar_paciente = TelaBuscaPaciente(self)
        self.__tela_listagem = TelaListagem(self)
        self.__tela_opcoes_mudanca = TelaOpcoes(self)
        self.__tela_editar = TelaEditarPaciente(self)
        self.__tele_endereco = TelaEndereco(self)
        self.__controlador_sistema = controlador_sistema

    def inserir_paciente(self, nome, telefone, cpf, bairro, rua, numero, complemento, nascimento):
        self.__tela_inserir_paciente.init_components(nome, telefone, cpf, bairro, rua, numero, complemento, nascimento)
        button, dados_paciente = self.__tela_inserir_paciente.open()
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
                    sg.Popup("Erro","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(None, dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except NomeInvalido:
                    sg.Popup("Erro","Preencha o nome com no mínimo 5 caracteres")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(None, dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                
                telefone = dados_paciente["telefone"]
                try:
                    if not telefone.isdigit():
                        raise CaracterAlfabeticoExcecao
                    elif len(telefone) < 10 or (len(telefone) > 13):
                        raise TelefoneComNumeroInvalido
                except CaracterAlfabeticoExcecao:
                    sg.Popup("Erro", "Valor incorreto, insira apenas números")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],None, dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except TelefoneComNumeroInvalido:
                    sg.Popup("Erro","Valor incorreto, o número deve conter de 10 a 11 digitos (incluíndo DDD)")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],None, dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                
                cpf = dados_paciente["cpf"]
                try:
                    if not cpf.isdigit():
                        raise CaracterAlfabeticoExcecao
                    elif len(cpf) != 11:
                        raise CpfInvalido
                except CaracterAlfabeticoExcecao:
                    sg.Popup("Erro","Valor incorreto, insira apenas números")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],dados_paciente["telefone"], None, dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except CpfInvalido:
                    sg.Popup("Erro","Valor incorreto, o CPF deve conter 11 digitos, formatação: 12645974944")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],dados_paciente["telefone"], None, dados_paciente["data_nascimento"])
                    break
                
                bairro = dados_paciente["bairro"]
                try:
                    if not bairro.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(bairro.replace(" ", "")) < 5:
                        raise NomeInvalido 
                except NomeComCaracterNumerico:
                    sg.Popup("Erro","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], None, dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except NomeInvalido:
                    sg.Popup("Erro","Preencha o nome com no mínimo 5 caracteres")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], None, dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break

                rua = dados_paciente["rua"]  
                try:
                    if not rua.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(rua.replace(" ", "")) < 5:
                        raise NomeInvalido
                except NomeComCaracterNumerico:
                    sg.Popup("Erro","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], None, dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except NomeInvalido:
                    sg.Popup("Erro","Preencha o nome com no mínimo 5 caracteres")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], None, dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break

                numero = dados_paciente["numero"] 
                try:
                    if not numero.isdigit():
                        raise Exception
                except Exception:
                    sg.Popup("Erro","Valor incorreto, insira apenas números")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], None, dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                
                complemento = dados_paciente["complemento"] 
                try:
                    if not complemento.replace(" ", "").isalnum():
                        raise Exception
                except Exception:
                    sg.Popup("Erro","Valor incorreto, insira apenas letras e numeros")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], None,dados_paciente["data_nascimento"])
                    break

                data_nascimento = dados_paciente["data_nascimento"]
                try:
                    if not data_nascimento.replace("/", "").isdigit():
                        raise ValueError
                except ValueError:
                    sg.Popup("Erro","Valor incorreto, insira apenas números, com a seguite formatação: DD/MM/AAAA")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],dados_paciente["telefone"],dados_paciente["cpf"],  dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], None)
                    break
                
                try:
                    for paciente in self.__pacientes:
                        if paciente.cpf == dados_paciente["cpf"]:
                                raise ValueError
                    novo_paciente = Paciente(nome, telefone, cpf, data_nascimento)
                    novo_paciente.determinar_endereco(bairro, rua, numero,complemento)
                    self.__pacientes.append(novo_paciente)
                    self.__tela_inserir_paciente.close()
                    sg.popup("Cadastramento", "Paciente cadastrado com sucesso")  
                    cadastro = False
                    break
                except ValueError:
                    sg.popup("Erro", "Paciente já cadastrado!")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente()
                    break
                
       
    def listar_pacientes(self):
        if self.__pacientes == []:
            sg.popup("Erro", "Ainda não há pacientes cadastrados")
        else:
            for paciente in self.__pacientes:
                self.__tela_listagem.init_components(paciente, "paciente")
                self.__tela_listagem.open()
                self.__tela_listagem.close()

    def buscar_paciente(self):
        button, value = self.__tela_bucar_paciente.open()
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

    def busca_paciente(self):
        paciente = self.buscar_paciente()
        if paciente == None:
            self.__tela_inserir_paciente.open()
        else:
            self.__tela_listagem.init_components(paciente, "paciente")
            self.__tela_listagem.open()
            self.__tela_listagem.close()

    def editar_paciente(self):
        paciente = self.buscar_paciente()
        if paciente == None:
            sg.popup("Erro","Paciente não cadastrado")
            self.__tela_opcoes.close()
        else:
            button, value = self.__tela_opcoes_mudanca.open()
            if value["nome"]:
                self.__tela_inserir_paciente.init_components(None, paciente.telefone, paciente.cpf, paciente.bairro, paciente.rua, paciente.numero, paciente.complemento, paciente.nascimento)
                button, dados_paciente = self.__tela_inserir_paciente.open()
                
                nome = dados_paciente["nome"]
                try:
                    if not nome.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(nome.replace(" ", "")) < 5:
                        raise NomeInvalido  
                except NomeComCaracterNumerico:
                    sg.Popup("Erro","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(None, dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except NomeInvalido:
                    sg.Popup("Erro","Preencha o nome com no mínimo 5 caracteres")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(None, dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                paciente.nome = nome
                self.__tela_inserir_paciente.close()
            
            self.__tela_inserir_paciente.init_components(paciente.nome, None, paciente.cpf, paciente.bairro, paciente.rua, paciente.numero, paciente.complemento, paciente.nascimento)
            button, dados_paciente = self.__tela_inserir_paciente.open()
            telefone = dados_paciente["telefone"]
            if value["telefone"]:
                try:
                    if not telefone.isdigit():
                        raise CaracterAlfabeticoExcecao
                    elif len(telefone) < 10 or (len(telefone) > 13):
                        raise TelefoneComNumeroInvalido
                except CaracterAlfabeticoExcecao:
                    sg.Popup("Erro", "Valor incorreto, insira apenas números")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],None, dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except TelefoneComNumeroInvalido:
                    sg.Popup("Erro","Valor incorreto, o número deve conter de 10 a 11 digitos (incluíndo DDD)")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],None, dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                paciente.telefone = telefone
                self.__tela_inserir_paciente.close()
            
            cpf = dados_paciente["cpf"]
            if value["cpf"]:
                self.__tela_inserir_paciente.init_components(paciente.nome, paciente.telefone, None, paciente.bairro, paciente.rua, paciente.numero, paciente.complemento, paciente.nascimento)
                button, dados_paciente = self.__tela_inserir_paciente.open()
                try:
                    if not cpf.isdigit():
                        raise CaracterAlfabeticoExcecao
                    elif len(cpf) != 11:
                        raise CpfInvalido
                except CaracterAlfabeticoExcecao:
                    sg.Popup("Erro","Valor incorreto, insira apenas números")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],dados_paciente["telefone"], None, dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except CpfInvalido:
                    sg.Popup("Erro","Valor incorreto, o CPF deve conter 11 digitos, formatação: 12645974944")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],dados_paciente["telefone"], None, dados_paciente["data_nascimento"])
                    break
                paciente.cpf = cpf
                self.__tela_inserir_paciente.close()
            
            
            if value["endereco"]:
                self.__tela_inserir_paciente.init_components(paciente.nome, paciente.telefone, paciente.cpf, None, None, None, None, paciente.nascimento)
                button, dados_paciente = self.__tela_inserir_paciente.open()
                bairro = dados_paciente["bairro"]
                try:
                    if not bairro.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(bairro.replace(" ", "")) < 5:
                        raise NomeInvalido 
                except NomeComCaracterNumerico:
                    sg.Popup("Erro","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome, paciente.telefone, paciente.cpf, None, dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except NomeInvalido:
                    sg.Popup("Erro","Preencha o nome com no mínimo 5 caracteres")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], None, dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break

                rua = dados_paciente["rua"]  
                try:
                    if not rua.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(rua.replace(" ", "")) < 5:
                        raise NomeInvalido
                except NomeComCaracterNumerico:
                    sg.Popup("Erro","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], None, dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except NomeInvalido:
                    sg.Popup("Erro","Preencha o nome com no mínimo 5 caracteres")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], None, dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break

                numero = dados_paciente["numero"] 
                try:
                    if not numero.isdigit():
                        raise Exception
                except Exception:
                    sg.Popup("Erro","Valor incorreto, insira apenas números")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], None, dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                
                complemento = dados_paciente["complemento"] 
                try:
                    if not complemento.replace(" ", "").isalnum():
                        raise Exception
                except Exception:
                    sg.Popup("Erro","Valor incorreto, insira apenas letras e numeros")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], None,dados_paciente["data_nascimento"])
                    break

                paciente.determinar_endereco(value["bairro"], value["rua"], value["numero"], value["complemento"]) 
                self.__tele_endereco.close()
            
            data_nascimento = dados_paciente["data_nascimento"]
            if value["data_nascimento"]:
                try:
                    if not data_nascimento.replace("/", "").isdigit():
                        raise ValueError
                except ValueError:
                    sg.Popup("Erro","Valor incorreto, insira apenas números, com a seguite formatação: DD/MM/AAAA")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],dados_paciente["telefone"],dados_paciente["cpf"],  dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], None)
                    break
                
                paciente.data_nascimento = data_nascimento
                self.__tela_inserir_paciente.close()
            

    def excluir_paciente(self):
        paciente = self.buscar_paciente()
        if paciente == None:
            self.__tela_inserir_paciente.open()
            self.__tela_inserir_paciente.close()
        else:
            self.__pacientes.remove(paciente)
            sg.popup("Remoção", "Paciente removido com sucesso!")

    def retornar_sistema(self):
        return self.__controlador_sistema
       
    def abre_tela(self):
        opcoes = {1: self.inserir_paciente, 2: self.listar_pacientes, 3: self.editar_paciente, 4: self.excluir_paciente, 5: self.busca_paciente}
        while True:
            button, values = self.__tela_paciente.open()
            if button == "Sair":
                print("entrou no if")
                print(button)
                break
            else:
                count = 1
                for i in values.values():
                    if i:
                        if count == 1:
                            opcoes[count](None, None, None, None, None, None, None, None) 
                        else:
                             opcoes[count]()

                    count += 1
        