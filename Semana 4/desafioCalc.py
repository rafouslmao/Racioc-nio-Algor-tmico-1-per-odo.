while True:
    exp = input("Digite sua expressão (ou digite sair para encerrar): ")
    if exp == "sair":
        break

    valido = True
    resultado = None

    try: 
        resultado = eval(exp)
    except ZeroDivisionError:
        print("Erro. Divisão por zero.")
        valido = False
    except:
        print("Expressão inválida. Tente novamente")
        valido = False
    
    if valido:
        print(f"O resultado da sua expressão é {resultado}")
## valido = True indica pro codigo se a expressao for valida ou nao
## quando a expressao for valida ele vai printar, ele comeca como True pq o codigo assume que a expressao eh valida ate que algo prove ao contrario, nesse caso a utilizacao de palavras ou divisao por zero
## o try eh bem autoexplicativo, ele pede para o codigo tentar rodar. caso ele de erro e crashe e simplesmente acabe com a run, oque geralmente acontece, o except salva ele de crashar e printa que deu erro e o pq q deu erro, nesse caso ele diz quando teve uma divisao por zero ou se a expressao for invalida.
## o except eh tipo um if, a diferenca eh q o if serve para checar condicoes antes de algo acontecer, ja o except reage depois que um erro acontece.
## o eval em geral pega uma string e executa ela como um codigo no Python, nesse caso ele pega a expressao. 
## seria a mesma coisa que botar uma variavel conta = 8 * 3 / (5*3)
## print (conta)
## ZeroDivisionError eh um codigo/nome especifico do Python que lanca quando vc tenta dividir por zero, que geralmente resulta em um erro.