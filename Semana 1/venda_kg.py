precoMaca = 10.99
precoPera = 8.99
kgMaca = float(input("Quantos kilos de maçã você deseja comprar? "))
kgPera = float(input("Quantos kilos de pera você deseja comprar? "))

totalMaca = kgMaca * precoMaca
totalPera = kgPera * precoPera
totalCompra = totalMaca + totalPera
print(f"O total da compra é: R${totalCompra:.2f}")

## é possível utilizar números "quebrados" como 0.302 ou 1.04 kgs que ainda daria o resultado certinho.
