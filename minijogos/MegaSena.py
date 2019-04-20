"""
Feito por Bruno Henrique
      10/10/2018 
Caso faça alguma alteração poste no github e mande o link
github: https://www.github.com/brunohendias

Alterado dia: 19/04/2019
"""

from random import *

premio = "210 Milhões"
print("~="*35)
nome = input(" Para darmos inicio ao jogo me diga qual seu nome: ")
print(" Bem vindo %s ao sorteio da Mega Sena da virada!! Sera hoje o seu dia de sorte?!"%nome)
print(" Premio acumulado em %s"%premio)
print(" Digite um numero por vez de 0 a 60")
print(" Para alterar algum numero digite 98 // Para sair digite 99")
print("~="*35)

mega = []
def sorteioMega():
    while len(mega) < 6:
        numero = randint(0,60)
        while numero in mega:
            numero = randint(0,60)
        mega.append(numero)
        
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
        
    print("\n Resultado da mega sena: {}\n bilhete completo: {}\n Numeros acertado: {}\n Numeros errado: {}\n Total de erros: {}\n".format(mega, bilhete, existe, erros, tot_erro))
    print("~="*35)
    
def bilhetePronto():
    tot_erro = 0
    existe, erros, bilhete = [], [], []
    
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
            
    sorteioMega()
    resultado(mega, bilhete, existe, erros, tot_erro)       
    
def montarBilhete():
    cont = 0
    tot_erro = 0
    existe, erros, aposta, bilhete = [], [], [],[]

    tot_aposta = int(input(" Quantos numeros de 6 a 15: "))
    print("")
    
    def trocaNumero():
        posicao = int(input(" Qual a posição do numero: "))
        numero = int(input(" Numero novo: "))
        print("")
        aposta[posicao] = numero
        
    sorteioMega()
    
    while tot_aposta < 6 or tot_aposta > 15:
        tot_aposta = int(input(" Quantos numeros deseja apostar entre 6 e 15: "))
        print("")
    for cont in range(tot_aposta):
        num = int(input(" Numero: "))
        while num < 0 or num > 60:
            num = int(input(" Numero: "))
        bilhete.append(num)
        if num in mega:
            existe.append(num)
            aposta.append(num)
        else:
            erros.append(num)
            tot_erro += 1
            aposta.append(num)
        while num == 98:
            trocaNumero()
            num = int(input(" Numero: "))
            cont += 1
        if num == 99:
            break
    resultado(mega, bilhete, existe, erros, tot_erro)

def escolha():
    print("")
    print(" Montar bilhete digite 1\n bilhete pronto digite 2 \n")
    escolha = int(input(" Opção escolhida: "))
    print("")
    print("~="*35)
    if escolha == 1:
        montarBilhete()
    else:
        bilhetePronto()

escolha()
print("")
continua = input(" Deseja continuar [Sim/Nao]? ").lower()

while continua == "sim":
   escolha()
   print("")
   continua = input(" Deseja continuar [Sim/Nao]? ").lower()
   
