from tela.tela_paciente.tela_paciente import TelaPaciente
from tela.tela_paciente.tela_inserir_paciente import TelaInserirPaciente
from tela.tela_paciente.tela_busca import TelaBuscaPaciente
from tela.tela_paciente.tela_listagem import TelaListagem
from tela.tela_paciente.tela_opcoes import TelaOpcoes
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

        self.__tele_endereco = TelaEndereco(self)
        self.__controlador_sistema = controlador_sistema

    def inserir_paciente(self, nome, telefone, cpf, bairro, rua, numero, complemento, data_nascimento):
        self.__tela_inserir_paciente.init_components(nome, telefone, cpf, bairro, rua, numero, complemento, data_nascimento)
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
                    sg.Popup("Nome inválido","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(None, dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except NomeInvalido:
                    sg.Popup("Nome inválido","Preencha o nome com no mínimo 5 caracteres")
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
                    sg.Popup("Telefone inválido", "Valor incorreto, insira apenas números")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],None, dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except TelefoneComNumeroInvalido:
                    sg.Popup("Telefone inválido","Valor incorreto, o número deve conter de 10 a 11 digitos (incluíndo DDD)")
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
                    sg.Popup("CPF inválido","Valor incorreto, insira apenas números")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],dados_paciente["telefone"], None, dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except CpfInvalido:
                    sg.Popup("CPF inválido","Valor incorreto, o CPF deve conter 11 digitos, formatação: 12645974944")
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
                    sg.Popup("Nome inválido","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], None, dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except NomeInvalido:
                    sg.Popup("Nome inválido","Preencha o nome com no mínimo 5 caracteres")
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
                    sg.Popup("Nome inválido","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], None, dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except NomeInvalido:
                    sg.Popup("Nome inválido","Preencha o nome com no mínimo 5 caracteres")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], None, dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break

                numero = dados_paciente["numero"] 
                try:
                    if not numero.isdigit():
                        raise Exception
                except Exception:
                    sg.Popup("Número inválido","Valor incorreto, insira apenas números")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], None, dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                
                complemento = dados_paciente["complemento"] 
                try:
                    if not complemento.replace(" ", "").isalnum():
                        raise Exception
                except Exception:
                    sg.Popup("Complemento inválido","Valor incorreto, insira apenas letras e numeros")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], None,dados_paciente["data_nascimento"])
                    break

                data_nascimento = dados_paciente["data_nascimento"]
                try:
                    if not data_nascimento.replace("/", "").isdigit():
                        raise ValueError
                except ValueError:
                    sg.Popup("Data inválida","Valor incorreto, insira apenas números, com a seguite formatação: DD/MM/AAAA")
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
                    return novo_paciente
                    #break
                except ValueError:
                    sg.popup("Erro", "Paciente já cadastrado!")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente()
                    break
                
    def listar_pacientes(self):
        if self.__pacientes == []:
            sg.popup("Erro", "Ainda não há pacientes cadastrados")
        else:
            self.__tela_listagem.init_components(self.__pacientes, "paciente")
            self.__tela_listagem.open()
            self.__tela_listagem.close()

    def buscar_paciente(self):
        self.__tela_bucar_paciente.init_components()
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
            sg.popup("Erro", "Paciente não cadastrado", "Faça o cadastro!")
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
            self.__tela_opcoes_mudanca.close()
            print(value)
            if value["nome"]:
                self.__tela_inserir_paciente.init_components(None, paciente.telefone, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento, paciente.data_nascimento)
                button, dados_paciente = self.__tela_inserir_paciente.open()
                nome = dados_paciente["nome"]
                try:
                    if not nome.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(nome.replace(" ", "")) < 5:
                        raise NomeInvalido  
                except NomeComCaracterNumerico:
                    sg.Popup("Nome inválido","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(None, paciente.telefone, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento, paciente.data_nascimento)
                   
                except NomeInvalido:
                    sg.Popup("Nome inválido","Preencha o nome com no mínimo 5 caracteres")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(None, paciente.telefone, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento, paciente.data_nascimento)

                paciente.nome = nome
                self.__tela_inserir_paciente.close() 
               

            if value["telefone"]:
                self.__tela_inserir_paciente.init_components(paciente.nome, None, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento, paciente.data_nascimento)
                button, dados_paciente = self.__tela_inserir_paciente.open()
                print(dados_paciente["telefone"])
                telefone = dados_paciente["telefone"]
                try:
                    if not telefone.isdigit():
                        raise CaracterAlfabeticoExcecao
                    elif len(telefone) < 10 or (len(telefone) > 13):
                        raise TelefoneComNumeroInvalido
                except CaracterAlfabeticoExcecao:
                    sg.Popup("Telefone inválido",  "Valor incorreto, insira apenas números")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,None, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                except TelefoneComNumeroInvalido:
                    sg.Popup("Telefone inválido", "Valor incorreto, o número deve conter de 10 a 11 digitos (incluíndo DDD)")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,None, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                telefone = dados_paciente["telefone"]
                paciente.telefone = telefone
                self.__tela_inserir_paciente.close()
                
            
            if value["cpf"]:
                self.__tela_inserir_paciente.init_components(paciente.nome, paciente.telefone, None, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                button, dados_paciente = self.__tela_inserir_paciente.open()
                cpf = dados_paciente["cpf"]
                try:
                    if not cpf.isdigit():
                        raise CaracterAlfabeticoExcecao
                    elif len(cpf) != 11:
                        raise CpfInvalido
                except CaracterAlfabeticoExcecao:
                    sg.Popup("CPF inválido","Valor incorreto, insira apenas números")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome, paciente.telefone, None, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                       
                except CpfInvalido:
                    sg.Popup("CPF inválido","Valor incorreto, o CPF deve conter 11 digitos, formatação: 12645974944")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome, paciente.telefone, None, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                paciente.cpf = cpf
                self.__tela_inserir_paciente.close()
                
                
            if value["endereco"]:
                self.__tela_inserir_paciente.init_components(paciente.nome, paciente.telefone, paciente.cpf, None, None, None, None, paciente.data_nascimento)
                button, dados_paciente = self.__tela_inserir_paciente.open()
                bairro = dados_paciente["bairro"]
                try:
                    if not bairro.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(bairro.replace(" ", "")) < 5:
                        raise NomeInvalido 
                except NomeComCaracterNumerico:
                    sg.Popup("Nome inválido""Valor incorreto, insira apenas letras")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome, paciente.telefone, paciente.cpf, None, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                except NomeInvalido:
                    ssg.Popup("Nome inválido","Preencha o nome com no mínimo 5 caracteres")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,paciente.telefone, paciente.cpf, None,paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                paciente.endereco.bairro = bairro
                self.__tela_inserir_paciente.close()

                rua = dados_paciente["rua"]  
                try:
                    if not rua.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(rua.replace(" ", "")) < 5:
                        raise NomeInvalido
                except NomeComCaracterNumerico:
                    sg.Popup("Nome inválido","Valor incorreto, insira apenas letras")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,paciente.telefone, paciente.cpf, dados_paciente["bairro"], None, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                except NomeInvalido:
                    sg.Popup("Nome inválido","Preencha o nome com no mínimo 5 caracteres")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,paciente.telefone, paciente.cpf, pacinete.endereco.bairro, None, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                paciente.endereco.rua = rua
                self.__tela_inserir_paciente.close()


                numero = dados_paciente["numero"] 
                try:
                    if not numero.isdigit():
                        raise Exception
                except Exception:
                    sg.Popup("Número inválido","Valor incorreto, insira apenas números")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,paciente.telefone, paciente.cpf, pacinete.endereco.bairro, paciente.endereco.rua, None,paciente.endereco.complemento,paciente.data_nascimento)
                       
                paciente.endereco.numero = numero
                self.__tela_inserir_paciente.close()

                complemento = dados_paciente["complemento"] 
                try:
                    if not complemento.replace(" ", "").isalnum():
                        raise Exception
                except Exception:
                    sg.Popup("Complemento Inválido","Valor incorreto, insira apenas letras e numeros")
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,paciente.telefone, paciente.cpf, pacinete.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, None,paciente.data_nascimento)
                    

                paciente.endereco.complemento = numero
                self.__tela_inserir_paciente.close()
                
                data_nascimento = dados_paciente["data_nascimento"]
                if value["data_nascimento"]:
                    try:
                        if not data_nascimento.replace("/", "").isdigit():
                            raise ValueError
                    except ValueError:
                        sg.Popup("Data inválida","Valor incorreto, insira apenas números, com a seguite formatação: DD/MM/AAAA")
                        self.__tela_inserir_paciente.close()
                        self.inserir_paciente(paciente.nome,paciente.telefone, paciente.cpf, pacinete.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento, None)
                        
                    
                    paciente.data_nascimento = data_nascimento
                    self.__tela_inserir_paciente.close()

    def excluir_paciente(self):
        paciente = self.buscar_paciente()
        if paciente == None:
            sg.popup("Erro", "Paciente não cadastrado")
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
                break
            else:
                index= 1
                for i in values.values():
                    if i:
                        if index == 1:
                            opcoes[index](None, None, None, None, None, None, None, None) 
                        else:
                            opcoes[index]()
                    index += 1
        