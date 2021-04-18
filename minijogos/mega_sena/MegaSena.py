#!/usr/bin/python3
"""
Feito por Bruno Henrique
Data:   10/10/2018
Caso faça alguma alteração poste no github e mande o link
github: https://www.github.com/brunohendias
"""
from Helpers import array_string, gera_bilhete
from Variables import *

def start_game():
    infos()
    escolha()

def reseta_valores():
    global acertos
    acertos = []
    global erros
    erros = []
    global qtd_numeros
    qtd_numeros = qtd_minima_numeros 

def linha():
    print("~="*30)

def infos():
    print("")
    linha()
    print(f"""
    Bem vindo {nome} ao sorteio da Mega Sena da virada!!
    Sera hoje o seu dia de sorte?!
    Premio acumulado em {premio}.
    Regras:
        - Digite um numero entre {menor_numero} e {maior_numero}.
        - Limite de numeros por bilhete:
            - Minimo: {qtd_minima_numeros}
            - Maximo: {qtd_maxima_numeros}
        - Vence quando acertar os {vitoria} numeros
    """)
    linha()

def mostra_opcoes():
    print(" Opções ")
    
    i = 0
    for opcao in opcoes:
        i +=1
        print(f" [{i}] {opcao['texto']}")

def escolha():
    mostra_opcoes()
    opcao = -1
    total_opcoes = len(opcoes)
    while opcao > total_opcoes or opcao < 0:
        opcao = input(" Opção: ")
        try:
            opcao = int(opcao) - 1
        except:
            print(" Valor invalido. Aceitamos apenas numero")
            escolha()
    texto = opcoes[opcao]['texto']
    action = opcoes[opcao]['action']
    print(f"\n Opção escolhida: {texto}\n")
    action()

def sortear():
    global bilhete_mega
    bilhete_mega = gera_bilhete(qtd_numeros)

def gera_bilhete_jogador():
    sortear()
    total_numeros()
    global apostas
    apostas = gera_bilhete(qtd_numeros)
    resultado()

def monta_bilhete_jogador():
    sortear()
    total_numeros()
    global apostas
    apostas = input("\n Digite os numeros da sua aposta: ").replace(',', ' ').replace(';', ' ').split()

    try:
        for i in range(len(apostas)):
            apostas[i] = int(apostas[i])
    except:
        print(f"\n Apenas numeros entre {menor_numero} e {maior_numero}")
        monta_bilhete_jogador()

    if len(apostas) == qtd_numeros:
        for aposta in apostas:
            if aposta > 60 or aposta < 0:
                print(f"\n Apenas numeros entre {menor_numero} e {maior_numero}")
                monta_bilhete_jogador()
    else:
        print(f"\n O bilhete precisa ter {qtd_numeros} numeros")
        monta_bilhete_jogador()
    resultado()

def total_numeros():
    global qtd_numeros
    msg = " Deseja apostar quantos numeros: "
    try:
        limite = int(input(msg))
        while limite < qtd_minima_numeros or limite > qtd_maxima_numeros:
            print(f" Quantidade minima: {qtd_minima_numeros}, Quantidade maxima: {qtd_maxima_numeros}")
            limite = int(input(msg))
        qtd_numeros = limite
    except:
        print(f" Escolha invalida. O bilhete terá {qtd_numeros} numeros")

def valida_apostas():
    for aposta in apostas:
        if aposta in bilhete_mega:
            acertos.append(aposta)
        else:
            erros.append(aposta)

def valida_jogo():
    valida_apostas()
    total_acertos = len(acertos)
    print(" Resultado da mega sena \n")
    if total_acertos == vitoria:
        print(f" Parabens {nome}!! Você acertou todos os numeros da Mega Sena e levou o premio de {premio}")
    elif total_acertos >= 3:
        print(f" Passou perto em {nome} na proxima voce ganha")
    else:
        print(" Pratique mais, passou longe")

def resultado():
    linha()
    valida_jogo()
    print(f"""
    Numeros sorteados: 
        - {array_string(bilhete_mega)}
    Bilhete completo: 
        - {array_string(apostas)}
    Numeros acertado: 
        - {array_string(acertos)}
    Numeros errado: 
        - {array_string(erros)}
    """)
    linha()
    jogar_novamente()

def jogar_novamente():
    msg = "\n Deseja continuar: sim/nao? "
    continua = input(msg).lower()
    if continua != "nao":
        reseta_valores()
        start_game()
        continua = input(msg).lower()
    else:
    	quit()

opcoes = [
    {'texto': 'Montar bilhete', 'action': monta_bilhete_jogador},
    {'texto': 'Bilhete pronto', 'action': gera_bilhete_jogador},
    {'texto': 'Sair', 'action': quit}
]

start_game()