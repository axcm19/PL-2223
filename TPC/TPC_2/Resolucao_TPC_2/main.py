

def main():

    print(" ")
    print("------------------------------ TPC 2 ------------------------------")
    print("Insira texto:")
    print(" ")
    print("  = --> Devolve o valor da soma total")
    print("  OFF (seja uppercase ou lowercase) --> Interrompe a soma")
    print("  ON (seja uppercase ou lowercase) --> Retoma a soma")
    print("  QUIT (input único em uppercase) --> Fecha o programa")
    print("-------------------------------------------------------------------")
    print(" ")

    texto = input()
    soma = 0
    estado = 1 # 1 -> on, 0 -> off

    while True:

        if texto == "QUIT":
            break

        for carater in texto:
            lowercase = carater.lower()

            if carater.isdigit() and estado == 1:
                soma += int(carater)


            if carater == "=" and estado == 1:
                print(f"Soma total = {soma}")

            #-------------------------------------------------------------------------------------------------
            # caso seja off

            if lowercase == "o" and texto[+1].lower() == "f" and texto[+1].lower() == "f":
                estado = 0

            if lowercase == "f" and texto[-1].lower() == "o" and texto[+1].lower() == "f":
                estado = 0

            if lowercase == "f" and texto[-1].lower() == "o" and texto[+1].lower() == "f":
                estado = 0

            # -------------------------------------------------------------------------------------------------
            # caso seja on

            if lowercase == "o" and texto[+1].lower() == "n":
                estado = 1

            if lowercase == "n" and texto[-1].lower() == "o":
                estado = 1

        texto = input()







if __name__ == "__main__":
    main()
