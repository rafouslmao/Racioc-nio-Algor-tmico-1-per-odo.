matriz = [
    [1,9.8,5.5,0],
    [2,3.5,6.8,0],
    [3,8.7,9.5,0],
    [4,2.3,10,0],
    [5,7.6,4.5,0]
]
matriz[0][3] =(matriz[0][1] + matriz[0][2])/2
matriz[1][3] =(matriz[1][1] + matriz[1][2])/2
matriz[2][3] =(matriz[2][1] + matriz[2][2])/2
matriz[3][3] =(matriz[3][1] + matriz[3][2])/2
matriz[4][3] =(matriz[4][1] + matriz[4][2])/2

maior = matriz[0][0]
indice = matriz[0][0]
for linha in range(5):
    while maior < matriz[linha][3]:
        maior = matriz[linha][3]
        indice = matriz[linha][0]
print(indice)