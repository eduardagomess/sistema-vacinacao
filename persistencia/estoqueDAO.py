from entidade.estoque import Estoque
from persistencia.DAO import DAO


class EstoqueDAO(DAO):
    def __init__(self):
        super().__init__('estoque.pkl')

    def add(self, lote, estoque: Estoque):
        if isinstance(estoque.lote, str) and (estoque is not None) and isinstance(estoque, Estoque):
            super().add(estoque.lote, estoque)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
