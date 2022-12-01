try:
    ini = int(input("deseja iniciar em qual numero: "))
    fim = int(input("deseja parar em qual numero: "))
    while ini <= fim:
        print(" %d"%fim*fim)
        fim -= 1
except:
    print('Aceitamos apenas numeros')