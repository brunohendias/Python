#!/usr/bin/python3
from Funcoes import crud
from Uteis import msg
from os import system
clear = system('cls')

print(msg.inicio)
input("Aperte ENTER para iniciar... ")
print(msg.info)

continua = True
while continua:
    continua = crud.adiciona_caixa()
    crud.ver_caixas()

print(msg.menu)
opcao = input("Digite a opção: ")
while True:
    if opcao == '':
        break
    
    elif opcao == '1':
        crud.ver_caixas()
        crud.adiciona_caixa()

    elif opcao == '2':
        crud.ver_caixas()
        crud.remove_caixa()
        
    elif opcao == '3': 
        crud.adiciona_cliente()
        
    elif opcao == '4':
        crud.remove_cliente()

    elif opcao == '5':
        crud.ver_caixas()
        crud.ver_fila_caixa()

    elif opcao == '6':
        crud.ver_cliente()

    elif opcao == '7':
        crud.ver_lobby()
        
    else:
        print("Opção invalida")

    input("\nAperte ENTER para prosseguir...")
    print(msg.menu)
    opcao = input("Digite a opção: ")