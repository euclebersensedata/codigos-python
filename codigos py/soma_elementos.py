def soma_elementos(lista):
    tam=len(lista)
    soma=0
    while tam>0:
        soma=soma+lista[tam-1]
        tam=tam-1
    return soma

n=int(input("Entre com o número de elementos da lista: "))
aux=n
lista=[]
while n>0:
    print("Entre com o elemento",aux-n+1,"da lista")
    x=int(input())
    lista.append(x)
    n=n-1

lista2=soma_elementos(lista)
print(lista2)
    
