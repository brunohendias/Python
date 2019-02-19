sexo = input("Digite seu sexo (homem/mulher): ").lower()
altura = float(input("Qual a sua altura: "))
if sexo == "homem":
    peso = (72.7*altura)-58
    print("Voce mede %.2f e seu peso ideal e %.2f"%(altura, peso))
elif sexo == "mulher":
    peso = (62.1*altura)-44.7
    print("Voce mede %.2f e seu peso ideal e %.2f"%(altura, peso))
