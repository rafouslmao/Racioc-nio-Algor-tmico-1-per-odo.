inicial = int(input("Digite o numero inicial: "))
final = int(input("Digite o numero final: "))

for i in range(inicial,final+1):
    print(f"Tabuada do {i}: ")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print(i)