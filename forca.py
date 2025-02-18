
print("Bem vindo ao jogo da forca!")

palavra_secreta = "Detroit".upper()
letras_acertadas = ("_" for letra in palavra_secreta)

print(letras_acertadas)

enforcou = False
acertou = False
erros = 0

while not enforcou and not acertou:

    chute = input("Digite uma letra")
    chute = chute.strip().upper()

    if chute in palavra_secreta:
        index = 0

        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index]= letra
            index += 1
            if "_" not in letras_acertadas:
                acertou = True
                print("Você ganhou!") 

       


    else:
        print("Você tem", erros, "erros")
        erros +=1

    print(letras_acertadas)