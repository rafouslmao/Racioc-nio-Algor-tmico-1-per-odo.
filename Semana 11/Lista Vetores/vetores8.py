notas = [0] * 15
soma = 0
for i in range(15):
    notas = int(input(f"Qual a nota do aluno {i+1}? "))
    soma += notas
print(soma)
