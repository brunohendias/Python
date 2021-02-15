import sys
sys.path.append('..')# Necessario para import de modulos em pasta anterior

# Classes do lobby
from Classes.Lobby.lobby import Lobby
lobby = Lobby()

def quantidade_lobby():
	return len(lobby.nom_clientes)

def clientes_lobby():
	return ', '.join(lobby.nom_clientes)

def ver_lobby():
    print(f"\nLobby de espera: {clientes_lobby()}.")
    print(f"Quantidade de pessoas no lobby: {quantidade_lobby()}")

def entrar_lobby(novo_cliente):
	novo_cliente.caixa = 'lobby'
	lobby.entrar_lobby(novo_cliente)
	print(f'\n{novo_cliente.nome} foi para o lobby de espera.')

def liberar_lobby():
	return lobby.liberar_lobby()