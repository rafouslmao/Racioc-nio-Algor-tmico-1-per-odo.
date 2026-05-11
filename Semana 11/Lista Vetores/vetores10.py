vetores = [0] * 5
soma = 0
media = 0
for i in range(5):
    vetores[i] = int(input("Digite um numero: "))

maior = vetores[0]
menor = vetores[0]

for i in range(5):
    if vetores[i] > maior:
        maior = vetores[i]
    if vetores[i] < menor:
        menor = vetores[i]
    soma += vetores[i]
media = soma / 5

print(f"O maior numero foi {maior}\nO menor numero foi {menor}\nA media do conjunto foi {media}")