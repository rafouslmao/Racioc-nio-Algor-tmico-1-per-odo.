while True:
    op = int(input("Qual operador você deseja? Digite o número correspondente ao operador. \n 1. Soma \n 2. Subtração \n 3. Multiplicação \n 4. Divisão \n 0. Sair \n "))
    if op == 0:
        break
    num1 = int(input("Qual o primeiro número da sua operação? "))
    num2 = int(input("Qual o segundo número da sua operação? "))
    resultado = None

    if op == 1:
        resultado = num1 + num2
        print(resultado)
    elif op == 2:
        resultado = num1 - num2
        print(resultado)
    elif op == 3:
        resultado = num1 * num2
        print(resultado)
    elif op == 4:
        resultado = num1 / num2
        print(resultado)