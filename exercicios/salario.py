salario = float(input("Quanto voce ganha por hora: "))
horas = float(input("Quantas horas voce trabalha no mes: "))
tot = salario * horas
print("Voce recebe no mes R$%.2f"%tot)
imp_renda = (tot /100)* 11
tot -= imp_renda
inss = (tot / 100)* 8
tot -= inss
sindicato = (tot / 100)* 5
tot -= sindicato
print("Foi retirado para o imposto de renda R$%.2f"%imp_renda)
print("Foi descontado do seu salario R$%.2f para o INSS"%inss)
print("Foi pago R$%.2f ao sindicato"%sindicato)
print("Salario liquido: R$%.2f"%tot)
