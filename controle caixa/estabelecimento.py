from caixa import Caixa
import os

print("=~"*32)
print("""
    Bem vindo ao controle de caixas
    Menu:
        [1] Adicionar funcionario para o caixa
        [2] Adicionar cliente
        [3] Remover cliente
""")
print("=~"*32)
comeca = input("Aperte ENTER para iniciar... ")
opcao = input("\nVamos começar, digite a opção escolhida: ")

supermercado = Caixa()
if opcao == '1':
    supermercado.adiciona_caixa()
elif opcao == '2':
    supermercado.entrar()
elif opcao == '3':
    supermercado.sair()

print(supermercado.caixas)
    
