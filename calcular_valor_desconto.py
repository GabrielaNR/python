p = int(input("Digite a quantidade de pedidos:"))
valor_total = 0

for i in range(p):
    pedido = input("Digite o nome do pedido e o valor separados por espaço: ").split()
    nome_pedido = pedido[0]
    valor_pedido = float(pedido[1])
    valor_total += valor_pedido

cupom = input("Escolha o cupom de desconto (cupom A = 10% ou cupom B = 20%): ").upper()
def calcular_desconto(valor_total, cupom):
    if cupom == "A":
        return valor_total * 0.9
    elif cupom == "B":
        return valor_total * 0.8
    else:
        return valor_total

valor_com_desconto = calcular_desconto(valor_total, cupom)

print("Valor total com desconto: {:.2f}".format(valor_com_desconto))
