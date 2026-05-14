matriz = [
    [5,6,2,8],
    [35,6,8,23],
    [25,65,98,2],
    [99,56,45,65]
]
maior = matriz[0][0]
indiceL = 0
indiceC = 0
for linha in range(4):
    for coluna in range(4):
        while maior < matriz[linha][coluna]:
            maior = matriz[linha][coluna]
            indiceL = linha
            indiceC = coluna
print(maior, indiceL, indiceC)
