lista = []
lista2 = list()
#============================================
lista3 = [1,2,3]
lista3.insert(0,5)
#============================================
lista4 = [1,2,3]
lista4.append(5)
#============================================
# lista5 = [1,2,3]
# lista5.extend(5,6)
#============================================
lista6 = [1,2,3]
lista6.remove(2)
# remove o NUMERO/VALOR 2, nao o indice
#============================================
lista7 = [1,2,3]
lista7.pop()
#============================================
lista8 = [1,2,3]
lista8.pop(0)
#============================================
lista9 = [1,2,3]
lista9.index(2)
# retorna o indice o valor 2
#============================================
lista10 = [1,2,2]
lista10.count(2)
#============================================
lista11 = [2,3,1]
lista11.sort()
#============================================
lista12 = [1,2,3]
lista12.reverse()
# retorna a lista inversa
#============================================
lista13 = [1,2,3]
len(lista13) #Retorna o tamanho da lista
min(lista13) #Retorna o menor valor da lista
max(lista13) #Retorna o maior valor da lista
sum(lista13) #Retorna a soma dos valores da lista
sorted(lista13) #Retorna a lista ordenada
sorted(lista13, reverse=True) #Retorna a lista ordenada (decrescente)
list(reversed(lista13)) #Retorna a lista na ordem inversa
#============================================
print(lista13)