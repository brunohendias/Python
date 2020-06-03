#!/usr/bin/python3

class Lobby:

    def __init__(self):
        self.lobby = []

    def entrar_lobby(self, nome):
        self.lobby.append(nome)
        print(f'\n({" ".join(self.lobby)}) entrou no lobby.')
        print(f'Quantidade de pessoas aguardando: {len(self.lobby)}\n.')

    def liberar_lobby(self, caixa, menor_fila):
        entrarNaFila = self.lobby[0]
        caixa[menor_fila].append(entrarNaFila)
        self.lobby.pop(0)
        print(f'\n{entrarNaFila} saiu do lobby e entrou na fila do caixa: {menor_fila}.')
        print(f'Lobby: ({" ".join(self.lobby)}).')
        print(f'Quantidade no lobby: {len(self.lobby)}.\n')

        return caixa
