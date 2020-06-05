#!/usr/bin/python3
from Funcoes import crud
from Mensagens import msg
import os

os.system('cls')
print(msg.inicio)
input("Aperte ENTER para iniciar... ")
print("\nPrimeiro vamos adicionar os caixas\nAperte ENTER para avançar para o proximo passo\n")

while True:
    nom_caixa = input("Nome do caixa a ser adicionado: ").lower()
    if nom_caixa == '':
        break
    
    crud.adiciona_caixa(nom_caixa)
    crud.ver_caixas()

print(msg.menu)
opcao = input("Digite a opção: ")
while True:
    if opcao == '':
        break
    
    elif opcao == '1':
        crud.ver_caixas()
        nom_caixa = input("Nome do caixa a ser adicionado: ").lower()
        if nom_caixa == '':
            break

        crud.adiciona_caixa(nom_caixa)

    elif opcao == '2':
        crud.ver_caixas()
        nom_caixa = input("Digite o nome do caixa a ser removido: ")

        crud.remove_caixa(nom_caixa)
        
    elif opcao == '3': 
        nom_cliente = input("Nome do cliente: ")

        crud.adiciona_cliente(nom_cliente)
        
    elif opcao == '4':
        crud.remove_cliente()

    elif opcao == '5':
        crud.ver_caixas()
        nom_caixa = input("Digite o nome do caixa para ver a fila: ")
        
        crud.ver_fila_caixa(nom_caixa)

    elif opcao == '6':
        crud.ver_lobby()
        
    else:
        print("Opção invalida")

    input("\nAperte ENTER para prosseguir...")
    print(msg.menu)
    opcao = input("Digite a opção: ")