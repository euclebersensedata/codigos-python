def remove_repetidos(lista):
    tam=len(lista)-1
    i=0
    lista2=[lista[0]]
    del lista[0]
    while i<tam:
        if not (lista[i] in lista2):
            lista2.append(lista[i])
        i=i+1
        
    tam2=len(lista2)
    lista3=[]
    while tam2>0:
        k=0
        aux=lista2[0]
        while k<tam2:
            
            if aux>lista2[k]:
                aux=lista2[k]
            k=k+1
        l=0
        while aux in lista2:
            if lista2[l]==aux:
                del lista2[l]
            l=l+1
        tam2=tam2-1
        lista3.append(aux)
    return lista3
            
n=int(input("Entre com o número de elementos da lista: "))
aux=n
lista=[]
while n>0:
    print("Entre com o elemento",aux-n+1,"da lista")
    x=int(input())
    lista.append(x)
    n=n-1

lista2=remove_repetidos(lista)
print(lista2)
    
