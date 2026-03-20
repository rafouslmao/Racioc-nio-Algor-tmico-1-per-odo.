a, b, c = map(float, input("Digite os lados do triângulo: ").split(','))
## print(a,b,c)
# if a + b > c and a + c > b and b + c > a:
#     pass
# else:
#     print("Os valores fornecidos não formam um triângulo.")
## tentei isso antes mas nao deu certo, perguntar depois pq q nao funcionou e como que faco funcionar.
while not (a + b > c and a + c > b and b + c > a):
    print("Os valores fornecidos não formam um triângulo.")
    a, b, c = map(float, input("Digite os lados do triângulo: ").split(','))

if a == b == c:
    print("Triângulo equilátero.")
elif a == b or a == c or b == c:
    print("Triângulo isósceles.")
else:
    print("Triângulo escaleno.")


## o pass eh so pro codigo passar sem dar erro, pq se o if ficar sem nada dentro ele da erro.
## o map eh para colocar diversos valores/variavel em uma unica linha. e o split determina qual valor vai pra cada variavel splitando a virgula.
