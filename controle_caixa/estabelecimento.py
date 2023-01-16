from Funcoes import crudCaixa, crudCliente, crudLobby
from Uteis import msg

print(msg.inicio)
input("Aperte ENTER para iniciar... ")
print(msg.info)

continua = True
while continua:
    continua = crudCaixa.add()

print(msg.menu)
opcao = input("Digite a opção: ")
while True:
    if opcao == '':
        break
    elif opcao == '1':
        crudCaixa.add()
    elif opcao == '2':
        crudCaixa.ver_caixa()
    elif opcao == '3': 
        crudCliente.add()
    elif opcao == '4': 
        crudLobby.show()
    elif opcao == '5':
        crudCaixa.rm()
    elif opcao == '6':
        crudCliente.rm()
    else:
        print("Opção invalida")

    input("\nAperte ENTER para prosseguir...")
    print(msg.menu)
    opcao = input("Digite a opção: ")