from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('suco de melancia', 5, 'grande')
bebida_suco.aplicar_desconto()
prato_cuzcus = Prato('cuscus', 10, 'bom demais')
prato_cuzcus.aplicar_desconto()
restaurante_praca.adicionar_card(bebida_suco)
restaurante_praca.adicionar_card(prato_cuzcus)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()