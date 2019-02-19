"""
Feito por Bruno Henrique
      10/10/2018 
Caso fassa alguma alteração poste no github e mande o link 
"""
from random import *

premio = "210 Milhões"
nome = input(" Para darmos inicio ao jogo me diga qual seu nome: ")
print("~="*35)
print(" Bem vindo %s ao sorteio da Mega Sena da virada!! Sera hoje o seu dia de sorte?!"%nome)
print(" Premio acumulado em %s"%premio)
print(" Digite um numero por vez de 0 a 60")
print(" Para alterar algum numero digite 98 // Para sair digite 99")
print("~="*35)
   
def bilhetePronto():
    cont = 0
    existe, erros, aposta, bilhete, mega = [], [], [], [], []
    def sorteioMega():
        while len(mega) < 6:
            numero = randint(0,60)
            while numero in mega:
                numero = randint(0,60)
            mega.append(numero)               
       
    while len(bilhete) < 6: 
        v = randint(0,60)
        while v in bilhete:
            v = randint(0,60)
        bilhete.append(v)
        if v in mega:
            existe.append(v)
            aposta.append(v)
        else:
            erros.append(v)
            aposta.append(v)
            
    sorteioMega()
    tot_erro = len(erros)
    
    mega = str(sorted(mega)).strip("[]") 
    bilhete = str(sorted(bilhete)).strip("[]")
    existe = str(sorted(existe)).strip("[]")
    erros = str(sorted(erros)).strip("[]")
    print("\n Resultado da mega sena: {}".format(mega))
    print(" bilhete completo:       {}".format(bilhete))
    print(" Numeros acertado:       {}".format(existe))
    print(" Numeros errado:         {}".format(erros))
    print(" Total de erros:         {}".format(tot_erro))
                
    if tot_erro == 0:
        print("")
        print(" Parabens %s acabou de Ganhar %s \n"%(nome, premio))
    elif tot_erro <= 3:
        print("")
        print(" Passou perto em %s na proxima voce ganha\n"%nome)
    elif tot_erro >= 4:
        print("")
        print(" Pratique mais, passou longe \n")
        
    
def montarBilhete():
    cont = 0
    mega, existe, erros, aposta, bilhete = [], [], [], [],[]

    tot_aposta = int(input(" Quantos numeros de 6 a 15: "))
    print("")
    
    def sorteioMega():        
        while len(mega) < 6:
           numero = randint(0,60)
           while numero in mega:
               numero = randint(0,60)
           mega.append(numero)
    def trocaNumero():
        posicao = int(input(" Qual a posição do numero: "))
        numero = int(input(" Numero novo: "))
        print("")
        aposta[posicao] = numero
        
    sorteioMega()
    tot_erro = len(erros)
    
    while tot_aposta < 6 or tot_aposta > 15:
        tot_aposta = int(input(" Quantos numeros deseja apostar entre 6 e 15: "))
        print("")
    for cont in range(tot_aposta):
        num = int(input(" Numero: "))
        while num < 0:
            num = int(input(" Numero: "))
        bilhete.append(num)
        if num in mega:
            existe.append(num)
            aposta.append(num)
        else:
            erros.append(num)
            aposta.append(num)
        while num == 98:
            trocaNumero()
            num = int(input(" Numero: "))
            cont += 1
        if num == 99:
            break
        
    mega = str(sorted(mega)).strip("[]") 
    bilhete = str(bilhete).strip("[]")
    existe = str(sorted(existe)).strip("[]")
    erros = str(sorted(erros)).strip("[]")
    print("\n Resultado da mega sena: {}".format(mega))
    print(" bilhete completo:       {}".format(bilhete))
    print(" Numeros acertado:       {}".format(existe))
    print(" Numeros errado:         {}".format(erros))
    print(" Total de erros:         {}".format(tot_erro))
                
    if tot_erro == 0:
        print("")
        print(" Parabens %s acabou de Ganhar %s \n"%(nome, premio))
    elif tot_erro <= 3:
        print("")
        print(" Passou perto em %s na proxima voce ganha\n"%nome)
    elif tot_erro >= 4:
        print("")
        print(" Pratique mais, passou longe \n")

escolha = int(input(" Bilhete pronto 1, montar bilhete 2: "))
if escolha == 1:
    bilhetePronto()
else:
    montarBilhete()
print("")
continua = input(" Deseja continuar [Sim/Nao]? ").lower()
print("")
while continua == "sim":
    escol = int(input(" Bilhete pronto 1 Escolher numeros 2: "))
    if escol == 1:
        bilhetePronto()
        continua = input(" Deseja continuar [Sim/Nao]? ").lower()
    else:
        montarBilhete()
        continua = input(" Deseja continuar [Sim/Nao]? ").lower()
