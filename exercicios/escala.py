ini = int(input("deseja iniciar em qual numero: "))
fim = int(input("deseja parar em qual numero: "))
fim += 1
while ini < fim:
    print(" %d"%ini*ini)
    ini += 1
