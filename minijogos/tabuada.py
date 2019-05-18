print("Ola! Bem vindo!\n")
while True:
    num = int(input("Deseja ver a Tabuada de qual numero: "))
    ini = int(input("Começar no numero: "))
    fim = int(input("Ate qual numero: "))
    operador = int(input("Digite [1]para Multiplicação [2]para Divisão [3]para Soma [4]para Subtração: "))
    if operador == 1:
        while ini < fim:
            ini += 1
            resultado = ini * num
            print(f"{ini} X {num} = {resultado}")

    elif operador == 2:
        while ini < fim:
            ini += 1
            resultado = ini / num
            print(f"{ini} / {num} = {resultado}")
 
    elif operador == 3:
        while ini < fim:
            ini += 1
            resultado = ini + num
            print(f"{ini} + {num} = {resultado}")

    elif operador == 4:
        while ini < fim:
            ini += 1
            resultado = ini - num
            print(f"{ini} - {num} = {resultado}")
