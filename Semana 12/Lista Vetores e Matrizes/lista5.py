vetor = [0]*10
par = 0
for i in range(10):
    vetor[i] = int(input("Digite um numero: "))
    if vetor[i] % 2 == 0:
        par +=1
print(par)