class Triangulo:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimetro(self):
        self.perimetro=self.a+self.b+self.c
        return self.perimetro
    def tipo_lado(self):
        if self.a==self.b and self.a==self.c:
            return 'equilátero'
        elif self.a!=self.b and self.c!=self.a:
            return 'escaleno'
        else:
            return 'isósceles'
    def retangulo(self):
        if self.a!=self.b and self.c!=self.a:
            if self.a>self.b and self.a>self.c:
                h=self.a
                c1=self.b
                c2=self.c
            elif self.b>self.a and self.b>self.c:
                    h=self.b
                    c1=self.a
                    c2=self.c
            else:
                    h=self.c
                    c1=self.a
                    c2=self.b
        else:
            return False
        if (h**2==c1**2+c2**2):
            return True
        else:
            return False
    def semelhantes(self,t2):
        a=self.a
        b=self.b
        c=self.c
        x=t2.a
        y=t2.b
        z=t2.c
        if (a>=b)and(b>=c):
            aux1=a
            aux2=b
            aux3=c
        elif (a>=c)and(c>=b):
            aux1=a
            aux2=c
            aux3=b
        elif (b>=a)and(a>=c):
            aux1=b
            aux2=a
            aux3=c
        elif (b>=c)and(c>=a):
            aux1=b
            aux2=c
            aux3=a
        elif (c>=a)and(a>=b):
            aux1=c
            aux2=a
            aux3=b
        elif (c>=b)and(b>=a):
            aux1=c
            aux2=b
            aux3=a
        if (x>=y)and(y>=z):
            auxp1=x
            auxp2=y
            auxp3=z
        elif (x>=z)and(z>=y):
            auxp1=x
            auxp2=z
            auxp3=y
        elif (y>=z)and(z>=x):
            auxp1=y
            auxp2=z
            auxp3=x
        elif (y>=x)and(x>=z):
            auxp1=y
            auxp2=x
            auxp3=z
        elif (z>=x)and(x>=y):
            auxp1=z
            auxp2=x
            auxp3=y
        elif (z>=y)and(y>=x):
            auxp1=z
            auxp2=y
            auxp3=x
        if (aux1/auxp1==aux2/auxp2)and(aux1/auxp1==aux3/auxp3):
            return True
        else:
            return False
