user = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if user == "admin" and senha == "1234":
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos. Tente novamente.")

if user == "convidado":
    print("Acesso restrito.")

 