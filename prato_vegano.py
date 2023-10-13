#pegar a quantidade de pediddos e armazenar numa lista
numPedidos = int(input("Digite a quantidade de pedidos: "))
pedidos = []

#rodar o for de acordo com a quantidade pedidos para responder às questões
for i in range(1, numPedidos + 1):
    prato = input("Digite o prato: ")
    calorias = int(input("Digite o número de calorias: "))
    vegano = input("O prato é vegano? Digite 'S' para sim ou 'N' para não.).upper()

#rodar o if/else e armazenar os resultados na lista pedidos
    if vegano == "N":
        ehVegano = False
        pedidos.append(f"Pedido {i} : {prato} Não-Vegano {calorias} calorias")
    elif vegano == "S":
        ehVegano = True
        pedidos.append(f"Pedido {i} : {prato} Vegano {calorias} calorias")
    else:
        pedidos.append("Error")

# Exibindo os pedidos

for pedido in pedidos:
    print(pedido)
