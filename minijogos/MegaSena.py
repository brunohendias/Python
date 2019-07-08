"""
Feito por Bruno Henrique
      10/10/2018 
Caso faça alguma alteração poste no github e mande o link
github: https://www.github.com/brunohendias

Alterado dia: 19/04/2019
Alterado dia: 26/04/2019
"""

from random import *

premio = "210 Milhões"
print("~="*35)
nome = input(" Para darmos inicio ao jogo me diga qual seu nome: ")
print(f" Bem vindo {nome} ao sorteio da Mega Sena da virada!!\n Sera hoje o seu dia de sorte?!")
print(f" Premio acumulado em {premio}")
print(" Digite um numero por vez de 0 a 60")
print(" Para alterar algum numero digite: 98")
print("~="*35)

mega = []
def sorteioMega():
    while len(mega) < 6:
        numero = randint(0,60)
        while numero in mega:
            numero = randint(0,60)
        mega.append(numero)
    return mega
        
def resultado(mega, bilhete, existe, erros, tot_erro, acerto):
    mega = str(sorted(mega)).strip("[]")
    bilhete = str(sorted(bilhete)).strip("[]")
    existe = str(sorted(existe)).strip("[]")
    erros = str(sorted(erros)).strip("[]")
    
    if acerto == 6:
        print("")
        print(f" Parabens {nome} acabou de Ganhar {premio} \n")
    elif acerto >= 3:
        print("")
        print(f" Passou perto em {nome} na proxima voce ganha\n")
    else:
        print("")
        print(" Pratique mais, passou longe \n")
        
    print(f" Resultado da mega sena: {mega}\n bilhete completo: {bilhete}\n Numeros acertado: {existe}\n Numeros errado: {erros}\n Total de erros: {tot_erro}\n")
    print("~="*35)
    
def bilhetePronto():
    tot_erro, acerto = 0, 0
    existe, erros, bilhete = [], [], []
    sorteioMega()
    
    while len(bilhete) < 6: 
        v = randint(0,60)
        while v in bilhete:
            v = randint(0,60)
        bilhete.append(v)
        if v in mega:
            existe.append(v)
            acerto += 1
        else:
            erros.append(v)
            tot_erro += 1
            
    resultado(mega, bilhete, existe, erros, tot_erro, acerto)       
    
def montarBilhete():
    tot_erro, cont, acerto = 0, 0, 0
    existe, erros, bilhete = [], [], []

    tot_aposta = int(input("\n Quantos numeros de 6 a 15: "))
    sorteioMega()
    
    while tot_aposta < 6 or tot_aposta > 15 or tot_aposta:
        tot_aposta = int(input(" Quantos numeros deseja apostar entre 6 e 15: "))
        print("")
    while cont < tot_aposta:
        num = int(input("\n Numero: "))
        while num < 0 or num > 60 and num != 98 or num in bilhete:
            num = int(input("\n Numero: "))
        if num == 98:
            cont -= 1
            num = int(input("\n Numero a ser trocado: "))
            bilhete.remove(num)
            if num in erros:
                tot_erro -= 1
                erros.remove(num)
            elif num in existe:
                existe.remove(num)
            num = int(input(" Novo numero: "))
            while num < 0 or num > 60 or num in bilhete:
                num = int(input(" Novo numero: "))
        bilhete.append(num)
        if num in mega:
            existe.append(num)
            acerto += 1
        else:
            erros.append(num)
            tot_erro += 1
        cont += 1

    resultado(mega, bilhete, existe, erros, tot_erro, acerto)    

def escolha():
    print("\n Montar bilhete digite 1\n bilhete pronto digite 2 \n")
    escolha = input(" Opção escolhida: ")
    print("~="*35)
    if escolha == '1':
        montarBilhete()
    else:
        bilhetePronto()

escolha()
continua = input("\n Deseja continuar [Sim/Nao]? ").lower()

while continua != "nao":
   escolha()
   continua = input("\n Deseja continuar [Sim/Nao]? ").lower()
   
