from Models.Fila import Fila
from Models.Caixa import Caixa
class Cliente:
    nome = ''
    idade = 0
    dinheiro = 0
    carrinho = Fila()
    def __str__(self):
        return f"{self.nome} {self.idade} anos\nR${self.dinheiro}\nCarrinho: {self.carrinho.fila}"
    def __repr__(self):
        return self.nome
