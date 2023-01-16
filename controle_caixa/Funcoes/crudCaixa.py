from sys import path
path.append('..')
from random import randint
from Models.Caixa import Caixa
caixas = list()

def show():
    return caixas

def ver_caixa():
    show()
    print(find())

def menor_fila():
    menor = 100
    c = caixas[0]
    for caixa in caixas:
        tot = len(caixa.fila.fila)
        if tot == 0:
            return caixa
        elif tot < menor:
            menor = tot
            c = caixa
    return c

def find():
    nome = input("Digite o nome do caixa: ")
    for caixa in caixas:
        if caixa.nome == nome:
            return caixa
    return Caixa()

def add():
    show()
    try:
        c = Caixa()
        c.nome = input("Nome do caixa a ser adicionado: ").lower()
        c.dinheiro = float(input("Dinheiro inicial do caixa: ").replace(',', '.'))
        c.limite = int(input("Limite de clientes na fila: "))
        caixas.append(c)
    except:
        print("Valor invalido, Valores padrão setado")

def rm():
    show()
    caixa = find()
    if not caixa:
        return False
    elif len(caixa.fila.fila) > 0:
        return "O caixa possui cliente"
    del(caixas[caixas.index(caixa)])
    return "Removido com sucesso"

def add_cliente(caixa, cliente):
    caixas[caixas.index(caixa)].fila.add(cliente)

def rm_cliente(caixa, cliente):
    caixas[caixas.index(caixa)].fila.rm(cliente)