
num = int(input("digite um numero: "))
while num <= 0:
    print("numero invalido")
    num = int(input("digite um numero: "))

soma = 0
cont = 1
exp = ""
for i in range(1,num+1):
    soma+=cont
    cont+=1
    if i ==1:
        exp = str(i)
    else:
        exp += f" + {i}"
print(f"{exp} = {soma}")
## exp = "" marca uma string vazia
## so quero pegar o primeiro numero entao o if i ==1: exp = str(i)
## se nao tivesse isso ficaria como +1 +2 +3 
