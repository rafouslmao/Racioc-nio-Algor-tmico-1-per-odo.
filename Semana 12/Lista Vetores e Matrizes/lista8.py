vetor = [0]*6
for i in range(6):
    vetor[i] = int(input("Digite um numero: "))
x = 5
for i in range(6):
    while x>-1:
        vetor[i] = vetor[x]
        x-=1
        

print(vetor)