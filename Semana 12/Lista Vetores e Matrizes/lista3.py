conj = [0]*10
quad = [0]*10

for i in range(10):
    conj[i] = float(input("Digite um numero: "))
for j in range(10):
    quad[j] = conj[j] **2
print(quad)