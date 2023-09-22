vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))

def saldoFinal():
    saldoTotal = vitorias - derrotas
    return saldoTotal

saldo = saldoFinal()

if (saldo < 10):
    nivel = "Ferro"

elif (saldo >= 11) and (saldo <= 20):
    nivel = "Bronze"

elif (saldo >= 21) and (saldo <= 50):
    nivel = "Prata"

elif (saldo >= 51) and (saldo <= 80):
    nivel = "Ouro"

elif (saldo >= 81) and (saldo <= 90):
    nivel = "Diamante"

elif (saldo >= 91) and (saldo <= 100):
    nivel = "Lendário"

elif (saldo >= 101):
    nivel = "Imortal"


print(f"O herói possui {saldo} pontos e está no nível {nivel}" )
