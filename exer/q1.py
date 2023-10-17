from random import randint

#Desenvolva um programa para ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
# o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor
# o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor


Q=[]

for numero in range (20):
    Q.append(randint(a=1, b=100))

print(Q)    

#Variavel de Controle

maior= -1
menor = float('inf')

for i in Q:
    if maior < i :
        maior= i

    if menor > i :
        menor= i



print(f"O maior valor é :{maior} e sua posição é {Q.index(max(Q))}")
print(f"O menor valor é :{menor} e sua posição é {Q.index(min(Q))}")
