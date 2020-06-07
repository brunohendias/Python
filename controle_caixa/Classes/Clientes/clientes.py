class Clientes:

    def __init__(self):
        self.clientes = []
        self.nom_clientes = []

    def seta_cliente(self, cliente):
    	self.clientes.append(cliente)
    	self.nom_clientes.append(cliente.nome)

    def remove_cliente(self, index):
        del(self.nom_clientes[index])
        del(self.clientes[index])
        
    def ver_cliente(self, index):
    	return self.clientes[index]