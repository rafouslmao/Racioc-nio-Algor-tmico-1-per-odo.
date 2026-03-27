while True:
    exp = input("Digite sua expressão (sair se quiser sair.): ")
    if exp == "sair":
        break

    oper = None
    operIndex = -1
    i = 0
    while i < len(exp):
        if exp[i] in "+-*/":
            op = exp[i]
            opIndex = 1
        i += 1
    

