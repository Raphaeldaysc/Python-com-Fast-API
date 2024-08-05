from models.restaurante import Restaurante as rtrt
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

restaurante_sabor_nordestino = rtrt("Sabor Nordestino", "Nordestina")
bebida_suco = Bebida("Suco de Laranja", 13.90, "M")
prato_pao = Prato("Pão Redondo", 0.50, "Experimente o irresistível pão redondo, uma verdadeira obra-prima da panificação! Com sua crosta dourada e crocante, ele revela um interior macio e saboroso que derrete na boca. Feito com ingredientes selecionados e fermentação natural, cada mordida é uma explosão de sabor e textura.")
bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()
restaurante_sabor_nordestino.adicionar_no_cardapio(bebida_suco)
restaurante_sabor_nordestino.adicionar_no_cardapio(prato_pao)


def main():
    restaurante_sabor_nordestino.exibir_cardapio


if __name__ == '__main__':
    main()
