from models.avaliacao import Avaliacao
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
from models.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Restaurante {self._nome} - Categoria {self._categoria} - Ativo {self._ativo} - Avaliações{self._avaliacao} - Cardapio {self._cardapio}'

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'Restaurante {
                  restaurante._nome} - Categoria {restaurante._categoria} - {restaurante.ativo} - {restaurante.media_avaliacoes}⭐')

    @property
    def ativo(self):
        return '㋡' if self._ativo else 'ꉕ'

    def ativar_restaurante(self):
        if not self._ativo:
            self._ativo = True

    def desativar_restaurante(self):
        if self._ativo:
            self._ativo = False

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        if nota <= 5 and nota != 0:
            self._avaliacao.append(avaliacao)
        else:
            print("Valor Invalido, nota até 5")

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_avaliacoes = len(self._avaliacao)
        media = round(soma_das_notas / qtd_avaliacoes, 1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            return self._cardapio.append(item)
        else:
            return "Valor Invalido"

    @property
    def exibir_cardapio(self):
        print(f"Cardapio do Restaurante {self._nome}\n")
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, "_descricao"):
                mensagem = f"{
                    i} - Prato: {item._nome} - Preço: {item._preco:.2f} - Descrição: {item._descricao}"
                print(mensagem)
            elif hasattr(item, "_tamanho"):
                mensagem = f"{
                    i} - Bebida: {item._nome} - Preço: {item._preco:.2f} - Tamanho: {item._tamanho}"
                print(mensagem)
            else:
                print("Item Invalido")
