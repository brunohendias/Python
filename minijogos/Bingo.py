"""
Feito por Bruno Henrique
      09/10/2018 
Caso fassa alguma alteração poste no github e mande o link 
"""
from random import *
nome = input(" Antes de começarmos qual seu nome? ")
print("~="*38)
print(" Seja bem vindo %s ao Bingo! Sera hoje o seu dia de sorte?!"%nome)
print(" Aperte Enter para sortear\n Digite sair para sair\n digite cartela para ver a sua cartela\n Digite sorteados para ver os numeros sorteados")
print("~="*38)
def trocaCartela():
    global formato
    global cartela
    formato, cartela = [], []    
    for tot in range(15):
        num = randint(0, 50)        
        while num in cartela:
            num = randint(0,50)
        cartela.append(num)
    formato = str(sorted(cartela)).strip("[]")   
    print(" Nova cartela Boa Sorte!! {}\n".format(formato))
def cartela():
    global cartela
    global formato
    cartela = []
    tot = len(cartela)
    for tot in range(15):
        num = randint(0, 50)        
        while num in cartela:           
            num = randint(0,50)
        cartela.append(num)
    formato = str(sorted(cartela)).strip("[]")
    print(" Essa é a sua cartela Boa Sorte!! {}\n".format(formato))
    nova = int(input(" Para trocar a cartelas digite 1 / continuar digite 2: "))
    while nova == 1:
        trocaCartela()
        nova = int(input(" Para trocar a cartela digite 1: "))
    print(" Numeros sorteados abaixo\n")
def sorteio():
    acerto = 0 
    global nume
    sortiado = []
    while True:        
        nume = randint(0, 50)
        while nume in sortiado:
            nume = randint(0,50)
        sortiado.append(nume)
        forma = str(sortiado).strip("[]")
        numero = input(" Sortiar mais um numero? ")
        print("")
        if numero == "sair":
            print(" Ate a proxima voce acertou %d numeros"%acerto)
            break
        elif numero == "sorteados":
            print(" Numeros ja sorteados: {}".format(forma))
            print("")
        elif numero == "cartela":
            print(" Cartela: {}".format(formato))
            print("")
        else:
            print(" %d"%nume)
            print("")
        if nume in cartela:
            acerto += 1
        elif acerto == 10:
            print(" OPA CORRE CORRE QUE TA COMPLETANDO\n")
        elif acerto == 15:
            print(" BINGO !!! Parabens %s VOCE VENCEU !!!\n"%nome)
            break        
    
def main():
    cartela()
    sorteio()
main()