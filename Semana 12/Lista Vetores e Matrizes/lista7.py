vetor = [0]*10
for i in range(10):
    vetor[i] = int(input("Digite um numero: "))
indice = 0
maior = vetor[0]
for j in range(10):
    if maior < vetor[j]:
        maior = vetor[j]
        indice = j
print(f"O maior numero eh {maior} e ele se encontra na posicao {indice} de acordo com o indice.")