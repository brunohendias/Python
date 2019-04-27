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
print(" Bem vindo %s ao sorteio da Mega Sena da virada!!\n Sera hoje o seu dia de sorte?!"%nome)
print(" Premio acumulado em %s"%premio)
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
        
def resultado(mega, bilhete, existe, erros, tot_erro):
    mega = str(sorted(mega)).strip("[]")
    bilhete = str(sorted(bilhete)).strip("[]")
    existe = str(sorted(existe)).strip("[]")
    erros = str(sorted(erros)).strip("[]")
    
    if tot_erro == 0:
        print("")
        print(" Parabens %s acabou de Ganhar %s \n"%(nome, premio))
    elif tot_erro <= 3:
        print("")
        print(" Passou perto em %s na proxima voce ganha\n"%nome)
    else:
        print("")
        print(" Pratique mais, passou longe \n")
        
    print(" Resultado da mega sena: {}\n bilhete completo: {}\n Numeros acertado: {}\n Numeros errado: {}\n Total de erros: {}\n".format(mega, bilhete, existe, erros, tot_erro))
    print("~="*35)
    
def bilhetePronto():
    tot_erro = 0
    existe, erros, bilhete = [], [], []
    sorteioMega()
    
    while len(bilhete) < 6: 
        v = randint(0,60)
        while v in bilhete:
            v = randint(0,60)
        bilhete.append(v)
        if v in mega:
            existe.append(v)
        else:
            erros.append(v)
            tot_erro += 1
            
    resultado(mega, bilhete, existe, erros, tot_erro)       
    
def montarBilhete():
    cont = 0
    tot_erro = 0
    existe, erros, bilhete = [], [], []

    tot_aposta = int(input("\n Quantos numeros de 6 a 15: "))
    sorteioMega()
    
    while tot_aposta < 6 or tot_aposta > 15:
        tot_aposta = int(input(" Quantos numeros deseja apostar entre 6 e 15: "))
        print("")
    while cont < tot_aposta:
        num = int(input("\n Numero: "))
        while num < 0 or num > 60 and num != 98 or num in bilhete:
            num = int(input("\n Numero: "))
        if num == 98:
            cont -= 1
            num = int(input(" Numero a ser trocado: "))
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
        else:
            erros.append(num)
            tot_erro += 1
        cont += 1

    resultado(mega, bilhete, existe, erros, tot_erro)    

def escolha():
    print("\n Montar bilhete digite 1\n bilhete pronto digite 2 \n")
    escolha = int(input(" Opção escolhida: "))
    print("~="*35)
    if escolha == 1:
        montarBilhete()
    else:
        bilhetePronto()

escolha()
continua = input("\n Deseja continuar [Sim/Nao]? ").lower()

while continua != "nao":
   escolha()
   continua = input("\n Deseja continuar [Sim/Nao]? ").lower()
   
