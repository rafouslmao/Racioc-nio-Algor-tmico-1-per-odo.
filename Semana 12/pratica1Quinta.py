matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz)
print("\n")


for indice in range(3):
    print(matriz[indice])

    
print("\n")


for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna])


for linha in matriz:
    print(linha)

