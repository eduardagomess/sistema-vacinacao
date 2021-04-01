from abc import ABC, abstractmethod

class AbstractTela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def pegar_opcao(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = int(input(mensagem))
            try:
                if inteiros_validos and valor_lido not in inteiros_validos:
                    raise ValueError
                return valor_lido
            except ValueError:
                print("Valor incorreto, digite um valor numérico inteiro válido")
                if inteiros_validos:
                    print("Valores válidos: ", inteiros_validos)

    def pegar_nome(self,  mensagem: str = ""):
        while True:
            nome = input(mensagem)
            try:
                if not nome.replace(" ", "").isalpha():
                    raise Exception
                return nome.title()
            except Exception:
                print("Valor incorreto, insira apenas letras")

    def pegar_telefone(self,  mensagem: str = ""):
        while True:
            telefone = input(mensagem)
            try:
                if not telefone.isdigit():
                    raise Exception
                return int(telefone)
            except Exception:
                print("Valor incorreto, insira o telfone com a seguinte formatação: DDXXXXXXXXXX")

    def pegar_cpf(self, mensagem: str = ""):
        while True:
            cpf = input(mensagem)
            try:
                if not cpf.isdigit():
                    raise Exception
                return int(cpf)
            except Exception:
                print("Valor incorreto, insira apenas números, formatação: 12645974944")

    def pegar_data_nascimento(self, mensagem: str = ""):
        while True:
            data_nascimento = input(mensagem)
            try:
                if not data_nascimento.replace("/", "").isdigit():
                    raise Exception
                return data_nascimento
            except Exception:
                print("Valor incorreto, insira apenas números, com a seguite formatação: DD/MM/AAAA")

    def pegar_complemento(self, mensagem: str = ""):
        while True:
            complemento = input(mensagem)
            try:
                if not complemento.replace(" ", "").isalnum():
                    raise Exception
                return complemento.title()
            except Exception:
                print("Valor incorreto, insira apenas letras e numeros")

    def pegar_num(self, mensagem: str = ""):
        while True:
            numero = input(mensagem)
            try:
                if not numero.isdigit():
                    raise Exception
                return numero
            except Exception:
                print("Valor incorreto, insira apenas números")








