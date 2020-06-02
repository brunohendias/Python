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
        if len(self.caixas[nome]) == 0:
            del(self.caixas[nome])
            return f"O caixa {nome} foi removido com sucesso."
        return "O caixa não pode ser removido porque contem cliente"

    def ver_fila_caixa(self, caixa):
        return self.caixas[caixa]
