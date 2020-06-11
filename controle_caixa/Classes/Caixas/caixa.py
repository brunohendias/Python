#!/usr/bin/python3
class Caixa:

    def __init__(self):
        self.nome = ''
        self.dinheiro_inicial = 1000.00
        self.dinheiro_final = 1000.00
        self.fila = []
        self.nom_clientes = []
        self.limiteFila = 5

    def __str__(self):
        return f"\nNome: {self.nome}\nDinheiro inicial: R${self.dinheiro_inicial}\nDinheiro atual: R${round(self.dinheiro_final, 2)}\nFila: {self.fila}\nLimite: {self.limiteFila}"

    def __repr__(self):
    	return self.nome