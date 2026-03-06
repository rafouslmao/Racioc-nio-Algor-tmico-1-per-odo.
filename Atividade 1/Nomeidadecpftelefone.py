nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
anoNascimento = int(input("Digite seu ano de nascimento: "))
telefone = input("Digite seu telefone: ")

## Por ano ser int, temos que converter ele para string para concatenar com as outras variáveis, caso contrário, teríamos um erro.
print("Olá, " + nome + "!" + "\n" + "Seu CPF é " + cpf + "." + "\n" + "Seu ano de nascimento é " + str(anoNascimento) + "\n" + "Seu telefone é " + telefone + "." + "\n" + "Seja bem-vindo a PUCPR! ")

##Inves de transformar Ano pra string, podemos usar o f (format) para formatar a string, assim não precisamos converter o ano para string, e o código fica mais limpo.
print((f"Ano: {anoNascimento}"))


