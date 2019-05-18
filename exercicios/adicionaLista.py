nomes = []
print("Digite exit para parar\n")
nome = input("Adicionar nome: ")
nomes.append(nome)
cont = 0
for i in nomes:
    cont += 1
    nome = input("Adicionar nome: ")
    nomes.append(nome)
    if nome == "exit":
        print("Foi adicionado %d nomes"%cont)
        break
print(nomes[:-1])
pergunta = input("Deseja alterar algum nome [S/N]? ").lower 
if pergunta == "s":
    continua = True
    while continua:
        try:
            nome = int(input("Nome a ser alterado: "))
            nomes.remove(nome)
            nome = input("Novo nome: ")
            nomes.append(nome)
        except:
            continua = True        
        print(nomes[:-1])
        parar = input("Deseja parar?(exit) ")
        if parar == "exit":
            continua = False
print(nomes[:-1])
