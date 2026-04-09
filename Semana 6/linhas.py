linha = int(input("Digite o numero correspondente para a quantidade de linhas que voce quer: "))

for i in range(1, linha + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()