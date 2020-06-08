class Caixas:
            
    def __init__(self):
        self.caixas = []
        self.nom_caixas = []
        self.index_fila = 0

    def ver_fila_caixa(self, index):
        return self.caixas[index].nom_clientes

    def adiciona_caixa(self, caixa):
        self.caixas.append(caixa)
        self.nom_caixas.append(caixa.nome)

    def remove_caixa(self, index):
        del(self.caixas[index])
        del(self.nom_caixas[index])

    def acha_menor_fila(self):
        menor_fila = self.caixas[self.index_fila].fila
        limite = len(self.caixas)

        for i in range(limite):
            if len(menor_fila) > len(self.caixas[i].fila):
                menor_fila = self.caixas[i].fila
                self.index_fila = i

        return self.index_fila

    def adiciona_cliente(self, index, cliente):
        self.caixas[index].fila.append(cliente)
        self.caixas[index].nom_clientes.append(cliente.nome)

    def remove_cliente(self, index, posicao):
        self.caixas[index].fila.pop(posicao)
        self.caixas[index].nom_clientes.pop(posicao)