tabuleiro = [" "] * 9
jogador = "X"
vencedor = None
turno = 0

combinacoes = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

while turno < 9 and not vencedor:
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

    pos = int(input(f"Jogador {jogador}, escolha uma posição (0-8): "))

    if tabuleiro[pos] != " ":
        print("Posição ocupada! Tente novamente.")
        continue

    tabuleiro[pos] = jogador
    turno += 1

    for combo in combinacoes:
        if tabuleiro[combo[0]] == tabuleiro[combo[1]] == tabuleiro[combo[2]] != " ":
            vencedor = tabuleiro[combo[0]]

    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"
print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
print("--+---+--")
print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
print("--+---+--")
print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

if vencedor:
    print(f"Jogador {vencedor} venceu!")
else:
    print("Empate!")