#!/usr/bin/python3

class Caixa:
            
    def __init__(self):
        self.caixas = {}
        self.nom_caixas = []
        self.limitePorCaixa = 5
        self.index_fila = 0

    def ver_fila_caixa(self, caixa):
        return self.caixas[caixa]

    def adiciona_caixa(self, nome):
        self.caixas[nome] = []
        self.nom_caixas.append(nome)

    def remove_caixa(self, nome):
        del(self.caixas[nome])
        self.nom_caixas.remove(nome)

    def acha_menor_fila(self):
        total_caixas = len(self.nom_caixas)
        if total_caixas == self.index_fila:
            menor_fila = self.nom_caixas[0]
            self.index_fila = 1
        else:
            menor_fila = self.nom_caixas[self.index_fila]
            self.index_fila += 1

        return menor_fila

    def adiciona_cliente(self, nom_cliente, menor_fila):
        self.caixas[menor_fila].append(nom_cliente)

    def remove_cliente(self, fila, posicao):
        self.caixas[fila].pop(posicao)