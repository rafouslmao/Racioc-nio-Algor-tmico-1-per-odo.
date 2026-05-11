vetores = [0] * 10
pares=0
for i in range(10):
    vetores[i] = int(input("Digite um numero: "))
    if vetores[i] % 2 ==0:
        pares += 1
print(f"O conjunto teve {pares} valores pares.")