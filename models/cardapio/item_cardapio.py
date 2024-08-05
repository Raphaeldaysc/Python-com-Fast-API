from abc import ABC, abstractmethod


class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return f"Nome: {self._nome} - Preço: {self._preco}"

    @abstractmethod
    def aplicar_desconto(self):
        pass
