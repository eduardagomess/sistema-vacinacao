from abc import ABC, abstractmethod
from excecao.nome_invalido import NomeInvalido
from excecao.caracter_numerico import NomeComCaracterNumerico
from excecao.caracter_alfabetico import CaracterAlfabeticoExcecao
from excecao.telefone_invalido import TelefoneComNumeroInvalido
from excecao.coren_invalido import CorenInvalido
from excecao.cpf_invalido import CpfInvalido
from excecao.dose_invalida import DoseInvalida
import datetime
import PySimpleGUI as sg


class AbstractTela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def colorir_info_correta(self, message: str) -> str:
        return f'\033[32m{message}\033[1m'

    def colorir_info_amotra(self, message: str) -> str:
        return f'\033[30m{message}\033[1m'

    def colorir_aviso(self, message: str) -> str:
        return f'\033[93m{message}\033[0m'

    def colorir_erro(self, message: str) -> str:
        return f'\033[91m{message}\033[0m'

    def colorir_info(self, message: str) -> str:
        return f'\033[96m{message}\033[0m'

    def colorir_titulo(self, message: str) -> str:
        return f'\033[94m{message}\033[0m'

    def colorir_escolha(self, message: str) -> str:
        return f'\033[95m{message}\033[0m'

    def pegar_opcao(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                if valor_lido.isalpha():
                    raise CaracterAlfabeticoExcecao
                elif inteiros_validos and int(valor_lido) not in inteiros_validos:
                    raise ValueError
                return int(valor_lido)
            except CaracterAlfabeticoExcecao:
                print(self.colorir_erro("Valor incorreto, insira apenas números"))
                if inteiros_validos:
                    print(self.colorir_info("Valores válidos: "), (self.colorir_info(inteiros_validos)))
            except ValueError:
                print(self.colorir_erro("Valor incorreto, digite um valor numérico inteiro válido"))
                if inteiros_validos:
                    print(self.colorir_info("Valores válidos: "), (self.colorir_info(inteiros_validos)))

 
  

    def pegar_nome(self,  mensagem: str = ""):
        while True:
            nome = input(mensagem)
            try:
                if not nome.replace(" ", "").isalpha():
                    raise NomeComCaracterNumerico
                elif len(nome.replace(" ", "")) < 5:
                    raise NomeInvalido
                return nome.title()
            except NomeComCaracterNumerico:
                print(self.colorir_erro("Valor incorreto, insira apenas letras"))
            except NomeInvalido:
                print(self.colorir_erro("Preencha o nome com no mínimo 5 caracteres"))

    def pegar_nome_vacina(self, mensagem: str = ""):
        while True:
            nome_vacina = input(mensagem)
            try:
                if len(nome_vacina.replace(" ", "")) < 5:
                    raise NomeInvalido
                return nome_vacina.title()
            except NomeInvalido:
                print(self.colorir_erro("Preencha o nome com no mínimo 5 caracteres"))

    def pegar_telefone(self,  mensagem: str = ""):
        while True:
            telefone = input(mensagem)
            try:
                if not telefone.isdigit():
                    raise CaracterAlfabeticoExcecao
                elif len(telefone) < 10 or (len(telefone) > 13):
                    raise TelefoneComNumeroInvalido
                return int(telefone)
            except CaracterAlfabeticoExcecao:
                print(self.colorir_erro("Valor incorreto, insira apenas números"))
            except TelefoneComNumeroInvalido:
                print(self.colorir_erro("Valor incorreto, o número deve conter de 10 a 11 digitos (incluíndo DDD)"))

    def pegar_cpf(self, mensagem: str = ""):
        while True:
            cpf = input(mensagem)
            try:
                if not cpf.isdigit():
                    raise CaracterAlfabeticoExcecao
                elif len(cpf) != 11:
                    raise CpfInvalido
                return int(cpf)
            except CaracterAlfabeticoExcecao:
                print(self.colorir_erro("Valor incorreto, insira apenas números"))
            except CpfInvalido:
                print(self.colorir_erro("Valor incorreto, o CPF deve conter 11 digitos, formatação: 12645974944"))

    def pegar_data_nascimento(self, mensagem: str = ""):
        while True:
            data_nascimento = input(mensagem)
            formatacao = "%d/%m/%Y"
            try:
                datetime.datetime.strptime(data_nascimento, formatacao)
                return data_nascimento
            except ValueError:
                print(self.colorir_erro("Valor incorreto, insira apenas números, com a seguite formatação: DD/MM/AAAA"))

    def pegar_complemento(self, mensagem: str = ""):
        while True:
            complemento = input(mensagem)
            try:
                if not complemento.replace(" ", "").isalnum():
                    raise Exception
                return complemento.title()
            except Exception:
                print(self.colorir_erro("Valor incorreto, insira apenas letras e numeros"))

    def pegar_num(self, mensagem: str = ""):
        while True:
            numero = input(mensagem)
            try:
                if not numero.isdigit():
                    raise Exception
                return int(numero)
            except Exception:
                print(self.colorir_erro("Valor incorreto, insira apenas números"))

    def pegar_dose(self, mensagem: str = ""):
        while True:
            valor_lido = input(mensagem)
            try:
                if not valor_lido.isdigit():
                    raise CaracterAlfabeticoExcecao
                elif int(valor_lido) not in [0,1,2]:
                    raise DoseInvalida
                return valor_lido
            except CaracterAlfabeticoExcecao:
                print(self.colorir_erro("Valor incorreto, digite um valor numérico inteiro válido (0,1 ou 2)"))
            except DoseInvalida:
                print(self.colorir_erro("Valor incorreto, insira apenas números (0,1 ou 2)"))

    def pegar_dose_vacina(self, mensagem: str = ""):
        while True:
            valor_lido = input(mensagem)
            try:
                if not valor_lido.isdigit():
                    raise CaracterAlfabeticoExcecao
                elif int(valor_lido) not in [1,2]:
                    raise DoseInvalida
                return valor_lido
            except CaracterAlfabeticoExcecao:
                print(self.colorir_erro("Valor incorreto, digite um valor numérico inteiro válido (1 ou 2)"))
            except DoseInvalida:
                print(self.colorir_erro("Valor incorreto, insira apenas números (1 ou 2)"))

    def pegar_coren(self, mensagem: str = ""):
        while True:
            coren= input(mensagem)
            try:
                if not coren.isdigit():
                    raise CaracterAlfabeticoExcecao
                elif len(coren) != 6:
                    raise CorenInvalido
                return int(coren)
            except CaracterAlfabeticoExcecao:
                print(self.colorir_erro("Valor incorreto, insira apenas números"))
            except CorenInvalido:
                print(self.colorir_erro("Valor incorreto, o COREN deve conter 6 digitos, formatação: 123456"))
