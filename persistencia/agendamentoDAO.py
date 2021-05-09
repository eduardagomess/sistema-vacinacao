from entidade.agendamento import Agendamento
import pickle


class AgendamentoDAO:

    def __init__(self):
        self.__data_source = "agendamentos.pkl"
        self.__cache = Agendamento()
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__data_source, "wb"))

    def __load(self):
        self.__cache = pickle.load(open(self.__data_source, "rb"))

    def save(self):
        print("ta no save")
        print(self.__cache.agendamentos)
        self.__dump()

    def get(self):
        return self.__cache