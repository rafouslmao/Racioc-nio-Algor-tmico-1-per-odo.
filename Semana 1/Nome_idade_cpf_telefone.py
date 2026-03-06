nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")

## Isso aqui é caso o usuário digite um algo que nao seja um ano válido para o ano de nascimento. Teria como fazer o mesmo para o cpf e telefone, mas não sei se é o que você quer que a gente faça, então vou deixar so o ano de nascimento mesmo.
while True:
    try: 
     anoNascimento = int(input("Digite seu ano de nascimento: "))
     if anoNascimento < 1900 or anoNascimento > 2026:
       print("Ano de nascimento inválido! Digite um ano entre 1900 e 2026.")
     else:
       break
    except ValueError:
     print("Ano de nascimento inválido! Digite apenas números.")
telefone = input("Digite seu telefone: ")

## Por ano ser int, temos que converter ele para string para concatenar com as outras variáveis, caso contrário, teríamos um erro.
print("Olá, " + nome + "!" + "\n" + "Seu CPF é " + cpf + "." + "\n" + "Seu ano de nascimento é " + str(anoNascimento) + "\n" + "Seu telefone é " + telefone + "." + "\n" + "Seja bem-vindo a PUCPR! ")

##Inves de transformar Ano pra string, podemos usar o f (format) para formatar a string, assim não precisamos converter o ano para string, e o código fica mais limpo.
#print((f"Ano: {anoNascimento}"))



