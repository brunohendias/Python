#!/usr/bin/python3
class Caixa:

    def __init__(self):
        self.nome = ''
        self.dinheiro_inicial = ''
        self.fila = []
        self.limiteFila = 5

    def __str__(self):
        return f"Nome: {self.nome}\nDinheiro: {self.dinheiro_inicial}\nFila: {self.fila}\nLimite: {self.limiteFila}"

    def __repr__(self):
    	return self.nome