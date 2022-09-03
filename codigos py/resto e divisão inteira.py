seg=input("Entre com o numero de segundos ")

s=float(seg)

h=s//3600
s=s%3600
m=s//60
s=s%60

print("É equivalente a ",h," horas; ",m," minutos; ",s," segundos.")
