numeros = list(map(int, input("Digite 10 números separados por vírgula: ").split(",")))
par = 0
impar = 0
contador = 0

while contador < 10:
    if numeros[contador] % 2 == 0:
        par += 1
    else:
        impar += 1
    contador += 1

print(f"A quantidade de números pares é {par} e a quantidade de números ímpares é {impar}")
## o numeros[contador] checka o indice da lista, q vai de 0 a 9, e dai ve se ele eh par ou impar, ta ali com menor que 10 pra quando chegar no 10 ele quebrar o loop.
