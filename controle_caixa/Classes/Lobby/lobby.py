#!/usr/bin/python3

class Lobby:

    def __init__(self):
        self.lobby = []
        self.nom_clientes = []

    def entrar_lobby(self, cliente):
    	self.lobby.append(cliente)
    	self.nom_clientes.append(cliente.nome)

    def liberar_lobby(self):
        foiParaFila = self.nom_clientes[0]
        self.lobby.pop(0)
        self.nom_clientes.pop(0)

        return foiParaFila
