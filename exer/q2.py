from random import randint
lista = []
soma = 0
for n in range(20):
    lista.append(randint(a=1, b=40))

for i in lista:
    if(i % 2) == 0:
        soma += 1



print(f'O resultado da soma é :  {soma}')
print(lista)
