pessoa = list(map(int, input("Digite 5 valores separados por uma virgula: ").split(",")))
listaOrden = sorted(pessoa)
listaDecres = sorted(pessoa, reverse=True)

print(f"{pessoa},\n{listaOrden},\n{listaDecres}")
print(len(pessoa))
print(min(pessoa))
print(max(pessoa))
print(sum(pessoa))
