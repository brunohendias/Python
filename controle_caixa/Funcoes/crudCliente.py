from sys import path
path.append('..')
from random import randint
from Models.Cliente import Cliente 
from Uteis.listas import produtos
from Funcoes import crudCaixa, crudLobby

def add():
    c = Cliente()
    c.nome = input("Nome do cliente: ")
    c.idade = randint(15, 70)
    c.dinheiro = randint(100, 300)
    for i in range(randint(2, 10)):
        index = randint(0, len(produtos) - 1)
        item = produtos[index]
        while item in c.carrinho.fila:
            index = randint(0, len(produtos) - 1)
            item = produtos[index]
        c.carrinho.add(item)
    
    caixa = crudCaixa.menor_fila()
    if len(caixa.fila.fila) < caixa.limite:
        return crudCaixa.add_cliente(caixa, c)
    crudLobby.add(c)
    crudLobby.show()

def rm():
    caixas = crudCaixa.show()
    caixa = caixas[randint(0, len(caixas) - 1)]
    cliente = caixa.fila[randint(0, len(caixa.fila) - 1)]
    for item in cliente.carrinho:
        preco = item[1]
        if cliente.dinheiro > preco:
            cliente.dinheiro -= preco
            caixa.dinheiro += preco
        else:
            print("Cliente ficou sem dinheiro")
            break
        print(f"{item[0]} - R${preco}, Carteira: {round(cliente.dinheiro, 2)}")
