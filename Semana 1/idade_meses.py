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
 hoje = date.today()
 anos = (hoje.year - aniversario.year)
 meses = (hoje.month - aniversario.month)
 idadeMeses = anos * 12 + meses
 return idadeMeses
 if hoje.day < aniversario.day:
    idadeMeses -= 1
## anos eh usado pra pegar o ano atual e subtrair pelo ano que foi inseritdo e meses faz a mesma coisa, mas com o mes. 
## Dai ele multiplica o resultado de anos por 12 e soma com o resultado de meses.

def get_valid_date_input():
    while True:
        dateStr = input("Digite sua data de nascimento (dd/mm/aaaa ou ddmmaaaa): ")
        try:
           if "/" in dateStr:
                day, month, year = map(int, dateStr.split('/'))
        ## caso o usuario digite a data no formato com as barras, ele entende e separa a data usando o split.   
           else:
                day = int(dateStr[0:2])
                month = int(dateStr[2:4])
                year = int(dateStr[4:8])
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
idadeCerta = calcular_idade_em_meses(dataNascimento)
print(f"Sua idade em meses é: {idadeCerta} meses")    


## OUTRA FORMA DE FAZER SEM IMPORTAR BIBLIOTECA
# idade = str(input("Qual sua data de nascimento em mmyyyy? "))
# anoAtual = 2026
# mes = int(input("Qual o mes atual? "))
# calcMes = (int(idade[0:2]) - mes)
# idadeMeses = (anoAtual - int(idade[2:6])) * 12 + calcMes
# print(f"Sua idade em meses é: {idadeMeses} meses")





