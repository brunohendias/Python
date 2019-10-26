#!/usr/bin/python3
import locale
locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')

salario = str(input("\nSalario bruto: "))
try:
	salario = float(salario.replace(',', '.'))
	vl_bruto = salario
except:
	print("\033[1;91m"+"Valor do salario invalido"+"\033[0;0m")
	quit()
v_a = str(input("Valor total do vale alimentação: "))
v_t = str(input("Vale transporte:[y/N] ").lower())
adicionar = input("Adicionar mais algum gasto?:[y/N] ").lower()

def formata_valor(valor):
	try:
		valor = str(locale.currency(valor, grouping=True))
	except:
		valor = str(round(valor, 2)).replace('.', ',')
	return valor

def color(valor, cor):
	valor = f"\033[1;{cor}m"+f"{formata_valor(valor)}"+"\033[0;0m"
	return valor

def inss(salario):
	old_salario = salario
	if salario <= 5645.80:
		if salario <= 1693.72:
			percent = 8
		elif salario >= 1693.73 and salario < 2822.90:
			percent = 9
		elif salario >= 2822.90 and salario < 5645.80:
			percent = 11
		vl_inss = salario * percent / 100
		salario -= vl_inss
		percent = f"retirando {percent}%"
	elif salario > 5645.80:
		vl_inss = 621.04
		percent = ''
		salario -= vl_inss

	return old_salario, vl_inss, percent, salario

def ir(salario):
	old_salario = salario
	try:
		salario = float(salario)
		if salario > 1904:
			if salario >= 1904 and salario <= 2826.65:
				percent = 7.5
			elif salario > 2826.65 and salario <= 3751.05:
				percent = 15
			elif salario > 3751.05 and salario <= 4664.68:
				percent = 22.5
			elif salario > 4664.68:
				percent = 27.5
			vl_ir = salario * percent / 100
			percent = str(percent) + '%'
			salario -= vl_ir
		elif salario < 1904:
			vl_ir = 0
			percent = 0
			print("\033[1;92m"+"Salario abaixo de $1904.00 não e cobrado o IR"+"\033[0;0m")
	except:
		print("\033[1;91m"+"Impossivel calcular IR. Salario não definido"+"\033[0;0m")
		quit()

	return old_salario, vl_ir, percent, salario

def vl_va(salario, va):
	percent = 20
	desconto = va * percent / 100
	salario += va
	soma = salario
	salario -= desconto
	return salario, desconto, percent, soma

def vl_vt(salario, vl_bruto):
	try:
		vl_bruto = float(str(vl_bruto).replace(',', '.'))
		percent = 8
		desconto = vl_bruto * percent / 100
		salario -= desconto
		return salario, desconto, percent
	except:
		return salario

def vl_aluguel(salario):
	old_salario = salario
	aluguel = 800
	salario -= aluguel
	return old_salario, salario, aluguel

def gasto_adicional():
	despesa_adicional = []
	while True:
		adicional = str(input("Gasto adicional: ")).replace(',','.')
		if adicional == '0':
			break
		try:
			adicional = float(adicional)
			nome = input("Nome: ")
			despesa_adicional.append({'val': adicional, 'nome': nome})
		except:
			print("Valor invalido")
	return despesa_adicional

def arquivo(salario, vl_bruto, v_a):
	try:
		arquivo = open(input("nome do arquivo: "), 'w+')
	except:
		arquivo = open("extrato_salario.txt", "w+")
		print("\033[1;91m"+"Erro ao criar o nome\nArquivo criado com nome: extrato_salario.txt"+"\033[0;0m")
	#INSS
	arquivo.write("\nImpostos")
	old_salario, vlinss, percent_inss, salario = inss(salario)
	arquivo.write(f"\n{formata_valor(old_salario)} - {color(vlinss, 91)} INSS {percent_inss} = {formata_valor(salario)}\n")
	#IR
	old_salario, vlir, percent_ir, salario = ir(salario)
	arquivo.write(f"{formata_valor(old_salario)} - {color(vlir, 91)} IR {percent_ir} = {formata_valor(salario)}\n")

	#DESPESAS
	arquivo.write("\nDespesas")
	old_salario, salario, aluguel = vl_aluguel(salario)
	arquivo.write(f"\n{formata_valor(old_salario)} - {color(aluguel, 91)} Aluguel = {formata_valor(salario)}\n")
	#Vale alimentação
	if v_a and v_a != '0':
		try:
			va = float(str(v_a).replace(',', '.'))
			salario, desconto, percent, soma = vl_va(salario, va)
			arquivo.write(f"\n{color(float(va), 92)} Vale alimentação\nSalario + Vale alimentação = {formata_valor(soma)}\nDescontando se usar tudo "+"\033[1;91m"+f"{formata_valor(desconto)}({percent}%)"+"\033[0;0m"+f" = {formata_valor(salario)}\n")
		except:
			print("\n\033[1;91m"+"valor do vale alimentação invalido"+"\033[0;0m\n")
	#Vale transporte
	if v_t == 'y':
		salario, desconto, percent = vl_vt(salario, vl_bruto)
		arquivo.write(f"\n{color(desconto, 91)} Vale transporte\nSalario - vale transporte = {formata_valor(salario)}\nVale transporte desconta {percent}% do valor bruto\n")

	#diferença
	try:
		vl_bruto = float(str(vl_bruto).replace(',', '.'))
		diferenca = salario - vl_bruto
		arquivo.write(f"\n{color(vl_bruto, 92)} Valor bruto\n{color(salario, 91)} Valor final(liquido)\nDiferença {color(diferenca, 91)}\n")
	except:
		print("\nSalario não e valido\n")

	#Gasto adicional
	if adicionar == 'y':
		print("\nDigite 0 para finalizar")
		despesas_ad = gasto_adicional()
		salario_liq = salario
		for i in range(len(despesas_ad)):
			old_salario = salario
			salario -= float(despesas_ad[i]['val'])
			arquivo.write(f"\n{formata_valor(old_salario)} - {color(despesas_ad[i]['val'], 91)} {despesas_ad[i]['nome']} = {color(salario, 91)}")
		arquivo.write(f"\n{color(salario_liq, 92)} - {len(despesas_ad)} itens adicionais = Valor liquido {color(salario, 91)}\n")
	quit()

arquivo(salario, vl_bruto, v_a)