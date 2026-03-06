nota1bi = float(input("Digite a nota do 1º bimestre: "))
while nota1bi < 0 or nota1bi > 10:
    print("Nota inválida! Digite uma nota entre 0 e 10.")
    nota1bi = float(input("Digite a nota do 1º bimestre: "))

nota2bi = float(input("Digite a nota do 2º bimestre: "))
while nota2bi < 0 or nota2bi > 10:
    print("Nota inválida! Digite uma nota entre 0 e 10.")
    nota2bi = float(input("Digite a nota do 2º bimestre: "))


nota3bi = float(input("Digite a nota do 3º bimestre: "))
while nota3bi < 0 or nota3bi > 10:
    print("Nota inválida! Digite uma nota entre 0 e 10.")
    nota3bi = float(input("Digite a nota do 3º bimestre: "))

nota4bi = float(input("Digite a nota do 4º bimestre: "))
while nota4bi < 0 or nota4bi > 10:
    print("Nota inválida! Digite uma nota entre 0 e 10.")
    nota4bi = float(input("Digite a nota do 4º bimestre: "))

mediaAnual = (nota1bi + nota2bi + nota3bi + nota4bi) / 4
print(f"A média anual do aluno é: {mediaAnual:.1f}")
