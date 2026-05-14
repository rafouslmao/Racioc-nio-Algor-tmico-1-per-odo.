matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matriz[0][0] = 20
matriz[1][2]=15
matriz[2][1]=19

print(matriz)
print("\n")

for indice in range(3):
    print(matriz[indice])
print("\n")

for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna])
print("\n")

soma = matriz[0][0] + matriz[1][0]
sub = matriz[2][2] - matriz[2][1]
mult = matriz[0][1] * matriz[2][0]
div = matriz[1][2] / matriz[0][2]
print(soma,sub,mult,div)