escolha = input("Você está em uma floresta, e encontrou dois caminhos, um para a direita e um para a esquerda. \n Para qual caminho você deseja seguir? (d/e) \n")

if escolha == "d":
    escolhaD = input("Você se deparou com uma montanha. Você deseja subir ela ou voltar para a floresta? (s/n) \n").lower()
    if escolhaD == "s": 
        print("Você encontrou um tesouro, parabéns!")
    else: 
        print("Você escolhe voltar e se perde dentro da floresta.")
if escolha == "e":
    escolhaE = input("Você encontrou um rio! Você deseja atravessar ele ou voltar para a floresta? (s/n) \n").lower()
    if escolhaE == "s":
        print("Você atravessa e chega seguramente em uma vila! Aproveite!")
    else:
        print("Você escolhe voltar e se perde dentro da floresta.")

