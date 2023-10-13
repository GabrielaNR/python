valorHamburguer = float(input("Valor do hamburgue: "))
quantidadeHamburguer = int(input("Quant hamburguer: "))
valorBebida = float(input("Valor goró: "))
quantidadeBebida = int(input("quant goró: "))
valorPago = float(input("valor pago: "))

hamburguerTotal = valorHamburguer * quantidadeHamburguer
bebidaTotal = valorBebida * quantidadeBebida
valorTotal = hamburguerTotal + bebidaTotal
troco = valorPago - valorTotal

print(f"O valor total do pedido é R$ {valorTotal:.2f}. Seu troco é R$ {troco:.2f}.")
