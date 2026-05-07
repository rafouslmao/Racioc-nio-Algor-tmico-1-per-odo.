import random 
numerosMega =[54,random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60)]
numerosApost = [0,0,0,0,0,0]
i = 0 
while i<6:
    num1 = int(input("Digite um numero: "))   
    while num1 < 1 or num1>60: 
        print("Numero Invalido")
        num1 = int(input("Digite um numero: "))   
    numerosApost[i]=num1
    i+=1
acertos = 0
indice=0
j=0

while indice<7:
    while j < 6:    
        if numerosMega == numerosApost[j]:
            acertos+=1
        j+=1
    indice+=1


print(f"Os numeros da mega foram: {numerosMega}")
print(f"os numeros apostados foram: {numerosApost}")
print(f"O numero de acertos foi: {acertos}")

