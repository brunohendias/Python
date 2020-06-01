# Programa para automatizar o controle de fila
# Feito por: https://github.com/brunohendias
# Data: 09/05/2020
import random

class Caixa:
            
    def __init__(self):
        self.caixas = {}
        self.lobby = []
        self.nom_caixas = []
        self.limitePorCaixa = 5

    def adiciona_caixa(self):
        nome = input("Digite o nome do caixa: ")
        self.caixas[nome] = []
        self.nom_caixas.append(nome)
        
    def entrar(self, nome):
        menor_fila = self.nom_caixas[0]
        fila = self.caixas[menor_fila]
        limite = self.limitePorCaixa
        
        for nom_caixa in self.caixas:
            if len(fila) > len(self.caixas[nom_caixa]):
                fila = self.caixas[nom_caixa]
                menor_fila = nom_caixa
                # verifica qual fila tem menos
                
        if len(fila) == limite:
            self.entrar_lobby(nome)
            # se a fila do caixa chegar no limite adiciona no lobby
 
        elif len(self.lobby) > 0:
            self.lobby.append(nome)
            print(f'\n{nome} foi para o lobby')
            self.liberar_lobby(menor_fila)
            # se tiver alguem no lobby coloca no caixa e adiciona o atual no lobby

        elif len(fila) < limite and len(self.lobby) == 0:
            self.caixas[menor_fila].append(nome)
            # se não tiver no limite e o lobby vazio adiciona na fila do caixa

    def sair(self):
        total_caixas = len(self.caixas) - 1
        caixa = random.randint(0, total_caixas)
        caixa = self.nom_caixas[caixa]

        if len(self.caixas[caixa]) == 0:
            for i in self.caixas:
                if len(self.caixas[i]) > 0:
                    caixa = i
                    break
            # Se a fila do caixa aleatorio estiver vazia ele verifica os outros
        
        elif len(self.caixas[caixa]) > 0:
            self.caixas[caixa].pop(0)
        
        qtd_lobby = len(self.lobby)
        if qtd_lobby > 0:
            self.liberar_lobby(caixa)

    def entrar_lobby(self, nome):
        self.lobby.append(nome)
        print(f'\n({" ".join(self.lobby)}) Aguardando alguma fila esvaziar')
        print(f'Quantidade de pessoas aguardando: {len(self.lobby)}\n')

    def liberar_lobby(self, menor_fila):
        entrarNaFila = self.lobby[0]
        self.caixas[menor_fila].append(entrarNaFila)
        self.lobby.pop(0)
        qtd_lobby = len(self.lobby)
        print(f'\n{entrarNaFila} saiu do lobby e entrou na fila do caixa: {menor_fila}')
        print(f'Lobby: ({" ".join(self.lobby)})')
        print(f'Quantidade no lobby: {qtd_lobby}\n')

