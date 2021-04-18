#!/usr/bin/python3
from random import randint
from Variables import menor_numero, maior_numero

def gera_numero():
    return randint(menor_numero, maior_numero)

def array_string(array):
    return ''.join(str(sorted(array)).strip('[]'))

def gera_bilhete(qtd_numeros):
    bilhete = []
    while len(bilhete) < qtd_numeros:
        num = gera_numero()
        while num in bilhete:
            num = gera_numero()
        bilhete.append(num)
    
    return bilhete