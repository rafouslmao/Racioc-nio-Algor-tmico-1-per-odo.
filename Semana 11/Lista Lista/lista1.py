import random
lista = []

for i in range (10):
    lista.append(random.randint(1,100))
print(lista)

#ou

lista2 = [random.randint(1,100) for i in range(10)]
print(lista2)