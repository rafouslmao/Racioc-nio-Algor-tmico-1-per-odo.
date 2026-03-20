a, b, c = map(float, input("Digite os lados do triângulo: ").split(','))
# print(a,b,c)
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
     print("Triângulo equilátero.")
    elif a == b or a == c or b == c:
     print("Triângulo isósceles.")
    else:
     print("Triângulo escaleno.")
else:
    print("Os valores fornecidos não formam um triângulo.")

# while not (a + b > c and a + c > b and b + c > a):
#     print("Os valores fornecidos não formam um triângulo.")
#     a, b, c = map(float, input("Digite os lados do triângulo: ").split(','))

if (a**2)+(b**2) == (c**2):
    print("Triângulo retângulo.")
else:
    print("Não é um triângulo retângulo.")


## o map eh para colocar diversos valores/variavel em uma unica linha. e o split determina qual valor vai pra cada variavel splitando a virgula.
## while not eh pra tipo, enquanto nao for isso aqui printa que o triangulo nao eh valido e pede pra vc digitar de novo.
