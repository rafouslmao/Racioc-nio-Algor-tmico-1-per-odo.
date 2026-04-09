# par = 0
# impar = 0
# for i in range(11):
#     if i % 2 == 0:
#         par +=1
#     elif i == 0:
#         continue
#     else:
#         impar+=1
#     print(i)
# print("\n" f"O número de pares é {par} e o número de impares é {impar}" "\n")


# for e in range(10,0,-1):
#     print(e)

## continue vai ignorar o 0 basicamente

# palavra = "Profe"
# for letra in palavra:
#     print(letra)

vogais = ("a","e","i","o","u","A","E","I","O","U")
palavra = input("Digite uma palavra que comece com uma vogal: ")
if palavra.startswith(vogais):
    for letra in palavra:
        print(letra)
else: 
    print("Palavra invalida")
    palavra = input("Digite uma palavra que comece com uma vogal: ")
    for letra in palavra:
        print(letra)