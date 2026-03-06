peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em m: "))    

imc = peso / (altura**2)
formattedValue = "{:.2f}".format(imc)

## elif serve como se fosse um "se" e o else serve como um "caso contrário", ou seja, se nenhuma das condições anteriores for verdadeira, o código do else será executado.
## para conversão em string, podemos usar o str() ou o f (format) para formatar a string, assim não precisamos converter o ano para string, e o código fica mais limpo.

if imc < 18.5:
    print("Você está abaixo do peso, pois seu imc é "+str(formattedValue))
elif imc >= 18.5 and imc < 25:
        print("O seu peso é normal, pois seu imc é "+str(formattedValue))    
elif imc >= 25 and imc < 30:
        print("Você é sobrepeso, pois seu imc é "+str(formattedValue))  
elif imc >= 30 and imc < 35:
       print("Você tem obesidade grau 1, pois seu imc é "+str(formattedValue))
elif imc >= 35 and imc <40 :
       print("Você tem obesidade grau 2, pois seu imc é "+str(formattedValue))
else:
         print("Você tem obesidade grau 3, pois seu imc é "+str(formattedValue))

## ctrl + / para comentar ou descomentar uma linha de código.

print(f"O seu IMC é {formattedValue}")
