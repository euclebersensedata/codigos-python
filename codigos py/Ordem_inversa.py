
lista=[]
x=1
i=1
while x!=0:
    print("Entre com o elemento",i,"da lista")
    x=int(input())
    lista.append(x)
    i=i+1
tam=len(lista)-1
while tam>0:
    print(lista[tam-1])
    tam=tam-1
