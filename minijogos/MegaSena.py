#!/usr/bin/python3

"""
Feito por Bruno Henrique
Data:   10/10/2018
Caso faça alguma alteração poste no github e mande o link
github: https://www.github.com/brunohendias
"""

from random import randint

premio = "210 Milhões"
nome = input(" Para darmos inicio ao jogo me diga qual seu nome: ")
print("~="*35)
print(f"""
    Bem vindo {nome} ao sorteio da Mega Sena da virada!!
    Sera hoje o seu dia de sorte?!
    Premio acumulado em {premio}.
    Digite um numero por vez de 1 a 60.
    Para alterar algum numero digite: trocar.
""")
print("~="*35)

def start_game():
    escolha()
    msg = "\n Deseja continuar [Sim/Nao]? "
    continua = input(msg).lower()
    if continua != "nao":
        escolha()
        continua = input(msg).lower()
    else:
    	quit()

def escolha():
    print("\n [1]Montar bilhete\n [2]Bilhete pronto\n [sair]Sair\n")
    escolha = input(" Opção: ")
    if escolha.isdigit():
        if escolha == '1':
            print(" Opção escolhida: Montar bilhete")
            montar_bilhete()
        elif escolha == '2':
            print(" Opção escolhida: Bilhete pronto")
            bilhete_pronto()
    elif escolha.lower() == 'sair':
        quit()
    else:
        start_game()

def sorteio_mega():
    bilhete_mega = []
    while len(bilhete_mega) < 6:
        numero = randint(1,60)
        while numero in bilhete_mega:
            numero = randint(1,60)
        bilhete_mega.append(numero)
    return bilhete_mega

def total_numeros(msg):
    try:
        total_aposta = int(input(msg))
        while total_aposta < 6 or total_aposta > 15:
            print(" Minimo 6, Maximo 15")
            total_aposta = int(input(msg))
    except:
        print(" Escolha invalida. Bilhete terá 6 numeros")
        total_aposta = 6
    return total_aposta

def bilhete_pronto():
    bilhete_jogador, acerto, erros = [], [], []
    bilhete_mega = sorteio_mega()
    total_aposta = total_numeros("\n Bilhete com quantos numeros? ")
    
    while len(bilhete_jogador) < total_aposta:
        numero = randint(1,60)
        while numero in bilhete_jogador:
            numero = randint(1,60)
        bilhete_jogador.append(numero)
        if numero in bilhete_mega:
            acerto.append(numero)
        else:
            erros.append(numero)

    resultado(bilhete_mega, bilhete_jogador, acerto, erros)

def montar_bilhete():
    acerto, erros = [], []
    bilhete_mega = sorteio_mega()
    total_aposta = total_numeros("\n Quantos numeros deseja apostar entre 6 e 15: ")

    bilhete_jogador = input("\n Digite os numeros da sua aposta: ").replace(',', ' ').replace(';', ' ').split()
    
    if len(bilhete_jogador) == total_aposta:
        acertos, erros = 0, 0
        list_acerto, list_erro = [], []
        numero_errado = False
        for i in range(len(bilhete_jogador)):
            aposta = int(bilhete_jogador[i])
            if aposta > 60 or aposta < 0:
                print("\n Apenas numeros entre 60 e 1")
                numero_errado = True
                break
            elif aposta == bilhete_mega[i]:
                list_acerto.append(aposta)
                acertos += 1
            else:
                list_erro.append(aposta)
                erros += 1

        if numero_errado:
            montar_bilhete()
        else:    
            resultado(bilhete_mega, bilhete_jogador, acertos, erros, list_acerto, list_erro)
    else:
        print("\n O bilhete excedeu a quantidade de numeros")
        montar_bilhete()

def resultado(mega, bilhete, acerto, erros, list_acerto, list_erro):
    if acerto == 6:
        print(f"\n Parabens {nome}!! Você acertou todos os numeros da Mega Sena e levou o premio de {premio}")
    elif acerto >= 3:
        print(f"\n Passou perto em {nome} na proxima voce ganha\n")
    else:
        print("\n Pratique mais, passou longe \n")

    bilhete_mega = ' '.join(sorted(mega))
    bilhete_jogador = ' '.join(sorted(bilhete))
    list_acerto = ' '.join(sorted(list_acerto))
    list_erro = ' '.join(sorted(list_erro))

    print(f" Resultado da mega sena: {bilhete_mega}\n bilhete completo: {bilhete_jogador}\n Numeros acertado: {acerto}\n Numeros errado: {erros}\n")
    print("~="*35)

start_game()