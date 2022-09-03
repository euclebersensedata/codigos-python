#Estudo de classes

class Email():
    def __init__(self, dominio, empresa, usuario) -> None:
        self.dominio = dominio
        self.empresa = empresa
        self.usuario = usuario        
        self.endereco = self.usuario + '@' + self.dominio
        pass

meu_email = Email("sensedata.com.br", "Sensedata", "eucleber.junior")
print(meu_email.endereco)
