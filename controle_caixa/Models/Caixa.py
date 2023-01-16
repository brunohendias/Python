from Models.Fila import Fila
class Caixa:
    nome = ''
    dinheiro = 1000.00
    fila = Fila()
    limite = 5
    def __init__(self):
        self.dinheiro_inicial = self.dinheiro
    def __str__(self):
        return f"\nNome: {self.nome}\nR${round(self.dinheiro, 2)}\nFila: {self.fila.fila}\nLimite: {self.limite}"
    def __repr__(self):
    	return self.nome
