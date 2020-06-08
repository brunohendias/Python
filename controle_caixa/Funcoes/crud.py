import sys
sys.path.append('..')
# Necessario para import de modulos em pasta anterior

# Classes do caixa
from Classes.Caixas.caixas import Caixas
from Classes.Caixas.caixa import Caixa
caixas = Caixas()

# Classes do cliente
from Classes.Clientes.clientes import Clientes
from Classes.Clientes.cliente import Cliente 
clientes = Clientes()

# Classes do lobby
from Classes.Lobby.lobby import Lobby
lobby = Lobby()

# Itens uteis para o projeto
from Uteis.listas import partileiras

from random import randint

def ver_lobby():
    print(f"\nLobby de espera: {' '.join(lobby.nom_clientes)}.")
    print(f"Quantidade de pessoas no lobby: {len(lobby.nom_clientes)}")

def ver_clientes():
    print(f"\nClientes: {' '.join(clientes.nom_clientes)}")

def ver_caixas():
    print(f"Caixas: {', '.join(caixas.nom_caixas)}\n")

def ver_fila_caixa():
    nom_caixa = input("Digite o nome do caixa para ver a fila: ")
    if nom_caixa in caixas.nom_caixas:
        index = caixas.nom_caixas.index(nom_caixa)
        fila_caixa = caixas.ver_fila_caixa(index)
        print(f"\nCaixa: {nom_caixa}\nFila: {' '.join(fila_caixa)}.")
    else:
        print(f"{nom_caixa} não está no caixa.")

def ver_cliente():
    print(f"Clientes: {', '.join(clientes.nom_clientes)}\n")
    nome_cliente = input("Nome do cliente: ")

    if nome_cliente in clientes.nom_clientes:
        index = clientes.nom_clientes.index(nome_cliente)
        cliente_busca = clientes.ver_cliente(index)
        print(f"\n{cliente_busca}")
    else:
        print("Cliente não encontrado.")

def define_cliente(index, nome):
    carrinho = []
    qtd_items = randint(2, 10)
    for i in range(qtd_items):
        item = randint(0, len(partileiras) - 1)
        while partileiras[item] in carrinho:
            item = randint(0, len(partileiras) - 1)
            partileiras[item]

        carrinho.append(partileiras[item] + ',')
    
    novo_cliente = Cliente()
    novo_cliente.nome = input("Nome do cliente: ")
    novo_cliente.idade = randint(15, 70)
    novo_cliente.dinheiro = randint(100, 300)
    novo_cliente.caixa = nome
    novo_cliente.carrinho = carrinho
    clientes.adiciona_cliente(novo_cliente)

    return novo_cliente

def adiciona_caixa():

    nom_caixa = input("Nome do caixa a ser adicionado: ").lower()
    if nom_caixa == '':
        return False

    elif nom_caixa in caixas.nom_caixas:
        print(f"O {nom_caixa} já está no caixa.")
    
    else:
        try:
            dinheiro = float(input("Dinheiro inicial do caixa: ").replace(',', '.'))
        except:
            print("Valor invalido")
            dinheiro = float(input("Dinheiro inicial do caixa: ").replace(',', '.'))
        limiteFila = input("Limite de clientes na fila: ")
        
        caixa = Caixa()
        caixa.nome = nom_caixa
        caixa.dinheiro_inicial = dinheiro
        caixa.limiteFila = caixa.limiteFila if limiteFila == '' else int(limiteFila)
        
        caixas.adiciona_caixa(caixa)
    
    return True

def adiciona_cliente():
    index = caixas.acha_menor_fila()
    caixa_atual = caixas.caixas[index]
    novo_cliente = define_cliente(index, caixa_atual.nome)

    fila_caixa = caixa_atual.fila
    limite = caixa_atual.limiteFila
    if len(fila_caixa) < limite and len(lobby.lobby) == 0:
        caixas.adiciona_cliente(index, novo_cliente)
        # se tiver caixa liberado e o lobby vazio adiciona na fila do caixa

    elif len(fila_caixa) == limite:
        lobby.entrar_lobby(novo_cliente)
        print(f'\n({novo_cliente.nome}) entrou no lobby.')
        ver_lobby()
        # se a fila do caixa chegar no limite adiciona no lobby

    elif len(lobby.lobby) > 0:
        lobby.entrar_lobby(novo_cliente)
        print(f'\n{novo_cliente.nome} foi para o lobby de espera.')
        if len(caixa_atual) < limite:
            foiParaFila = lobby.liberar_lobby()
            caixas.adiciona_cliente(index, foiParaFila)
            print(f'\n{foiParaFila} saiu do lobby e entrou na fila do caixa: {menor_fila}.')
            ver_lobby()
        # se tiver alguem no lobby e tiver algum caixa com espaço, coloca no caixa e adiciona o atual no lobby

def remove_caixa():
    nom_caixa = input("Digite o nome do caixa a ser removido: ")
    if nom_caixa in caixas.nom_caixas:
        index = caixas.nom_caixas.index(nom_caixa)
        if len(caixas.caixas[index].fila) == 0:
            caixas.remove_caixa(index)
            print(f"O caixa {nom_caixa} foi removido com sucesso.")
        else:
            print("O caixa não pode ser removido porque contem cliente")
    else:
        print(f"{nom_caixa} não está no caixa.")

def remove_cliente():
    nom_caixas = caixas.nom_caixas
    _caixas = caixas.caixas
    index = randint(0, len(nom_caixas) - 1)

    print(_caixas)

    if len(_caixas[index].fila) == 0:
        for i in _caixas:
            if len(_caixas[i].fila) > 0:
                index = i
                break
        # Se a fila do caixa aleatorio estiver vazia ele verifica os outros

    _caixa = _caixas[index]
    if len(_caixa.fila) == 0:
        print('\nTodos os caixas estão vasios')

    elif len(_caixa.fila) > 0:
        cliente_removido = _caixa.fila[0]
        caixas.remove_cliente(index, 0)
        clientes.remove_cliente(index)
        nome = cliente_removido.nome
        print(f"O cliente {nome} saio do caixa: {_caixa.nome}.")

    if len(lobby.lobby) > 0:
        foiParaFila = lobby.liberar_lobby()
        caixas.adiciona_cliente(index, foiParaFila)
        nome = foiParaFila.nome
        print(f'\n{nome} saiu do lobby e entrou na fila do caixa: {_caixa.nome}.')