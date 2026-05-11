vetores = [0] * 10

for i in range(10):
    vetores[i] = int(input("Digite um numero: "))

maior = vetores[0]
menor = vetores[0]

for i in range(10):
    if vetores[i] > maior:
        maior = vetores[i]
    if vetores[i] < menor:
        menor = vetores[i]
print(f"Maior: {maior} \nMenor: {menor}")