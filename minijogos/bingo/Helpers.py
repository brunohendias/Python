#!/usr/bin/python3
from random import randint
from Variables import menor_numero, maior_numero, tamanho_cartela, limite_colunas

def gera_numero():
    return randint(menor_numero, maior_numero)

def gera_cartela():
    cartela = []
    for i in range(tamanho_cartela):
        num = gera_numero()
        while num in cartela:
            num = gera_numero()
        cartela.append(num)
    return cartela

def linha():
    print("\n -------------------------")

def mostra_cartela(cartela):
    nova = sorted(cartela)
    atual = 0
    linha()
    for num in nova:
        atual += 1
        if atual == limite_colunas:
            linha()
            atual = 0
        elif int(num) < 10:
            print(f"   {num}", end="", flush=True)
        else:
            print(f"  {num}", end="", flush=True)