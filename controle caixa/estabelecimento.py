#!/usr/bin/python3
from caixa import Caixa
from cliente import Cliente
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
print("=~="*25)
print(f"""
            Menu de opções
            
    [0] Finalizar o programa    
    [1] Adicionar caixa
    [2] Adicionar cliente
    [3] Remover cliente
    [4] Ver a fila do caixa

    Caixas: {' '.join(caixa.nom_caixas)}
""")
print("=~="*25)

opcao = input("Digite a opção: ")
while True:
    if opcao == '':
        break
    
    elif opcao == '1':
        caixa.adiciona_caixa()
        
    elif opcao == '2':
        nome = input("Nome do cliente: ")
        caixa.caixas = cliente.entrar(nome, caixa.caixas, caixa.nom_caixas, caixa.limitePorCaixa)
        
    elif opcao == '3':
        caixa.caixas = cliente.sair(caixa.caixas, caixa.nom_caixas)

    elif opcao == '4':
        print(f"\nCaixas: {' '.join(caixa.nom_caixas)}")
        nom_caixa = input("Digite o nome do caixa: ")
        print(f"\n Caixa: {nom_caixa}\n Fila: {' '.join(caixa.ver_fila_caixa(nom_caixa))}")

    else:
        print("Opção invalida")

    opcao = input("\nDigite a opção: ")
    
