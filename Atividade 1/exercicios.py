ano = float(input("Digite seu ano de nascimento: "))
idade = 2026 - (ano)
print(f"Sua idade é {idade} anos")

from datetime import date
import sys 

anoNascimento = int(input("Qual seu ano de nascimento? "))
def calcular_idade(ano_nascimento):
    data_atual = date.today()
    ano_atual = data_atual.year
    idade = ano_atual - ano_nascimento
    return idade
