#!/usr/bin/python3
class Caixa:

    def __init__(self):
        self.nome = ''
        self.dinheiro_inicial = ''
        self.fila = []
        self.limiteFila = 5

    def __str__(self):
    	return f"Nome: {self.nome}\nDinheiro: {self.dinheiro_inicial}\nFila: {self.fila}\nLimite: {self.limiteFila}"

caixa = Caixa()
caixas = []

caixa.nome = 'bruno'
caixa.dinheiro_inicial = 3000
caixa.fila = ['marta', 'maria', 'jose']
caixas.append(caixa)

caixa.nome = 'jose'
caixa.dinheiro_inicial = 7000
caixa.fila = ['leticia', 'josana', 'vitor']
caixas.append(caixa)