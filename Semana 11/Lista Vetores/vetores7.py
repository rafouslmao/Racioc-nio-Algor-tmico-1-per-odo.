vetores = [0] * 10

for i in range(10):
    vetores[i] = int(input("Digite um numero: "))
maior = vetores[0]
pos = 0

for i in range(10):
    if vetores[i] > maior:
        maior = vetores[i]
        pos=i
print(f"Vetor: {vetores}\nMaior: {maior}\nIndice do maior: {pos}")