
contador = 0
soma = 0

while True:
    num = float(input("Digite um número. Para encerrar o ciclo digite -1: "))
    if num == -1:
        if contador == 0:
            print("Nenhum número foi digitado")
        else:
            media = soma / contador
            print(f"A média dos números digitados foi: {media}")
    else:
        soma += num
        contador += 1