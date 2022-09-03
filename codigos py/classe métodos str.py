class Carro:
    def __init__(self, modelo, ano, cor, velmax):
        self.modelo=modelo
        self.ano=ano
        self.cor=cor
        self.velmax=velmax
    def imprima_carro(self):
        if self.vel==0:
            print("%s %s %d"%(self.modelo, self.cor, self.ano))
        elif self.vel<self.velmax:
            print("%s %s indo a  %d km/h"%(self.modelo, self.cor, self.vel))
        else:
            print("%s %s indo muito rápido"%(self.modelo, self.cor))
    def acelere(self,v):
        self.vel=v
        if self.vel>self.velmax:
            self.vel=self.velmax
        self.imprima_carro()
    def pare(self):
        self.vel=0
        self.imprima_carro()
