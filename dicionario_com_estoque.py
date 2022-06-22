x = int(input("Digite x: "))
y = int(input("Digite y: "))

estoque_toner_preto = {"laserjet: E55040, MPF E57540": [1, 292.48],
                       "laserjet: E40040, MPF E42540": [1, 383.43]}

saida = [["laserjet: E55040, MPF E57540", x],["laserjet: E40040, MPF E42540", y]]
total = 0

print("Saída:/n")
for operação in saida:
    produto, quantidade = operação
    valor = estoque_toner_preto[produto][1]
    baixa = valor*quantidade
    print(f"{produto:12s}: {quantidade:3d} x {valor:6.2f} = {baixa:6.2f}")
    estoque_toner_preto[produto][0] -= quantidade
    total += baixa
print(f" Baixa total: {total:21.2f}\n")

