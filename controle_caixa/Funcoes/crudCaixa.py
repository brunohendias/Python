import sys
sys.path.append('..')# Necessario para import de modulos em pasta anterior
from random import randint

# Classes do caixa
from Classes.Caixas.caixas import Caixas
from Classes.Caixas.caixa import Caixa
caixas = Caixas()

def ver_caixas():
    print(f"Caixas: {', '.join(caixas.nom_caixas)}\n")

def ver_caixa():
    ver_caixas()
    nome_cliente = input("Nome do caixa: ")
    try:
        index = caixas.nom_caixas.index(nome_cliente)
        print(f"{caixas.ver_caixa(index)}")
    except:
        print("Caixa não encontrado")

def ver_fila_caixa():
    ver_caixas()
    nom_caixa = input("Digite o nome do caixa para ver a fila: ")
    try:
        index = caixas.nom_caixas.index(nom_caixa)
        fila_caixa = caixas.ver_fila_caixa(index)
        print(f"\nCaixa: {nom_caixa}\nFila: {' '.join(fila_caixa)}.")
    except:
        print(f"{nom_caixa} não está no caixa.")

def acha_menor_fila():
    index = caixas.acha_menor_fila()
    _caixa = caixas.caixas[index]
    
    return {'caixa': _caixa, 'index': index}

def caixa_aleatorio():
    index = randint(0, len(caixas.nom_caixas) - 1)
    _caixa = caixas.caixas[index]
    if len(_caixa.fila) == 0:
        caixa_aleatorio()
        # Se a fila do caixa aleatorio estiver vazia ele sorteia outro

    return {'caixa': _caixa, 'index': index}

def adiciona_caixa():
    ver_caixas()
    nom_caixa = input("Nome do caixa a ser adicionado: ").lower()
    if nom_caixa == '':
        return False
    elif nom_caixa in caixas.nom_caixas:
        print(f"O {nom_caixa} já está no caixa.")
    
    else:
        caixa = Caixa()
        caixa.nome = nom_caixa
        dinheiro = input("Dinheiro inicial do caixa: ").replace(',', '.')
        try:
           dinheiro = float(dinheiro)
           caixa.dinheiro_inicial = dinheiro
           caixa.dinheiro_final = dinheiro
        except:
            print("Valor invalido, o caixa iniciara com o valor padrão\n")

        limiteFila = input("Limite de clientes na fila: ")
        try:
            limiteFila = int(limiteFila)
            caixa.limiteFila = limiteFila
        except:
            print("Valor invalido, o caixa iniciara com o limite padrão\n")
        
        caixas.adiciona_caixa(caixa)
    
    return True

def remove_caixa():
    ver_caixas()
    nom_caixa = input("Digite o nome do caixa a ser removido: ")
    try:
        index = caixas.nom_caixas.index(nom_caixa)
        tot_clientes = len(caixas.caixas[index].fila)

        if tot_clientes == 0:
            caixas.remove_caixa(index)
            print(f"O caixa {nom_caixa} foi removido com sucesso.")
        else:
            print("O caixa não pode ser removido porque contem cliente")
    except:
        print(f"{nom_caixa} não está no caixa.")

def adiciona_cliente_caixa(index, novo_cliente):
    caixas.adiciona_cliente(index, novo_cliente)

def remove_cliente_caixa(index, posicao):
    caixas.remove_cliente(index, posicao)