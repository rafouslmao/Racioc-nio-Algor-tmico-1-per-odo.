# idade = int(input("Digite a sua idade : "))
# idade_meses = idade * 12
# print(f"A idade em meses é: {idade_meses} meses")


## Isso serviria para calcular apenas a idade padrao em anos, sem contar os meses. Se for para contar os meses o código seria assim.

## Vou precisar pegar coisa de bibliotecas que eu sei que ainda não vimos, mas eu ja tenho um pouco de experiencia usando bibliotecas(bem pouco mesmo). 

from datetime import date
import sys

def calcular_idade_em_meses(aniversario):
## aniversario é um parametro que essencialmente dentro da função é igual o dataNascimento
## então quando for chamaddo o calcular_idade_em_meses, o aniversario pega a informacao do dataNascimento e entende como aniversario = date(2008, 04, 04)
## dai o idade = hoje.year - aniversario.year; é lido como: idade = 2026 - 2008
 hoje = date.today()
 idade = hoje.year - aniversario.year - ((hoje.month, hoje.day) < (aniversario.month, aniversario.day))
 return idade

def get_valid_date_input():
    while True:
        date_str = input("Digite sua data de nascimento (dd/mm/aaaa ou ddmmaaaa): ")
        try:
           if "/" in date_str:
                day, month, year = map(int, date_str.split('/'))
        ## caso o usuario digite a data no formato com as barras, ele entende e separa a data usando o split.   
           else:
                day = int(date_str[0:2])
                month = int(date_str[2:4])
                year = int(date_str[4:8])
        ## caso o usuario digite a data no formato sem as barras, ele entende e separa a data os pontos sao pra indicar a posição de cada parte que ele precisa tirar, como começa do 0, o dia fica como 0:2, o mes como 2:4 e o ano como 4:8
        ## a separação funciona como 0 inicio e 2 fim então ele so pega o 0 e 1. Por isso que no mês ele comeca pedindo o 2.
           return date(year, month, day)
        ## esse return date é invertido porque assim que a biblioteca datetime entende a data.
        except ValueError:
            print("Data inválida! Por favor, tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            sys.exit(1)
dataNascimento = get_valid_date_input()
idadeMeses = calcular_idade_em_meses(dataNascimento) * 12
print(f"Sua idade em meses é: {idadeMeses} meses")            

