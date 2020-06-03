#!/usr/bin/python3
import random

class Cliente:
        
    def entrar(self, nome, caixa, lobby):
        limitePorCaixa = caixa.limitePorCaixa
        nom_caixas = caixa.nom_caixas
        caixas = caixa.caixas
        menor_fila = nom_caixas[0]
        fila = caixas[menor_fila]
        limite = limitePorCaixa
        
        for nom_caixa in caixas:
            if len(fila) > len(caixas[nom_caixa]):
                fila = caixas[nom_caixa]
                menor_fila = nom_caixa
                # verifica qual fila tem menos
                
        if len(fila) == limite:
            lobby.entrar_lobby(nome)
            # se a fila do caixa chegar no limite adiciona no lobby
 
        elif len(lobby.lobby) > 0:
            lobby.lobby.append(nome)
            print(f'\n{nome} foi para o lobby de espera.')
            lobby.liberar_lobby(menor_fila)
            # se tiver alguem no lobby coloca no caixa e adiciona o atual no lobby

        elif len(fila) < limite and len(lobby.lobby) == 0:
            caixas[menor_fila].append(nome)
            # se não tiver no limite e o lobby vazio adiciona na fila do caixa

        return caixas

    def sair(self, caixa, lobby):
        caixas = caixa.caixas
        nom_caixas = caixa.nom_caixas
        caixa = random.randint(0, len(caixas) - 1)
        caixa = nom_caixas[caixa]

        if len(caixas[caixa]) == 0:
            for i in caixas:
                if len(caixas[i]) > 0:
                    caixa = i
                    break
            # Se a fila do caixa aleatorio estiver vazia ele verifica os outros
        
        if len(caixas[caixa]) > 0:
            cliente_removido = caixas[caixa][0]
            caixas[caixa].pop(0)
            print(f"O cliente {cliente_removido} saio do caixa: {caixa}.")        

        if len(lobby.lobby) > 0:
            caixas = lobby.liberar_lobby(caixas, caixa)

            
        return caixas
