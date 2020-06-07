class Caixas:
            
    def __init__(self):
        self.caixas = []
        self.nom_caixas = []
        self.index_fila = 0

    def ver_fila_caixa(self, index):
        return self.caixas[index].fila

    def adiciona_caixa(self, caixa):
        self.caixas.append(caixa)
        self.nom_caixas.append(caixa.nome)

    def remove_caixa(self, index):
        del(self.caixas[index])
        del(self.nom_caixas[index])

    def acha_menor_fila(self):
        total_caixas = len(self.nom_caixas)
        index = self.index_fila
        if index == total_caixas:
            index = 0
            self.index_fila = 0
        else:
            self.index_fila += 1

        return index

    def adiciona_cliente(self, index, cliente):
        self.caixas[index].fila.append(cliente)

    def remove_cliente(self, index, posicao):
        self.caixas[index].fila.pop(posicao)