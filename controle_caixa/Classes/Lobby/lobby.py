#!/usr/bin/python3

class Lobby:

    def __init__(self):
        self.lobby = []

    def entrar_lobby(self, cliente):
    	self.lobby.append(cliente)

    def liberar_lobby(self):
        foiParaFila = self.lobby[0] 
        self.lobby.pop(0)

        return foiParaFila
