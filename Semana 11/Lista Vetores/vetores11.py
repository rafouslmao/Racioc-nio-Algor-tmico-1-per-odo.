vetores = [0] * 5

for i in range(5):
    vetores[i] = int(input("Digite um numero: "))
maior = vetores[0]
menor = vetores[0]
posMa = 0
posMe = 0
for i in range(5):
    if vetores[i] > maior:
        maior = vetores[i]
        posMa=i
for i in range(5):
    if vetores[i] < menor:
        menor = vetores[i]
        posMe=i
print(f"A posicao do maior, de acordo com o indice, foi: {posMa}\nA posicao do menor, de acordo com o indice, foi: {posMe}")