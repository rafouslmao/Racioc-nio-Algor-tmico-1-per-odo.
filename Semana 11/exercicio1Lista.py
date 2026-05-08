import random
numerosJogador1 = []
numerosJogador2 = []
dado1 = random.randint(1,6)
numerosJogador1.insert(0,dado1)
dado2 = random.randint(1,6)
numerosJogador1.insert(1,dado2)
dado3 = random.randint(1,6)
numerosJogador1.insert(2,dado3)
dado4 = random.randint(1,6)
numerosJogador2.insert(0,dado4)
dado5 = random.randint(1,6)
numerosJogador2.insert(1,dado5)
dado6 = random.randint(1,6)
numerosJogador2.insert(2,dado6)

resultadoJogador1 = sum(numerosJogador1)
resultadoJogador2 = sum(numerosJogador2)
print(f"Dados Jogador 1: {dado1}, {dado2}, {dado3}\nDados Jogador 2: {dado4}, {dado5}, {dado6}\n{resultadoJogador1}\n{resultadoJogador2}")
if resultadoJogador1 > resultadoJogador2:
    print("Jogador 1 venceu")
elif resultadoJogador1 < resultadoJogador2:
    print("Jogador 2 venceu")
else:
    print("Empatou")
