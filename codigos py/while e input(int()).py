n=int(input("Digite um número inteiro: "))
aux=n
i=0
while (n!=0):
    if (aux%n==0):
        i=i+1
    n=n-1
if (i==2):
    print("primo")
else:
    print("não primo")
