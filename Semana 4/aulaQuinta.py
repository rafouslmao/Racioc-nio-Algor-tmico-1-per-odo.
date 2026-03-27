# contador = 0
# while contador < 3:
#     print("Olá")
#     contador = contador + 1


# contador = 3
# while contador > 0:
#     print("Olá")
#     contador -= 1

# for i in range (11):
#     print(i)
# print(" \n \n ")

# for e in range (10, -1, -1): 
#     print(e)

# for o in range (1,11):
#     print(num * o)
# print("\n \n")

num = int(input("Digite um número de 1-10: "))
while num < 0 or num > 10:
    print("Número inválido, tente novamente.")
    num = int(input("Digite um número: "))

a = 1
while a <= 10:
    print(a)
    a += 1
print("\n \n")

b = 10
while b >= 0:
    print(b)
    b -= 1
print("\n \n")

c = 1
while c <= 10:
    print(num * c)
    c += 1


palavra = input("Digite uma palavra que tem no minimo 3 letras e no maximo 10: ")
letMin = 3
letMax = 10
while len(palavra) < letMin or len(palavra) > letMax: 
    print("Palavra invaida.")
    palavra = input("Digite uma palavra que tem no minimo 3 letras e no maximo 10: ")
else: 
    print(palavra,"\n",len(palavra))
