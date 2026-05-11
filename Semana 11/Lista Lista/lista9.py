import random

alfabeto = list("abcdefghijklmnopqrstuvwxyz")
embaralhado = alfabeto.copy()
random.shuffle(embaralhado)

letra = random.choice(alfabeto)
escolha = int(input(f"Em qual posicao(0-25) esta a letra {letra}? "))

if embaralhado[escolha] == letra:
    print("Voce acertou!")
else:
    print(f"Voce errou!\nA letra {letra} estava na posicao {embaralhado.index(letra)}")