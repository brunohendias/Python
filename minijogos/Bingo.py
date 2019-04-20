"""
Feito por Bruno Henrique
      09/10/2018 
Caso fassa alguma alteração poste no github e mande o link
github: https://github.com/brunohendias

Alterado dia 19/04/2019
"""
from random import *
print("~="*38)
nome = input(" Antes de começarmos qual seu nome? ")
print(" Seja bem vindo %s ao Bingo! Sera hoje o seu dia de sorte?!"%nome)
print(" Aperte Enter para sortear\n Digite sair para sair\n digite cartela para ver a sua cartela\n Digite sorteados para ver os numeros sorteados")
print("~="*38)

def cartelaPronta():
    global cartela
    cartela = []
    for tot in range(15):
        num = randint(0, 50)        
        while num in cartela:
            num = randint(0,50)
        cartela.append(num)
    
def criaCartela():
    cartelaPronta()
    print(" Essa é a sua cartela Boa Sorte!! {}\n".format(cartela))
    novaCartela = int(input(" Para trocar a cartelas digite 1 / continuar digite 2: "))
    while novaCartela == 1:
        print("")
        cartelaPronta()
        print(" Nova cartela: {}".format(cartela))
        print("")
        novaCartela = int(input(" Para trocar a cartela digite 1: "))
    print(" Numeros sorteados abaixo\n")
def sorteio():
    acerto = 0
    sortiado = []
    num = randint(0, 50)
    sortiado.append(num)
    print(" %d"%num)
    while True:
        numero = input(" Sortiar mais um numero? ").lower()
        if numero == "sair":
            print(" Obrigado por jogar voute sempre")
            break
        elif numero == "" or numero == "sim":
            num = randint(0, 50)
            while num in sortiado:
                num = randint(0,50)
            if num in cartela:
                acerto += 1
            sortiado.append(num)
            print(" %d"%num)
        elif numero == "sorteados":
            formato = str(sorted(sortiado)).strip("[]")
            print("\n Numeros ja sorteados: {}".format(formato))
            print("")
        elif numero == "cartela":
            print("\n Cartela: {}".format(cartela))
            print("")
        else:
            print(" %d"%num)
            print("")
        
        if acerto == 10 and acerto < 11:
            print(" OPA CORRE CORRE QUE TA COMPLETANDO\n")
        if acerto == 15:
            print(" BINGO !!! Parabens %s VOCE VENCEU !!!\n"%nome)
            break
    
def main():
    criaCartela()
    sorteio()
main()
