nota = float(input("Qual foi a nota do aluno? \n"))

while nota < 0 or nota > 10:
    print("Nota inválida.")
    nota = float(input("Qual foi a nota do aluno? \n"))


print(f"A nota do aluno foi {nota}.")