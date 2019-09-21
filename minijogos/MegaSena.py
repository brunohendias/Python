#!/usr/bin/python

"""
Feito por Bruno Henrique
      10/10/2018
Caso faça alguma alteração poste no github e mande o link
github: https://www.github.com/brunohendias

Alterado dia: 19/04/2019
Alterado dia: 26/04/2019
"""

from random import randint

premio = "210 Milhões"
nome = input(" Para darmos inicio ao jogo me diga qual seu nome: ")
print("~="*35)
print(f" Bem vindo {nome} ao sorteio da Mega Sena da virada!!\n Sera hoje o seu dia de sorte?!")
print(f" Premio acumulado em {premio}")
print(" Digite um numero por vez de 0 a 60")
print(" Para alterar algum numero digite: 98")
print("~="*35)


def sorteio_mega():
    bilhete_mega = []
    while len(bilhete_mega) < 6:
        numero = randint(0,60)
        while numero in bilhete_mega:
            numero = randint(0,60)
        bilhete_mega.append(numero)
    return bilhete_mega

def resultado(mega, bilhete, existe, erros):
    bilhete_mega = str(sorted(mega)).strip("[]")
    bilhete_jogador = str(sorted(bilhete)).strip("[]")
    existe = str(sorted(existe)).strip("[]")
    erros = str(sorted(erros)).strip("[]")

    if len(existe) == 6:
        print(f"\n Parabens {nome} acabou de Ganhar {premio} \n")
    elif len(existe) >= 3:
        print(f"\n Passou perto em {nome} na proxima voce ganha\n")
    else:
        print("\n Pratique mais, passou longe \n")

    print(f" Resultado da mega sena: {bilhete_mega}\n bilhete completo: {bilhete_jogador}\n Numeros acertado: {existe}\n Numeros errado: {erros}\n")
    print("~="*35)

def bilhete_pronto():
    bilhete_jogador, existe, erros = [], [], []
    bilhete_mega = sorteio_mega()

    while len(bilhete_jogador) < 6:
        numero = randint(0,60)
        while numero in bilhete_jogador:
            numero = randint(0,60)
        bilhete_jogador.append(numero)
        if numero in bilhete_mega:
            existe.append(numero)
        else:
            erros.append(numero)
    resultado(bilhete_mega, bilhete_jogador, existe, erros)

def montar_bilhete():

    bilhete_jogador, existe, erros = [], [], []
    bilhete_mega = sorteio_mega()

    total_aposta = int(input("\n Quantos numeros deseja apostar entre 6 e 15: "))

    while total_aposta < 6 or total_aposta > 15:
        total_aposta = int(input(" Quantos numeros deseja apostar entre 6 e 15: "))
        print("")
    while len(bilhete_jogador) < total_aposta:
        numero = int(input("\n Numero: "))
        if(numero < 0):
            print(" Apenas numeros maiores que 0")
        elif(numero in bilhete_jogador):
            print(f" O numero {numero} ja existe escolha outro")
        elif numero == 98:
            numero = int(input("\n Numero a ser trocado: "))
            while numero not in bilhete_jogador:
                print(f" Numero {numero} nao foi escolhido")
                numero = int(input("\n Numero a ser trocado: "))
            bilhete_jogador.remove(numero)
            if numero in erros:
                erros.remove(numero)
            elif numero in existe:
                existe.remove(numero)
            numero = int(input(" Novo numero: "))
            while numero < 0 or numero > 60 or numero in bilhete_jogador:
                numero = int(input(" Novo numero: "))
            bilhete_jogador.append(numero)
            if numero in bilhete_mega:
                existe.append(numero)
            else:
                erros.append(numero)
        elif(numero > 60):
            print(" Apenas numeros menores que 60")
        else:
            bilhete_jogador.append(numero)
            if numero in bilhete_mega:
                existe.append(numero)
            else:
                erros.append(numero)

    resultado(bilhete_mega, bilhete_jogador, existe, erros)

def escolha():
    print("\n [1]Montar bilhete digite \n [2]bilhete pronto digite \n")
    escolha = input(" Opção escolhida: ")
    print("~="*35)
    if escolha == '1':
        montar_bilhete()
    else:
        bilhete_pronto()

escolha()
continua = input("\n Deseja continuar [Sim/Nao]? ").lower()

while continua != "nao":
   escolha()
   continua = input("\n Deseja continuar [Sim/Nao]? ").lower()
