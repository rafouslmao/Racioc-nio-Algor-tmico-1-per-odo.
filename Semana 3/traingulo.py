a, b, c = map(float, input("Digite os lados do triângulo: ").split(','))
## print(a,b,c)
if a + b > c and a + c > b and b + c > a:
    pass
if a == b == c:
    print("Triângulo equilátero.")
elif a == b or a == c or b == c:
    print("Triângulo isósceles.")
else: 
    print("Triângulo escaleno.")

## o pass eh so pro codigo passar sem dar erro, pq se o if ficar sem nada dentro ele da erro.
## o map eh para colocar diversos valores/variavel em uma unica linha. e o split determina qual valor vai pra cada variavel splitando a virgula.
