multiplo = 0

for i in range(0,101,3):          
        if i == 0:
            continue
        if i % 5 ==0:
            continue
        else:
            multiplo +=1
            print(i)

       
print(f"O numero de multiplos de 3 que nao sao multiplos de 5 eh {multiplo}")