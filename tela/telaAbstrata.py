from abc import ABC, abstractmethod

class AbstractTela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def verifica_num(self, mensagem: str = "", inteiros_validos: [] = None):
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
