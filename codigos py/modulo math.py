import math

def éhipotenusa(x):
    b=x-1
    condição=False
    while b>0 and not condição:
        if (math.sqrt(x**2-b**2))%int((math.sqrt(x**2-b**2)))==0:
            condição=True
        b=b-1
    return condição



n=int(input())
soma=0
while n>0:
    if éhipotenusa(n):
        soma=soma+n
    n=n-1
print(soma)
