#!/usr/bin/python

"""
Feito por Bruno Henrique
      09/10/2018
Caso fassa alguma alteração poste no github e mande o link
github: https://github.com/brunohendias

Alterado dia 19/04/2019
Alterado dia 26/04/2019
"""
from random import randint
import time

nome = input(" Antes de começarmos qual seu nome? ")
print("~="*38)
print(f" Seja bem vindo {nome} ao Bingo! Sera hoje o seu dia de sorte?!")
print(" Aperte Enter para sortear\n digite sair para sair\n digite cartela para ver a sua cartela\n Digite sorteados para ver os numeros sorteados")
print("~="*38)

def cria_cartela():
    cartela = []
    for total in range(15):
        numero = randint(0, 100)
        while numero in cartela:
            numero = randint(0,100)
        cartela.append(numero)
    return cartela

def start_game():
    intervalo, total_sorteios, acerto = 2, 60, 0
    cartela = cria_cartela()
    print(f" Essa é a sua cartela Boa Sorte!!\n {str(sorted(cartela)).strip('[]')}\n")
    nova_cartela = input(" Para trocar a cartela digite trocar / começar o jogo aperte ENTER: ").lower()
    while nova_cartela == "trocar":
        cartela = cria_cartela()
        print(f"\n Nova cartela:\n {str(sorted(cartela)).strip('[]')}")
        nova_cartela = input("\n Para trocar a cartela digite trocar ou aperte Enter para começar: ").lower()
    print("\n Numeros sorteados abaixo\n")
    sorteio(cartela, intervalo, acerto, total_sorteios)

def sorteio(cartela, intervalo, acerto, total_sorteios):
    numeros_sorteados = []
    continua = True
    while continua:
        if len(numeros_sorteados) == total_sorteios:
            continua = False
            print(f"\n Foi sorteado os {total_sorteados} numeros\n Numeros sortiados:\n{str(sorted(numeros_sortiados)).strip('[]')}\n Total de acertos: {acerto}\n Obrigado por jogar, mais sorte na proxima")
        else:
            num = randint(0, 100)
            while num in numeros_sorteados:
                num = randint(0,100)
            if num in cartela:
                acerto += 1
            numeros_sorteados.append(num)
            #print("", num, end="") print os numeros na mesma linha
            print(f" {num}")
        time.sleep(intervalo)

        if acerto >= 10 and acerto < 12 and continua == True:
            print(" OPA CORRE CORRE QUE TA COMPLETANDO\n")
        elif acerto == 15:
            print(f" BINGO !!! Parabens {nome} VOCE VENCEU !!!\n")
            continua = False


def main():
    start_game()
main()
