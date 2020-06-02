#!/usr/bin/python3
from Classes.caixa import Caixa
from Classes.cliente import Cliente
import os

caixa = Caixa()
cliente = Cliente()

os.system('cls')
print("=~="*25)
print("""
    Programa para automatizar o controle de fila
    Github: https://github.com/brunohendias
    Data: 09/05/2020
""")
print("=~="*25)
input("Aperte ENTER para iniciar... ")
print("\nPrimeiro vamos adicionar os caixas\nAperte ENTER para avançar para o proximo passo\n")

while True:
    nom_caixa = input("Nome do caixa: ")
    if nom_caixa == '':
        break
    
    caixa.adiciona_caixa(nom_caixa)
    print(f"Caixas: {' '.join(caixa.nom_caixas)}\n")

print("\nAgora vamos começar\n")
print("=~="*15)
msg = f"""
            Menu de opções    

    [1] Adicionar caixa     [2] Remover caixa
    [3] Adicionar cliente   [4] Remover cliente
    [5] Ver a fila do caixa

    [ENTER] Finalizar o programa
"""
print(msg)
print("=~="*15)

opcao = input("\nDigite a opção: ")
while True:
    if opcao == '':
        break
    
    elif opcao == '1':
        nom_caixa = input("Nome do caixa a ser adicionado: ")
        caixa.adiciona_caixa(nom_caixa)

    elif opcao == '2':
        print(f"\nCaixas: {' '.join(caixa.nom_caixas)}")
        nom_caixa = input("Digite o nome do caixa a ser removido: ")
        print(caixa.remove_caixa(nom_caixa))
        
    elif opcao == '3':
        nome = input("Nome do cliente: ")
        caixa.caixas = cliente.entrar(nome, caixa.caixas, caixa.nom_caixas, caixa.limitePorCaixa)
        
    elif opcao == '4':
        caixa.caixas = cliente.sair(caixa.caixas, caixa.nom_caixas)

    elif opcao == '5':
        print(f"\nCaixas: {' '.join(caixa.nom_caixas)}")
        nom_caixa = input("Digite o nome do caixa para ver a fila: ")
        print(f"\n Caixa: {nom_caixa}\n Fila: {' '.join(caixa.ver_fila_caixa(nom_caixa))}")

    else:
        print("Opção invalida")

    print("=~="*15)
    print(msg)
    print("=~="*15)
    opcao = input("\nDigite a opção: ")
    
