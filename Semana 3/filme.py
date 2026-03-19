idade = int(input("Idade: "))
ingresso = input("Voce tem ingresso? (s/n)").lower()
if ingresso == "s" :
    ingresso = True
else:
    ingresso = False
# if idade >= 18 and ingresso:
#     print("Bom filme!")
# elif idade >= 18 and not ingresso:
#     print("Você precisa comprar um ingresso.")
# elif idade < 18 and ingresso:
#     print("Você não tem idade para assistir esse filme, venha com um adulto")
# else:
#     print("Por que você está aqui? Compre um ingresso e venha com um adulto.")
if idade >= 18:
    if ingresso:
        print("Bom filme!")
    else:
        print("Você não tem um ingresso, por favor compre um.")
else: 
    print("Você não tem idade para assistir esse filme, venha com um adulto.")