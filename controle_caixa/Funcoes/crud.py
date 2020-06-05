import random
import sys
sys.path.append('..') 
# Necessario para import de modulos em pasta anterior

from Classes.caixa import Caixa
from Classes.cliente import Cliente
from Classes.lobby import Lobby

caixa = Caixa()
cliente = Cliente()
lobby = Lobby()

def adiciona_caixa(nom_caixa):
    if nom_caixa in caixa.caixas:
        print(f"O {nom_caixa} já está no caixa.")
    else:
        caixa.adiciona_caixa(nom_caixa)

def remove_caixa(nom_caixa):
    if nom_caixa in caixa.caixas:
        if len(caixa.caixas[nom_caixa]) == 0:
            caixa.remove_caixa(nom_caixa)
            print(f"O caixa {nom_caixa} foi removido com sucesso.")
        else:
            print("O caixa não pode ser removido porque contem cliente")
    else:
        print(f"{nom_caixa} não está no caixa.")

def adiciona_cliente(nom_cliente):
    limite = caixa.limitePorCaixa
    menor_fila = caixa.acha_menor_fila()
    caixa_atual = caixa.caixas[menor_fila]

    if len(caixa_atual) < limite and len(lobby.lobby) == 0:
        caixa.adiciona_cliente(nom_cliente, menor_fila)
        # se tiver caixa liberado e o lobby vazio adiciona na fila do caixa

    elif len(caixa_atual) == limite:
        lobby.entrar_lobby(nom_cliente)
        print(f'\n({" ".join(lobby.lobby)}) entrou no lobby.')
        print(f'Quantidade de pessoas aguardando: {len(lobby.lobby)}\n.')
        # se a fila do caixa chegar no limite adiciona no lobby

    elif len(lobby.lobby) > 0:
        lobby.entrar_lobby(nom_cliente)
        print(f'\n{nome_cliente} foi para o lobby de espera.')
        if len(caixa_atual) < limite:
            saiuDoLobby = lobby.liberar_lobby()
            print(f'Lobby: ({" ".join(lobby.lobby)}).')
            print(f'Quantidade no lobby: {len(lobby.lobby)}.\n')
            caixa.adiciona_cliente(saiuDoLobby, menor_fila)
            print(f'\n{foiParaFila} saiu do lobby e entrou na fila do caixa: {menor_fila}.')
        # se tiver alguem no lobby e tiver algum caixa com espaço, coloca no caixa e adiciona o atual no lobby

def remove_cliente():
    caixas = caixa.caixas
    nom_caixas = caixa.nom_caixas
    index_caixa = random.randint(0, len(caixas) - 1)
    _caixa = nom_caixas[index_caixa]

    if len(caixas[_caixa]) == 0:
        for i in caixas:
            if len(caixas[i]) > 0:
                _caixa = i
                break
        # Se a fila do caixa aleatorio estiver vazia ele verifica os outros

    if len(caixas[_caixa]) == 0:
        print('\nTodos os caixas estão vasios')

    elif len(caixas[_caixa]) > 0:
        cliente_removido = caixas[_caixa][0]
        caixa.remove_cliente(_caixa, 0)
        print(f"O cliente {cliente_removido} saio do caixa: {_caixa}.")

    if len(lobby.lobby) > 0:
        saiuDoLobby = lobby.liberar_lobby()
        print(f'Lobby: ({" ".join(lobby.lobby)}).')
        print(f'Quantidade no lobby: {len(lobby.lobby)}.\n')
        caixa.adiciona_cliente(saiuDoLobby, _caixa)
        print(f'\n{foiParaFila} saiu do lobby e entrou na fila do caixa: {_caixa}.')

def ver_fila_caixa(nom_caixa):
    if nom_caixa in caixa.caixas:
        fila_caixa = caixa.ver_fila_caixa(nom_caixa)
        print(f"\n Caixa: {nom_caixa}\n Fila: {' '.join(fila_caixa)}.")
    else:
        print(f"{nom_caixa} não está no caixa.")

def ver_lobby():
    print(f"\nLobby de espera: {' '.join(lobby.lobby)}.")
    print(f"Quantidade de pessoas no lobby: {len(lobby.lobby)}")

def ver_caixas():
    print(f"Caixas: {' '.join(caixa.nom_caixas)}\n")