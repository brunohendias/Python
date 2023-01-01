class Caixa:
    nome = ''
    dinheiro = 1000.00
    fila = []
    limite = 5
    def __init__(self):
        self.dinheiro_inicial = self.dinheiro
    def __str__(self):
        return f"\nNome: {self.nome}\nDinheiro: R${round(self.dinheiro, 2)}\nFila: {self.fila}\nLimite: {self.limiteFila}"
    def __repr__(self):
    	return self.nome
    def add_cliente(self, cliente):
        if len(self.fila) < self.limite:
            self.fila.append(cliente)
    def rm_cliente(self, cliente):
        if cliente < 0 or cliente > len(self.fila):
            return 'cliente nao esta na fila'
        del(self.fila[cliente])