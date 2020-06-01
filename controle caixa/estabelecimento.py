#!/usr/bin/python3
from caixa import Caixa
import os

os.system('cls')
print("=~="*25)
print("""
    Programa para automatizar o controle de fila
    Github: https://github.com/brunohendias
    Data: 09/05/2020
""")
print("=~="*25)
input("Aperte ENTER para iniciar... ")
print("\nPrimeiro vamos adicionar os caixas\nDigite (fim) para o proximo passo\n")

estabelecimento = Caixa()
continua = True
while continua:
    caixa = input("Nome do caixa: ")
    if caixa == 'fim':
        continua = False
        break
    caixa = estabelecimento.adiciona_caixa(caixa)
    print(f"Caixas: {' '.join(estabelecimento.nom_caixas)}\n")

print("\nAgora vamos começar\n")
print("=~="*25)
print(f"""
            Menu de opções
            
    [0] Finalizar o programa    
    [1] Adicionar caixa
    [2] Adicionar cliente
    [3] Remover cliente
    [4] Ver a fila do caixa

    Caixas: {' '.join(estabelecimento.nom_caixas)}
""")
print("=~="*25)

opcao = input("Digite a opção: ")
while opcao != '0':
    if opcao == '1':
        estabelecimento.adiciona_caixa()
        
    elif opcao == '2':
        nome = input("Nome do cliente: ")
        estabelecimento.entrar(nome)
        
    elif opcao == '3':
        estabelecimento.sair()

    elif opcao == '4':
        nom_caixa = input("Digite o nome do caixa: ")
        print(f"\n Caixa: {nom_caixa}\n Fila: {' '.join(estabelecimento.ver_fila_caixa(nom_caixa))}")

    else:
        print("Opção invalida")

    opcao = input("\nDigite a opção: ")
    
