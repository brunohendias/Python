#!/usr/bin/python

"""
Feito por Bruno Henrique
      09/10/2018
Caso fassa alguma alteração poste no github e mande o link
github: https://github.com/brunohendias
"""
from random import randint
from time import sleep

# intervalo entre o sorteio de um novo numero
intervalo = 4
# Total de sorteos
total_sorteios = 60
# O menor numero a ser sorteado
menor_numero = 1
# O maior numero a ser sorteado
maior_numero = 80
# O maximo de numeros na cartela
tamanho_cartela = 20 

nome = input("\n Antes de começarmos me diga qual seu nome? ")
print("~="*38)
print(f"""
    Seja bem vindo {nome} ao Bingo! Será hoje o seu dia de sorte!?
    O sorteio acontece automaticamente a cada {intervalo} segundos e termina quando
    sortear {total_sorteios} numeros diferentes. Os numeros da cartela vai de {menor_numero} a {maior_numero}
    com limite de {tamanho_cartela} numeros. No final é mostrado os resultados contendo
    os numeros sorteados e o total de acertos.
""")
print("~="*38)
msg = "\n Para trocar a cartela digite (trocar) / para começar o jogo aperte ENTER: "

def start_game():
    cartela = cria_cartela()
    print(f"\n Essa é a sua cartela Boa Sorte!!\n\n ( {str(sorted(cartela)).strip('[]')} )")
    nova_cartela = input(msg).lower()
    while nova_cartela == "trocar":
        cartela = cria_cartela()
        print(f"\n Nova cartela\n\n ( {str(sorted(cartela)).strip('[]')} )")
        nova_cartela = input(msg).lower()
    print("\n Numeros sorteados abaixo\n")
    sorteio(cartela)

def cria_cartela():
    cartela = []
    for total in range(tamanho_cartela):
        numero = randint(menor_numero, maior_numero)
        while numero in cartela:
            numero = randint(menor_numero, maior_numero)
        cartela.append(numero)
    return cartela

def sorteio(cartela):
    numeros_sorteados = []
    acerto = 0
    continua = True
    while continua:
        if len(numeros_sorteados) == total_sorteios:
            continua = False
            print(f"\n Foi sorteado os {total_sorteios} numeros\n Total de acertos: {acerto}\n Obrigado por jogar, mais sorte na proxima")
        elif acerto == 20:
            print(f"\n BINGO !!! Parabens {nome} VOCE VENCEU !!!\n")
            continua = False
        else:
            num = randint(menor_numero, maior_numero)
            while num in numeros_sorteados:
                num = randint(menor_numero, maior_numero)
            if num in cartela:
                acerto += 1
            numeros_sorteados.append(num)
            print(f" {num}", end="", flush=True)

        sleep(intervalo)# tempo para o proximo sorteio

start_game()
