lista = [1,2,3]
matriz =[
    [1,2],
    [3,4]
]

matriz2=[[1,2],[3,4]]
# Pode ser dos dois jeitos. Melhor o primeiro por organizacao.

matriz3 = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

matriz3 [0] [2] = 2
matriz3 [2] [0] = 7
matriz3 [3] [3] = 8
#=================
lista2 = [9,8,7,6]
for indice in range(4):
    print(lista2[indice])

#=================
print("\n")
matriz4 = [
    [9,8],
    [7,6]
]
for linha in range(2):
    for coluna in range(2):
        print(matriz4[linha][coluna])
print("\n")
for linha in range(2):
    print(matriz4[linha])

