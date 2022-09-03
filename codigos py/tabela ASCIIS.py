def maiusculas(frase):
    string=''
    i=0
    while i < len(frase):
        if ord(frase[i])>=65 and ord(frase[i])<=90:
            string+=frase[i]
        i+=1
    return string
