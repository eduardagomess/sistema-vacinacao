from abc import ABC, abstractmethod
from excecao.nome_invalido import NomeInvalido
from excecao.caracter_alfabetico import CaracterAlfabeticoExcecao
from excecao.dose_invalida import DoseInvalida
import datetime
import PySimpleGUI as sg


class AbstractTela(ABC):

    @abstractmethod
    def __init__(self):
        self.__window = None

    def pegar_nome_vacina(self, mensagem: str = ""):
        nome_vacina = str(mensagem)
        try:
            nome_vacina.replace(" ", "")
            if len(nome_vacina) < 5:
                raise NomeInvalido
            return nome_vacina.title()
        except NomeInvalido:
            sg.popup("Preencha o nome com no mínimo 5 caracteres")
            return False

    def pegar_quantidade(self, msg: str = ""):
        qtd = msg
        try:
            if not qtd.isdigit():
                raise CaracterAlfabeticoExcecao
            return qtd
        except CaracterAlfabeticoExcecao:
            sg.popup("Quantidade deve conter apenas números!")
            return False

    def pegar_dose_vacina(self, mensagem: str = ""):
        valor_lido = mensagem
        try:
            if not valor_lido.isdigit():
                raise CaracterAlfabeticoExcecao
            elif int(valor_lido) not in [1, 2]:
                raise DoseInvalida
            return valor_lido
        except CaracterAlfabeticoExcecao:
            sg.popup("Valor incorreto, digite um valor numérico inteiro válido (1 ou 2)")
            return False
        except DoseInvalida:
            sg.popup("Valor incorreto, insira apenas números (1 ou 2)")
            return False

    def pegar_data_nascimento(self, mensagem: str = ""):
        data_nascimento = mensagem
        formatacao = "%d/%m/%Y"
        try:
            datetime.datetime.strptime(data_nascimento, formatacao)
            return data_nascimento
        except ValueError:
            sg.popup("Valor incorreto, insira apenas números, com a seguite formatação: DD/MM/AAAA")
            return False

    def pegar_complemento(self, mensagem: str = ""):
        while True:
            complemento = input(mensagem)
            try:
                if not complemento.replace(" ", "").isalnum():
                    raise Exception
                return complemento.title()
            except Exception:
                print(self.colorir_erro("Valor incorreto, insira apenas letras e numeros"))

    def open(self):
        pass

    def close(self):
        pass

    def msg(self, msg):
        sg.popup_ok(msg)
