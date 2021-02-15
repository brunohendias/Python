#!/usr/bin/python3
class Cliente:

    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.dinheiro = 0
        self.caixa = ''
        self.carrinho = []

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nDinheiro: R${self.dinheiro}\nCarrinho: {', '.join(self.carrinho)}\nCaixa: {self.caixa}"

    def __repr__(self):
        return self.nome