arquivo = float(input("Qual o tamanho do arquivo: "))
formato = input("Tamanho do aquivo esta em GB ou MB: ").lower()
if formato == "gb":
    arquivo *= 1000
link = float(input("Qual a velocidade do link em Mbps: "))
velocidade = (arquivo / link) / 60
print("O tamanho do arquivo e %.2f MB e ira gastar %.2f minutos para baixar a uma velocidade de %.1f Mbps"%(arquivo, velocidade, link))
