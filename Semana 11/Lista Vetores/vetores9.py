vetores = [0] * 10
positivos = 0
negativos = 0 
soma = 0
for i in range(10):
    vetores[i] = float(input("Digite um numero: "))
    if vetores[i] < 0:
        negativos += 1
    if vetores[i] > 0:
        positivos +=1
        soma += vetores[i]
print(f"O conjunto teve {positivos} positivo(s) e {negativos} negativo(s).\nA soma dos numeros positivos foi {soma}")