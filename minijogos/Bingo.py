"""
Feito por Bruno Henrique
      09/10/2018 
Caso fassa alguma alteração poste no github e mande o link
github: https://github.com/brunohendias

Alterado dia 19/04/2019
Alterado dia 26/04/2019
"""
from random import *
print("~="*38)
nome = input(" Antes de começarmos qual seu nome? ")
print(f" Seja bem vindo {nome} ao Bingo! Sera hoje o seu dia de sorte?!")
print(" Aperte Enter para sortear\n digite sair para sair\n digite cartela para ver a sua cartela\n Digite sorteados para ver os numeros sorteados")
print("~="*38)

def cartelaPronta():
    global cartela
    cartela = []
    for tot in range(15):
        num = randint(0, 50)        
        while num in cartela:
            num = randint(0,50)
        cartela.append(num)
    return cartela

def criaCartela():
    cartelaPronta()
    print(f" Essa é a sua cartela Boa Sorte!! {cartela}\n")
    novaCartela = input(" Para trocar a cartela digite trocar / começar o jogo aperte ENTER: ").lower()
    while novaCartela == "trocar":
        cartelaPronta()
        print(f"\n Nova cartela: {cartela}")
        novaCartela = input("\n Para trocar a cartela digite trocar ou aperte Enter para começar: ").lower()
    print("\n Numeros sorteados abaixo\n")
    
def sorteio():
    acerto = 0
    sortiado = []
    procegue = True
    while procegue:
        numero = input(" Sortiar um numero? ").lower()
        if numero == "" or numero == "sim":
            num = randint(0, 50)
            while num in sortiado:
                num = randint(0,50)
            if num in cartela:
                acerto += 1
            sortiado.append(num)
            print(" %d"%num)
        elif numero == "sair":
            procegue = False
            print(" Obrigado por jogar volte sempre")
        elif numero == "sorteados":
            formato = str(sorted(sortiado)).strip("[]")
            print(f"\n Numeros ja sorteados: {formato}\n")
        elif numero == "cartela":
            print(f"\n Cartela: {cartela}\n")

        if acerto >= 10 and acerto < 12:
            print(" OPA CORRE CORRE QUE TA COMPLETANDO\n")
        elif acerto == 15:
            print(f" BINGO !!! Parabens {nome} VOCE VENCEU !!!\n")
            procegue = False
    
def main():
    criaCartela()
    sorteio()
main()