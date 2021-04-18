#!/usr/bin/python3
"""
Feito por Bruno Henrique
      09/10/2018
Caso fassa alguma alteração poste no github e mande o link
github: https://github.com/brunohendias
"""

from time import sleep
from Variables import *
from Helpers import gera_cartela, linha, mostra_cartela, gera_numero

def mostra_infos():
    global nome
    nome = input("\n Antes de começarmos me diga qual seu nome? ")
    print("~="*34)
    print(f"""
    Seja bem vindo {nome} ao Bingo! Será hoje o seu dia de sorte!?

    Sobre o sorteio:
        - Acontece automaticamente a cada {intervalo} segundos
        - Termina quando:
            - Sortear {limite_sorteios} numeros diferentes
            - Acertar os {total_acertos_vitoria} numeros.

    Sobre a cartela do jogador:
        - Possui os numeros entre {menor_numero} e {maior_numero}
        - Limite de {tamanho_cartela} numeros.

    No final é mostrado os resultados contendo:
        - Os numeros sorteados
        - O total de acertos
    """)
    print("~="*34)

def start_game():
    mostra_infos()
    gera_cartela_jogador()
    sorteio()

def escolher():
    return input("\n\n Para começar o jogo aperte ENTER. Trocar cartela digite trocar: ").lower()

def gera_cartela_jogador():
    global cartela
    cartela = gera_cartela()
    print(f"\n Essa é a sua cartela")
    mostra_cartela(cartela)
    if escolher() == "trocar":
        gera_cartela_jogador()

def sortear():
    global acertos
    global coluna_atual
    num = gera_numero()
    while num in num_sorteados:
        num = gera_numero()

    num_sorteados.append(num)
    if num in cartela:
        acertos += 1
    
    coluna_atual += 1
    if coluna_atual == limite_colunas:
        linha()
        coluna_atual = 0
    elif int(num) < 10:
        print(f"   {num}", end="", flush=True)
    else:
        print(f"  {num}", end="", flush=True)
    
    return num

def valida_sorteio():
    finalizou = False
    if acertos == total_acertos_vitoria:
        print(f"\n\n BINGO !!! Parabens {nome} VOCE VENCEU !!!\n")
        finalizou = True
    elif len(num_sorteados) == limite_sorteios:
        print(f"""
    Foi sorteado os {limite_sorteios} numeros.
    Total de acertos: {acertos}.
    Obrigado por jogar, mais sorte na proxima.
        """)
        finalizou = True
    
    return finalizou

def sorteio():
    print("\n OK! Então vamos iniciar. Numeros sorteados abaixo")
    finalizou = False
    linha()
    while not finalizou:
        sleep(intervalo)# tempo para o proximo sorteio
        sortear()
        finalizou = valida_sorteio()

start_game()