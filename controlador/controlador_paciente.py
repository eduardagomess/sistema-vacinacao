from tela.tela_paciente.tela_paciente import TelaPaciente
from tela.tela_paciente.tela_inserir_paciente import TelaInserirPaciente
from tela.tela_paciente.tela_busca import TelaBuscaPaciente
from tela.tela_listagem import TelaListagem
from tela.tela_paciente.tela_opcoes import TelaOpcoes
from tela.tela_endereco.tela_endereco import TelaEndereco
from entidade.paciente import Paciente
from excecao.nome_invalido import NomeInvalido
from excecao.caracter_numerico import NomeComCaracterNumerico
from excecao.caracter_alfabetico import CaracterAlfabeticoExcecao
from excecao.telefone_invalido import TelefoneComNumeroInvalido
from excecao.coren_invalido import CorenInvalido
from excecao.cpf_invalido import CpfInvalido
import PySimpleGUI as sg
from persistencia.pacienteDAO import PacienteDAO
import datetime



class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self.__pacienteDAO = PacienteDAO()
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
                    sg.Popup("Nome inválido","Insira apenas letras", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(None, dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except NomeInvalido:
                    sg.Popup("Nome inválido","Preencha o nome com no mínimo 5 caracteres", font=("Helvetica", 15, "bold"), text_color='red')
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
                    sg.Popup("Telefone inválido", "Insira apenas números", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],None, dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except TelefoneComNumeroInvalido:
                    sg.Popup("Telefone inválido","O número deve conter de 10 a 11 digitos (incluíndo DDD)", font=("Helvetica", 15, "bold"), text_color='red')
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
                    sg.Popup("CPF inválido","Insira apenas números",font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],dados_paciente["telefone"], None, dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except CpfInvalido:
                    sg.Popup("CPF inválido","O CPF deve conter 11 digitos, formatação: 12645974944",font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],dados_paciente["telefone"], None,dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                
                bairro = dados_paciente["bairro"]
                try:
                    if not bairro.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(bairro.replace(" ", "")) < 5:
                        raise NomeInvalido 
                except NomeComCaracterNumerico:
                    sg.Popup("Bairro inválido","Insira apenas letras", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], None, dados_paciente["rua"], dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except NomeInvalido:
                    sg.Popup("Bairro inválido","Preencha o nome com no mínimo 5 caracteres", font=("Helvetica", 15, "bold"), text_color='red')
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
                    sg.Popup("Rua inválida","Insira apenas letras", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], None, dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                except NomeInvalido:
                    sg.Popup("Rua inválida","Preencha o nome com no mínimo 5 caracteres", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], None, dados_paciente["numero"], dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break

                numero = dados_paciente["numero"] 
                try:
                    if not numero.isdigit():
                        raise Exception
                except Exception:
                    sg.Popup("Número residencial inválido","Insira apenas números", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], None, dados_paciente["complemento"],dados_paciente["data_nascimento"])
                    break
                
                complemento = dados_paciente["complemento"] 
                try:
                    if not complemento.replace(" ", "").isalnum():
                        raise Exception
                except Exception:
                    sg.Popup("Complemento inválido","Insira apenas letras e numeros", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"], dados_paciente["telefone"], dados_paciente["cpf"], dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"], None,dados_paciente["data_nascimento"])
                    break

                data_nascimento = dados_paciente["data_nascimento"]
                try:
                    formatacao = '%d/%m/%Y'
                    datetime.datetime.strptime(data_nascimento, formatacao)
                except ValueError:
                    sg.Popup("Data inválida","insira apenas números, com a seguite formatação: DD/MM/AAAA", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(dados_paciente["nome"],dados_paciente["telefone"],dados_paciente["cpf"],  dados_paciente["bairro"], dados_paciente["rua"], dados_paciente["numero"],dados_paciente["complemento"], None)
                    break
                try:
                    for paciente in self.__pacienteDAO.get_all():
                        if paciente.cpf == dados_paciente["cpf"]:
                            raise ValueError
                    novo_paciente = Paciente(nome, telefone, cpf, data_nascimento)
                    novo_paciente.determinar_endereco(bairro, rua, numero,complemento)
                    self.__pacienteDAO.add(novo_paciente)
                    self.__tela_inserir_paciente.close()
                    sg.popup("Paciente cadastrado com sucesso", font=("Helvetica", 15, "bold"), text_color='#4682B4') 
                    cadastro = False
                    return novo_paciente
                except ValueError:
                    sg.popup("Erro", "Paciente já cadastrado!", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(None, None, None, None, None, None, None, None)
                    break
        else:
            self.__tela_inserir_paciente.close()

                
    def listar_pacientes(self):
        if self.__pacienteDAO.get_all() == []:
            sg.popup("Erro", "Ainda não há pacientes cadastrados", font=("Helvetica", 15, "bold"), text_color='red')
        else:
            self.__tela_listagem.init_components(self.__pacienteDAO.get_all(), "paciente")
            self.__tela_listagem.open()
            self.__tela_listagem.close()

    def buscar_paciente(self):
        self.__tela_bucar_paciente.init_components()
        button, value = self.__tela_bucar_paciente.open()
        self.__tela_bucar_paciente.close()
        id = value[0]
        if button == "Sair":
            return "Sair"
        else:
            try:
                if not id.isdigit():
                    raise CaracterAlfabeticoExcecao
                elif len(id) != 11:
                    raise CpfInvalido
            except CaracterAlfabeticoExcecao:
                sg.Popup("CPF inválido","Insira apenas números",font=("Helvetica", 15, "bold"), text_color='red')
                self.buscar_paciente()
            except CpfInvalido:
                sg.Popup("CPF inválido","O CPF deve conter 11 digitos, formatação: 12645974944",font=("Helvetica", 15, "bold"), text_color='red')
                self.buscar_paciente()
            for paciente in self.__pacienteDAO.get_all():
                if paciente.cpf == id:
                    return paciente
            return None

    def busca_paciente(self):
        paciente = self.buscar_paciente()
        if paciente == "Sair":
            self.__tela_paciente.close()
            return
        if paciente == None:
            sg.popup("Erro", "Paciente não cadastrado", "Faça o cadastro!", font=("Helvetica", 15, "bold"), text_color='red')
        else:
            self.__tela_listagem.init_components(self.__pacienteDAO.get(paciente), "paciente_relatorio")
            self.__tela_listagem.open()
            self.__tela_listagem.close()

    def editar_paciente(self):
        paciente = self.buscar_paciente()
        if paciente == "Sair":
            self.__tela_paciente.close()
            return
        if paciente == None:
            sg.popup("Erro","Paciente não cadastrado", font=("Helvetica", 15, "bold"), text_color='red')
            self.__tela_opcoes.close()
        else:
            button, value = self.__tela_opcoes_mudanca.open()
            self.__tela_opcoes_mudanca.close()
            if value["nome"]:
                self.__tela_inserir_paciente.init_components(None, paciente.telefone, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento, paciente.data_nascimento)
                button, dados_paciente = self.__tela_inserir_paciente.open()
                self.__tela_inserir_paciente.close()
                nome = dados_paciente["nome"]
                try:
                    if not nome.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(nome.replace(" ", "")) < 5:
                        raise NomeInvalido  
                except NomeComCaracterNumerico:
                    sg.Popup("Nome inválido","Insira apenas letras", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(None, paciente.telefone, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento, paciente.data_nascimento)
                   
                except NomeInvalido:
                    sg.Popup("Nome inválido","Preencha o nome com no mínimo 5 caracteres", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(None, paciente.telefone, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento, paciente.data_nascimento)

                paciente.nome = nome
                self.__pacienteDAO.add(paciente)
                sg.Popup("Nome do paciente alterado com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')
                self.__tela_inserir_paciente.close() 

            if value["telefone"]:
                self.__tela_inserir_paciente.init_components(paciente.nome, None, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento, paciente.data_nascimento)
                button, dados_paciente = self.__tela_inserir_paciente.open()
                telefone = dados_paciente["telefone"]
                try:
                    if not telefone.isdigit():
                        raise CaracterAlfabeticoExcecao
                    elif len(telefone) < 10 or (len(telefone) > 13):
                        raise TelefoneComNumeroInvalido
                except CaracterAlfabeticoExcecao:
                    sg.Popup("Telefone inválido", "Insira apenas números", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,None, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                except TelefoneComNumeroInvalido:
                    sg.Popup("Telefone inválido", "O número deve conter de 10 a 11 digitos (incluíndo DDD)", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,None, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                paciente.telefone = telefone
                self.__pacienteDAO.add(paciente)
                sg.Popup("Telefone do paciente alterado com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')
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
                    sg.Popup("CPF inválido","Insira apenas números", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome, paciente.telefone, None, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                       
                except CpfInvalido:
                    sg.Popup("CPF inválido","O CPF deve conter 11 digitos, formatação: 12645974944", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome, paciente.telefone, None, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                paciente.cpf = cpf
                self.__pacienteDAO.add(paciente)
                sg.Popup("CPF do paciente alterado com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')
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
                    sg.Popup("Bairro inválido", "Insira apenas letras", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome, paciente.telefone, paciente.cpf, None, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                except NomeInvalido:
                    sg.Popup("Nome inválido","Preencha o nome com no mínimo 5 caracteres")

                    sg.Popup("Bairro inválido","Preencha o nome com no mínimo 5 caracteres", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,paciente.telefone, paciente.cpf, None,paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                paciente.endereco.bairro = bairro
                self.__pacienteDAO.add(paciente)
                sg.Popup("Bairro do paciente alterado com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')
                self.__tela_inserir_paciente.close()

                rua = dados_paciente["rua"]  
                try:
                    if not rua.replace(" ", "").isalpha():
                        raise NomeComCaracterNumerico
                    elif len(rua.replace(" ", "")) < 5:
                        raise NomeInvalido
                except NomeComCaracterNumerico:
                    sg.Popup("Rua inválido","Insira apenas letras", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,paciente.telefone, paciente.cpf, dados_paciente["bairro"], None, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                except NomeInvalido:
                    sg.Popup("Rua inválido","Preencha o nome com no mínimo 5 caracteres", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,paciente.telefone, paciente.cpf, paciente.endereco.bairro, None, paciente.endereco.numero, paciente.endereco.complemento,paciente.data_nascimento)
                        
                paciente.endereco.rua = rua
                self.__pacienteDAO.add(paciente)
                sg.Popup("Rua do paciente alterada com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')
                self.__tela_inserir_paciente.close()

                numero = dados_paciente["numero"] 
                try:
                    if not numero.isdigit():
                        raise Exception
                except Exception:
                    sg.Popup("Número residencial inválido","Insira apenas caracteres numéricos", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,paciente.telefone, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, None,paciente.endereco.complemento,paciente.data_nascimento)
                       
                paciente.endereco.numero = numero
                self.__pacienteDAO.add(paciente)
                sg.Popup("Némero residencial alterado com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')
                self.__tela_inserir_paciente.close()

                complemento = dados_paciente["complemento"] 
                try:
                    if not complemento.replace(" ", "").isalnum():
                        raise Exception
                except Exception:
                    sg.Popup("Complemento Inválido","Insira apenas letras e numeros", font=("Helvetica", 15, "bold"), text_color='red')
                    self.__tela_inserir_paciente.close()
                    self.inserir_paciente(paciente.nome,paciente.telefone, paciente.cpf, paciente.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, None,paciente.data_nascimento)
                    
                paciente.endereco.complemento = numero
                self.__pacienteDAO.add(paciente)
                sg.Popup("Complemento alterado com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')
                self.__tela_inserir_paciente.close()
                
                data_nascimento = dados_paciente["data_nascimento"]
                if value["data_nascimento"]:
                    try:
                        if not data_nascimento.replace("/", "").isdigit():
                            raise ValueError
                    except ValueError:
                        sg.Popup("Data inválida","Insira apenas números, com a seguite formatação: DD/MM/AAAA", font=("Helvetica", 15, "bold"), text_color='red')
                        self.__tela_inserir_paciente.close()
                        self.inserir_paciente(paciente.nome,paciente.telefone, paciente.cpf, pacinete.endereco.bairro, paciente.endereco.rua, paciente.endereco.numero, paciente.endereco.complemento, None)     

                    paciente.data_nascimento = data_nascimento
                    self.__pacienteDAO.add(paciente)
                    sg.Popup("Data de nascimento alterado com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')
                    self.__tela_inserir_paciente.close()

    def excluir_paciente(self):
        paciente = self.buscar_paciente()
        if paciente == "Sair":
            self.__tela_paciente.close()
            return
        if paciente == None:
            sg.popup("Erro", "Paciente não cadastrado", font=("Helvetica", 15, "bold"), text_color='red')
        else:
            self.__pacienteDAO.remove(paciente)
            sg.popup("Remoção", "Paciente removido com sucesso!", font=("Helvetica", 15, "bold"), text_color='#4682B4')

    def retornar_sistema(self):
        return self.__controlador_sistema
       
    def abre_tela(self):
        opcoes = {1: self.inserir_paciente, 2: self.listar_pacientes, 3: self.editar_paciente, 4: self.excluir_paciente, 5: self.busca_paciente}
        while True:
            button, values = self.__tela_paciente.open()
            if button == "Sair" or values == None:
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
