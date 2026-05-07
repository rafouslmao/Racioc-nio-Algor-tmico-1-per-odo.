numeros = [5,7,12,2,9,21]
numeros[1] = 17
numeros[3] = 22
print(numeros)
print("=============")
# print(numeros[0])
# print(numeros[1])
# print(numeros[2])
# print(numeros[3])
# print(numeros[4])
# print(numeros[5])
numeros[2] = 1
numeros[4] = 29
print(numeros)
print("=============")
# print(numeros[0])
# print(numeros[1])
# print(numeros[2])
# print(numeros[3])
# print(numeros[4])
# print(numeros[5])

soma = numeros[5] + numeros[4]
sub = numeros[3] - numeros[1]
mult = numeros[0] * numeros[5]
div = numeros[3] / numeros[2]
print(soma)
print(sub)
print(mult)
print(div)
print("=============")
indice = 0

while indice < 6:
    print(numeros[indice] * 2)
    indice+=1
print("=============")   
i = 0 
while i < len(numeros):
    print(numeros[i])
    i+=1
print("=============")
for i in range(len(numeros)):
    print(numeros[i])
print("=============")
for numero in numeros:
    print(numero)



numero = input("Digite um numero: ")

while not numero.isdigit():
    numero = input("Digite um numero: ")
print(type(numero))
numero = int(numero)
print(type(numero))