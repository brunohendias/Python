#!/usr/bin/python3
import locale
locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')

salario = str(input("\nSalario bruto: "))
vl_bruto = salario
v_a = str(input("Valor total do vale alimentação: "))
v_t = str(input("vale transporte:[y/N] ").lower())
adicionar = input("Adicionar mais algum gasto?:[y/N] ").lower()
#salvar = input("Salvar informações em um arquivo?[y/N] ").lower()

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
	try:
		salario = float(salario.replace(',', '.'))
	except:
		print("\033[1;91m"+"Valor do salario invalido"+"\033[0;0m")
		quit()
	old_salario = salario
	print("\nImpostos")
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
	except:
		print("\033[1;91m"+"Impossivel calcular IR. Salario não definido"+"\033[0;0m")
		quit()
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
	
	return old_salario, vl_ir, percent, salario

def vl_va(salario, va):
	percent = 20
	desconto_va = va * percent / 100
	salario += va
	soma_va = salario
	salario -= desconto_va
	return salario, desconto_va, percent, soma_va

def vl_vt(salario, vl_bruto):
	try:
		vl_bruto = float(str(vl_bruto).replace(',','.'))
		percent = 8
		desconto_vt = vl_bruto * percent / 100
		salario -= desconto_vt
		return salario, desconto_vt, percent
	except:
		return salario

def despesas(salario, va, vt):
	if type(salario) == float or type(salario) == int:
		print("\nDespesas")
		old_salario = salario
		aluguel = 800
		salario -= aluguel
		print(f"{formata_valor(old_salario)} - {color(aluguel, 91)} Aluguel = {formata_valor(salario)}")
		if va:
			try:
				va = float(str(va).replace(',','.'))
				salario, desconto_va, percent_va, soma_va = vl_va(salario, va)
				salario_va = salario
			except:
				va = 0
				desconto_va = 0
				percent_va = 0
				soma_va = salario
				salario_va = salario
				print("\033[1;91m"+"valor do vale alimentação invalido"+"\033[0;0m")
		else:
			va = 0
			desconto_va = 0
			percent_va = 0
			soma_va = salario
			salario_va = salario		
		
		if vt == 'y':
			salario, desconto_vt, percent_vt = vl_vt(salario, vl_bruto)
		else:
			desconto_vt = 0
			percent_vt = 8
		return salario, salario_va, va, desconto_va, percent_va, soma_va, desconto_vt, percent_vt
	else:
		return False

def gasto_adicional():
	print("\nDigite 0 para finalizar")
	despesa_adicional = []
	while True:
		adicional = str(input("Gasto adicional: ")).replace(',','.')
		if adicional == '0':
			break
		try:
			adicional = float(adicional.replace(',', '.'))
			nome = input("Nome: ")
			despesa_adicional.append({'val': adicional, 'nome': nome})
		except:
			print("Valor invalido")
	return despesa_adicional  

def impostos(old_salario, imposto, msg, percent, salario):
	print(f"{formata_valor(old_salario)} - {color(imposto, 91)} {msg} {percent} = {formata_valor(salario)}")

def resultado(salario):
	#INSS
	old_salario, vlinss, percent_inss, salario = inss(salario)
	impostos(old_salario, vlinss, 'INSS', percent_inss, salario)
	#IR
	old_salario, vlir, percent_ir, salario = ir(salario)
	impostos(old_salario, vlir, 'IR', percent_ir, salario)

	#DESPESAS
	salario, salario_va, va, desconto_va, percent_va, soma_va, desconto_vt, percent_vt = despesas(salario, v_a, v_t)
	#Vale alimentação
	print(f"\n{color(float(va), 92)} Vale alimentação\nSalario + Vale alimentação = {formata_valor(soma_va)}\nDescontando se usar tudo "+"\033[1;91m"+f"{formata_valor(desconto_va)}({percent_va}%)"+"\033[0;0m"+f" = {formata_valor(salario_va)}")
	#Vale transporte
	print(f"\n{color(desconto_vt, 91)} Vale transporte\nSalario - vale transporte = {formata_valor(salario)}\nVale transporte desconta {percent_vt}% do valor bruto")

	#diferença
	diferenca = salario - float(vl_bruto)
	print(f"\n{color(float(vl_bruto), 92)} Valor bruto\n{color(salario, 91)} Valor final(liquido)\nDiferença {color(diferenca, 91)}")

	#Gasto adicional
	despesas_ad = gasto_adicional()
	salario_liq = salario
	for i in range(len(despesas_ad)):
		old_salario = salario
		salario -= float(despesas_ad[i]['val'])
		print(f"{formata_valor(old_salario)} - {color(despesas_ad[i]['val'], 91)} {despesas_ad[i]['nome']} = {color(salario, 91)}")
	print(f"{color(salario_liq, 92)} - {len(despesas_ad)} itens adicionais = Valor liquido {color(salario, 91)}\n")

resultado(salario)