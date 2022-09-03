def bubble_sort(lista):
    fim=len(lista)
    for i in range(fim-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
                print("[",lista[0],",",sep='',end='')
                for k in range(1,len(lista)-1,1):
                    print(" ",lista[k],",",sep='',end='')
                print(" ",lista[len(lista)-1],"]",sep='')
    return lista
