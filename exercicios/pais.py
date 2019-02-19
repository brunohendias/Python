print("Pais A recebe pais com menor numero de habitantes")
a = float(input("Quantos habitantes tem no Pais A: "))
b = float(input("Quantos habitantes tem no Pais B: "))
while a > b:
    a = float(input("Quantos habitantes tem no Pais A: "))
por_a = float(input("Qual a porcentagem de crecimento anual do Pais A: "))
por_b = float(input("Qual a porcentagem de crecimento anual do Pais B: "))
while por_a < por_b:
    print("Pais A tem uma porcentagem de crecimento menor que a do pais B portanto pais A não alcançara Pais B")
    por_a = float(input("Qual a porcentagem de crecimento anual do Pais A: "))
a = (a*por_a)/100 + a
b = (b*por_b)/100 + b
tempo = 0
while b > a:
    a = (a*por_a)/100 + a
    b = (b*por_b)/100 + b
    tempo += 1
    if a >= b:
        print("gastara %d anos para Pais A igualar a população do Pais B"%tempo)
    
    
    
