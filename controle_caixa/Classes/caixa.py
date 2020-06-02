#!/usr/bin/python3

class Caixa:
            
    def __init__(self):
        self.caixas = {}
        self.nom_caixas = []
        self.limitePorCaixa = 5

    def adiciona_caixa(self, nome):
        self.caixas[nome] = []
        self.nom_caixas.append(nome)

    def remove_caixa(self, nome):
        pass

    def ver_fila_caixa(self, caixa):
        return self.caixas[caixa]

