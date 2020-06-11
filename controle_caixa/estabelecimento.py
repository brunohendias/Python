#!/usr/bin/python3
from Funcoes.crudCaixa import adiciona_caixa, remove_caixa, ver_fila_caixa, ver_caixa
from Funcoes.crudCliente import adiciona_cliente, remove_cliente, ver_cliente
from Funcoes.crudLobby import ver_lobby
from Uteis import msg

print(msg.inicio)
input("Aperte ENTER para iniciar... ")
print(msg.info)

continua = True
while continua:
    continua = adiciona_caixa()

print(msg.menu)
opcao = input("Digite a opção: ")
while True:
    if opcao == '':
        break
    
    elif opcao == '1':
        adiciona_caixa()

    elif opcao == '2':
        remove_caixa()
        
    elif opcao == '3': 
        adiciona_cliente()
        
    elif opcao == '4':
        remove_cliente()

    elif opcao == '5':
        ver_fila_caixa()

    elif opcao == '6':
        ver_cliente()

    elif opcao == '7':
        ver_caixa()

    elif opcao == '8':
        ver_lobby()
        
    else:
        print("Opção invalida")

    input("\nAperte ENTER para prosseguir...")
    print(msg.menu)
    opcao = input("Digite a opção: ")