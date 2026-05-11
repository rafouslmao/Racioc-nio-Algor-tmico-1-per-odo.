lista = ["Rafael","Artur","Joao","Ana","Uva"]

maior = lista[0]
menor = lista[0]

for palavra in lista:
    if len(palavra) > len(maior):
        maior = palavra
    if len(palavra) < len(menor):
        menor = palavra
print(menor,maior)