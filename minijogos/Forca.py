# brincando com jogo forca
# 12/05/2019
# github.com/brunohendias

palavra_chave = ['b','r','a','s','i','l']
letras_certas, letras_erradas = [], []
total_acertos = 0
letra = ''

print(" Bem vindo ao jogo da forca\n\n Regra do jogo\n Digite uma letra por vez ate acertas todas\n O jogo termina quando errar mais de 6 veses ou acerta a palavra\n\n Boa sorte e bom jogo")
print(" Para sair digite sair\n Dica: E um pais\n")

for i in range(len(palavra_chave)):
    letras_certas.append('-')

while len(letras_erradas) < 6 and total_acertos < len(palavra_chave) and letra != 'sair':
    letra = input("Letra: ")
    if letra in palavra_chave:
        for i in range(0, len(palavra_chave)):
            if palavra_chave[i] == letra and letra not in letras_certas:
                letras_certas[i] = letra
                total_acertos += 1
        print(f'letras certas: {" ".join(letras_certas)}\n')
    elif letra not in palavra_chave and letra != 'sair':
        letras_erradas.append(letra)
        print(f'letras erradas: {" ".join(letras_erradas)}') 
