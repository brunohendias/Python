#!/usr/bin/python3
import random

class Cliente:

    def __init__(self):
        self.lobby = []
        
    def entrar(self, nome, caixas, nom_caixas, limitePorCaixa):
        menor_fila = nom_caixas[0]
        fila = caixas[menor_fila]
        limite = limitePorCaixa
        
        for nom_caixa in caixas:
            if len(fila) > len(caixas[nom_caixa]):
                fila = caixas[nom_caixa]
                menor_fila = nom_caixa
                # verifica qual fila tem menos
                
        if len(fila) == limite:
            self.entrar_lobby(nome)
            # se a fila do caixa chegar no limite adiciona no lobby
 
        elif len(self.lobby) > 0:
            self.lobby.append(nome)
            print(f'\n{nome} foi para o lobby de espera.')
            self.liberar_lobby(menor_fila)
            # se tiver alguem no lobby coloca no caixa e adiciona o atual no lobby

        elif len(fila) < limite and len(self.lobby) == 0:
            caixas[menor_fila].append(nome)
            # se não tiver no limite e o lobby vazio adiciona na fila do caixa

        return caixas

    def sair(self, caixas, nom_caixas):
        total_caixas = len(caixas) - 1
        caixa = random.randint(0, total_caixas)
        caixa = nom_caixas[caixa]

        if len(caixas[caixa]) == 0:
            for i in caixas:
                if len(caixas[i]) > 0:
                    caixa = i
                    break
            # Se a fila do caixa aleatorio estiver vazia ele verifica os outros
        
        if len(self.lobby) > 0:
            self.liberar_lobby(caixa)

        elif len(caixas[caixa]) > 0:
            cliente_removido = caixas[caixa][0]
            caixas[caixa].pop(0)
            print(f"O cliente {cliente_removido} saio do caixa: {caixa}.")
            
        return caixas

    def entrar_lobby(self, nome):
        self.lobby.append(nome)
        print(f'\n({" ".join(self.lobby)}) entrou no lobby.')
        print(f'Quantidade de pessoas aguardando: {len(self.lobby)}\n.')

    def liberar_lobby(self, menor_fila):
        entrarNaFila = self.lobby[0]
        self.caixas[menor_fila].append(entrarNaFila)
        self.lobby.pop(0)
        qtd_lobby = len(self.lobby)
        print(f'\n{entrarNaFila} saiu do lobby e entrou na fila do caixa: {menor_fila}.')
        print(f'Lobby: ({" ".join(self.lobby)}).')
        print(f'Quantidade no lobby: {qtd_lobby}.\n')
