'''filme=[{'título':'Star Wars',
        'ano':1977,
        'diretor':'George Lucas'},
        {'título':'Avengers',
        'ano':2020,
        'diretor':'Irmãos Russo'}]
for k in filme.keys():
    print('Chave ' + str(k))  
for v in filme.values():
    print('Valor ' + str(v))
for k, v in filme.items():
    print('O '+ str(k) +' é ' + str(v))'''
#para printar o valor da chave com a chave (use "" - aspas duplas):
#print(filme[1]["título"])
#para declarar uma nova chave no dicionário, basta escrever o nome da chave e o 
#valor que será adicionada à direita
#filme[0]['duração']=90
#print(filme[0])
#print(filme[1])

estado={}
brasil=[]
for c in range(0,3):
    estado['Estado']=str(input('Nome do estado: '))
    estado['Sigla']=str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in range(brasil):
    for k,v in e.items():
        print('O ' + str(k) + ' é ' + str(v),end=' ')
    print()
