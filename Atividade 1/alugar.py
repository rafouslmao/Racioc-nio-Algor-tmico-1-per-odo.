qntdCarro = int(input("Quantos carros você deseja alugar? "))
valorCarro = float(100.00)
valorTotal = qntdCarro * valorCarro

print(f"O valor total do aluguel é de R${valorTotal:.2f}")

## Pode utilizar tanto o float tanto o int, para esse caso é até melhor usar o int, seria diferente se o valor do carro fosse R$124,90. 
## O .2f no valor total não é útil nesse caso, porque ele arredonda as casas decimais e encurta a resposta do código, numa conta financeira não será utilizado mas é legal manter para fixar melhor o que essa função faz.
