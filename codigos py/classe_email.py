#Estudo de classes

class Email():
    def __init__(self, dominio, empresa, usuario) -> None:
        self.dominio = dominio
        lista_empresas = ("Sensedata","Zenvia")
        if empresa in lista_empresas:
            self.empresa = empresa
        else:
            raise Exception("Não trabalhamos nessa empresa!")
        self.usuario = usuario        
        self.endereco = self.usuario + '@' + self.dominio
        pass

    def enviar_email(self):
        assunto = input("Assunto: ")
        with open(f"{assunto}.txt","w") as arquivo:
            arquivo.write(assunto)
        print()
        destinatario = input("Destinatario: ")
        with open(f"{assunto}.txt","a") as arquivo:
            arquivo.write("\n" + destinatario)
        print()
        mensagem = input("Mensagem: ")
        with open(f"{assunto}.txt","a") as arquivo:
            arquivo.write("\n" + mensagem)
#Estrutura do with: with open(nome_do_arquivo, objetivo_de_abrir_ele - r,w) as arquivo
#read: para arquivos simples
#readlines: cria uma lista que cada linha é um elemento da lista
#encoding="utf-8": corrige o problema de caracteres especiais



meu_email = Email("sensedata.com.br", "Sensedata", "eucleber.junior")
Email.enviar_email(meu_email)
