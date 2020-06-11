import sys
sys.path.append('..') # Necessario para import de modulos em pasta anterior
from random import randint

# Classes do cliente
from Classes.Clientes.clientes import Clientes
from Classes.Clientes.cliente import Cliente 
clientes = Clientes()

# Itens uteis para o projeto
from Uteis.listas import partileiras, preco_decimal

# Funcoes Dependencia
from Funcoes.crudLobby import ver_lobby, quantidade_lobby, liberar_lobby, entrar_lobby
from Funcoes.crudCaixa import acha_menor_fila, caixa_aleatorio, adiciona_cliente_caixa, remove_cliente_caixa

def ver_clientes():
    print(f"\nClientes: {' '.join(clientes.nom_clientes)}")

def ver_cliente():
    ver_clientes()
    nome_cliente = input("Nome do cliente: ")

    try:
        index = clientes.nom_clientes.index(nome_cliente)
        cliente_busca = clientes.ver_cliente(index)
        print(f"\n{cliente_busca}")
    except:
        print("Cliente não encontrado.")

def define_cliente(nome_cliente, nome_caixa):
    carrinho = []
    qtd_items = randint(2, 10)
    for i in range(qtd_items):
        item = randint(0, len(partileiras) - 1)
        while partileiras[item] in carrinho:
            item = randint(0, len(partileiras) - 1)
        
        carrinho.append(partileiras[item])
    
    novo_cliente = Cliente()
    novo_cliente.nome = nome_cliente
    novo_cliente.idade = randint(15, 70)
    novo_cliente.dinheiro = randint(100, 300)
    novo_cliente.caixa = nome_caixa
    novo_cliente.carrinho = carrinho
    clientes.adiciona_cliente(novo_cliente)

    return novo_cliente

def finaliza_cliente(cliente_removido, _caixa):
    for item in cliente_removido.carrinho:
        index_item = partileiras.index(item)
        preco = preco_decimal[index_item]
        if cliente_removido.dinheiro > 0 and cliente_removido.dinheiro > preco:
            cliente_removido.dinheiro -= preco
            _caixa.dinheiro_final += preco
        else:
            print("Cliente ficou sem dinheiro")
            break
        print(f"Item: {item}, Preço: {preco}, Carteira cliente: {round(cliente_removido.dinheiro, 2)}")

def adiciona_cliente():
    menor_fila = acha_menor_fila()
    index = menor_fila['index']
    caixa_atual = menor_fila['caixa']
    fila_caixa = caixa_atual.fila
    limite = caixa_atual.limiteFila

    nome_cliente = input("Nome do cliente: ")
    novo_cliente = define_cliente(nome_cliente, caixa_atual.nome)

    qt_lobby = quantidade_lobby()# Retorna int
    if len(fila_caixa) < limite and qt_lobby == 0:
        adiciona_cliente_caixa(index, novo_cliente)
        # se tiver caixa liberado e o lobby vazio adiciona na fila do caixa

    elif len(fila_caixa) == limite:
        entrar_lobby(novo_cliente)
        ver_lobby()
        # se a fila do caixa chegar no limite adiciona no lobby

    elif qt_lobby > 0:
        entrar_lobby(novo_cliente)
        if len(fila_caixa) < limite:
            foiParaFila = liberar_lobby()
            foiParaFila.caixa = caixa_atual.nome
            adiciona_cliente_caixa(index, foiParaFila)
            print(f'\n{foiParaFila.nome} saiu do lobby e entrou na fila do caixa: {caixa_atual.nome}.')
            ver_lobby()
            # se tiver alguem no lobby e tiver algum caixa com espaço, coloca no caixa e adiciona o atual no lobby
        else:
            print("\ntodos os caixas estão cheios")

def remove_cliente():
    tot_clientes = len(clientes.nom_clientes)
    if tot_clientes == 0:
        print("Todos os caixas estão vasios")
        return False

    aleatorio = caixa_aleatorio()
    index = aleatorio['index']
    _caixa = aleatorio['caixa']

    if len(_caixa.fila) > 0:
        cliente_removido = _caixa.fila[0]
        finaliza_cliente(cliente_removido, _caixa)
        remove_cliente_caixa(index, 0)
        clientes.remove_cliente(index)
        nome = cliente_removido.nome
        print(f"O cliente {nome} saio do caixa: {_caixa.nome}.")

    qt_lobby = quantidade_lobby()# Retorna int
    if qt_lobby > 0:
        foiParaFila = liberar_lobby()
        adiciona_cliente_caixa(index, foiParaFila)
        nome = foiParaFila.nome
        print(f'\n{nome} saiu do lobby e entrou na fila do caixa: {_caixa.nome}.')