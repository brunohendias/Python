print("~="*35)
print("Seja bem vindo ao Jogo da forca ")
print("~="*35)
palavra_chave = ["b","r","a","s","i","l"]
letras_descobertas = []
letras_erradas = []
tot_erro = 0
for i in range(0, len(palavra_chave)):
    letras_descobertas.append("-")
acertou = False
while acertou == False:
    letra = input("Letra: ")
    for i in range(0, len(palavra_chave)):
        if letra == palavra_chave[i]:
            letras_descobertas[i] = letra
        print(letras_descobertas[i])
    if letra not in palavra_chave:
        letras_erradas.append(letra)
        tot_erro += 1 
    acertou = True
    for x in range(0, len(letras_descobertas)):
        if letras_descobertas[x] == "-":
            acertou = False
