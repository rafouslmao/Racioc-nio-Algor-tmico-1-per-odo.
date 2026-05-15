vetor = [0]*10

for i in range(10):
    vetor[i] = float(input("Digite um numero: "))

maior = vetor[0]
menor = vetor[0]
for j in range(10):
    if maior < vetor[j]:
        maior = vetor[j]
    if menor > vetor[j]:
        menor = vetor[j]
print(menor,maior)
