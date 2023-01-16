from sys import path
path.append('..')
from Models.Fila import Fila
lobby = Fila()

def show():
    return lobby

def add(cliente):
	lobby.add(cliente)
	print(f'{cliente.nome} foi para o lobby de espera.')

def rm():
	cliente = lobby[0]
	lobby.rm(0)
	return cliente