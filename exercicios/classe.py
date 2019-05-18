# treinando orientação em objeto com python
# criando uma familia

class pessoa:
    def __init__(self, nome, idade, sexo, tamanho, peso):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.tamanho = tamanho
        self.peso = peso

    def __repr__(self):
        return f'pessoa({self.nome}, {self.idade}, {self.sexo}, {self.tamanho}, {self.peso})'

pai = pessoa("Reni", 40, "masculino", 1.80, 90)
mae = pessoa("Katia", 32, "feminino", 1.70, 80)
filha = pessoa("Evelyn", 11, "feminino", 1.50, 50)
filho = pessoa("Bruno", 20, "masculino", 1.70, 80)

print(pai, mae, filha, filho)
