class Fila:
    fila = []
    def add(self, obj):
        self.fila.append(obj)
    def rm(self, obj):
        del(self.fila[obj])