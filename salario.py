#!/usr/bin/python3

salario = str(input("\nSalario bruto: "))
vl_bruto = salario
v_a = str(input("Valor total do vale alimentação: "))
v_t = str(input("vale transporte:[y/N] ").lower())

def formata_valor(valor):
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
	elif salario > 5645.80:
		vl_inss = 621.04
	salario -= vl_inss
	if percent:
		percent = f"retirando {percent}%"
	else:
		percent = f" - {vl_inss}"
	print(f"R${formata_valor(old_salario)} - R${color(vl_inss, 91)} INSS {percent} = R${formata_valor(salario)}")
	return salario

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
		salario -= vl_ir
		print(f"R${formata_valor(old_salario)} - R${color(vl_ir, 91)} IR retirando {formata_valor(percent)}% = R${formata_valor(salario)}")
	return salario

def despesas(salario, va, vt, vlbruto):
	if type(salario) == float or type(salario) == int:
		print("\nDespesas")
		old_salario = salario
		aluguel = 800
		salario -= aluguel
		print(f"R${formata_valor(old_salario)} - R${color(aluguel, 91)} Aluguel = R${formata_valor(salario)}")
		if va:
			try:
				va = float(va)
				percent = 20
				desconto_va = va * percent / 100
				salario += va
				print(f"\nR${color(va, 92)} Vale alimentação\nSalario + Vale = R${round(salario, 2)}")
				salario -= desconto_va
				print(f"descontando se usar tudo "+"\033[1;91m"+f"R${formata_valor(desconto_va)}({percent}%)"+"\033[0;0m"+f" = R${formata_valor(salario)}")
			except:
				print("\033[1;91m"+"valor do vale invalido"+"\033[0;0m")
		if vt == 'y':
			vlbruto = float(vlbruto)
			percent = 8
			desconto_vt = vlbruto * percent / 100
			salario -= desconto_vt
			print(f"\nR${color(desconto_vt, 91)} Vale transporte\nSalario - vale transporte = R${formata_valor(salario)}\nVale transporte desconta {percent}% do valor bruto")
		return salario
	else:
		return False

def adicional(vl_liq):
	print("digite 0 para finalizar\n")
	salario = vl_liq
	itens_adicional = []
	while True:
		adicional = str(input("Gasto adicional: ")).replace(',','.')
		if adicional == '0':
			break
		try:
			adicional = float(adicional)
			itens_adicional.append(adicional)
		except:
			print("Valor invalido")
	for i in range(len(itens_adicional)):
		old_salario = salario
		salario -= itens_adicional[i]
		print(f"R${formata_valor(old_salario)} - R${color(itens_adicional[i], 91)} = {color(salario, 91)}")
	print(f"R${color(vl_liq, 92)} - {len(itens_adicional)} itens adicionais = Valor liquido R${color(salario, 91)}\n")

vl_liq = round(despesas(ir(inss(salario)), v_a, v_t, vl_bruto), 2)

def resultado(vl_liquido, vlbruto):
	try:
		vlbruto = float(vlbruto)
		diferenca = vl_liquido - vlbruto
		print(f"\nR${color(float(vlbruto), 92)} Valor bruto\nR${color(vl_liquido, 91)} Valor final(liquido)\nDiferença R${color(diferenca, 91)}\n")
	except:
		return False

resultado(vl_liq, vl_bruto)

adicionar = input("Adicionar mais algum gasto?:[y/N] ").lower()
if adicionar == 'y':
	adicional(vl_liq)
else:
	quit()