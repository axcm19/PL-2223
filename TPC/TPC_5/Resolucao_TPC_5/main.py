import os
import re

# ----------------------------------------------------------------------------------------------------------------------
def moedas_invalidas(lista_moedas):
    # devolve uma string com todas as moedas inválidas
    inval = ""

    for moeda in lista_moedas:

        # se a moeda for centimo
        if moeda != "1c" and moeda != "2c" and moeda != "5c" and moeda != "10c" and moeda != "20c" and moeda != "50c" and moeda != "1e" and moeda != "2e":
            inval = inval + moeda + " "

    return inval


# ----------------------------------------------------------------------------------------------------------------------
def moedas_validas(lista_moedas):
    nova_lista = []

    for moeda in lista_moedas:

        # se a moeda for centimo
        if moeda == "1c" or moeda == "2c" or moeda == "5c" or moeda == "10c" or moeda == "20c" or moeda == "50c" or moeda == "1e" or moeda == "2e":
            nova_lista.append(moeda)

    return nova_lista

# ----------------------------------------------------------------------------------------------------------------------
def converte_para_string(saldo_double):
    # pega na string saldo e retorna o double correspondente

    saldo_string = '{:.2f}'.format(saldo_double)
    saldo_string = saldo_string.replace('.', '')
    saldo_string = saldo_string[:1] + 'e' + saldo_string[1:] + 'c'

    return saldo_string

# ----------------------------------------------------------------------------------------------------------------------
def converte_para_double(saldo):
    # pega na string saldo e retorna o double correspondente

    saldo_double = float(saldo[:1] + '.' + saldo[2:-1])

    return saldo_double

# ----------------------------------------------------------------------------------------------------------------------
def analisa_numero(numeros, saldo):
    # função que analisa o tipo de número e altera o saldo

    saldo_numerico = converte_para_double(saldo)

    if numeros[0] == 6 and numeros[1] == 0 and numeros[2] == 1:
        print("maq: 'Esse número não é permitido neste telefone. Queira discar novo número!'")


    elif numeros[0] == 6 and numeros[1] == 4 and numeros[2] == 1:
        print("maq: 'Esse número não é permitido neste telefone. Queira discar novo número!'")


    elif numeros[0] == 0 and numeros[1] == 0:
        if saldo_numerico >= 1.50:
            saldo_numerico -= 1.50
        else:
            print("maq: 'Saldo insuficiente'")


    elif numeros[0] == 2:
        if saldo_numerico >= 0.25:
            saldo_numerico -= 0.25
        else:
            print("maq: 'Saldo insuficiente'")

    elif numeros[0] == 8 and numeros[1] == 0 and numeros[2] == 0:
        saldo_numerico -= 0

    elif numeros[0] == 8 and numeros[1] == 0 and numeros[2] == 8:
        if saldo_numerico >= 0.10:
            saldo_numerico -= 0.10
        else:
            print("maq: 'Saldo insuficiente'")

    else:
        # caso esteja no formato pedido
        print("maq: 'Esse número não é permitido neste telefone. Queira discar novo número!'")

    saldo = converte_para_string(saldo_numerico)
    return saldo

# ----------------------------------------------------------------------------------------------------------------------
def extrair_numeros(string):
    padrao = r'(\d)'
    numeros = re.findall(padrao, string)

    # Converte os números de string para inteiros
    numeros = [int(n) for n in numeros]

    return numeros

# ----------------------------------------------------------------------------------------------------------------------
def extrair_moedas(string):
    padrao = r'(\d+[c|e])'
    moedas = re.findall(padrao, string)

    return moedas

# ----------------------------------------------------------------------------------------------------------------------
def saldo_string(lista_moedas):
    # esta função serve apenas para converter a lista de moedas obtida em extrair_moedas() numa string que representa o saldo
    # ainda não está a fazer a validação das moedas introduzidas

    saldo = ""

    total_euros = 0
    total_centimos = 0

    for moeda in lista_moedas:

        # se a moeda for centimo
        if re.search("c", moeda):
            total_centimos += int(re.search("(\d+)", moeda).group(1))

        # se a moeda for euro
        elif re.search("e", moeda):
            total_euros += int(re.search("(\d+)", moeda).group(1))

    saldo = f"{total_euros}e{total_centimos}c"

    return saldo

# ----------------------------------------------------------------------------------------------------------------------

def main():
    # construção da UI

    print(" ")
    print("--------------------------------- TPC 5 ---------------------------------")
    print(" ")
    print("Iniciando simulação de cabine telefónica")
    print("Insira comandos [LEVANTAR, POUSAR, MOEDA <lista de valores>, T=numero, ABORTAR] ")
    print(" ")
    print("-------------------------------------------------------------------------")
    print(" ")

    comand = ""
    comand = input("")  # input reservado para os comandos passados pelo utilizador



    if comand == "LEVANTAR":
        print("maq: 'Introduza moedas.'")

        comand2 = ""
        saldo = "0"
        troco = "0"

        while comand2 != "ABORTAR" or comand2 != "POUSAR":


            comand2 = input("")

            if re.match(r"(MOEDA)", comand2):
                moedas = extrair_moedas(comand2)

                #validação das moedas introduzidas
                inval = moedas_invalidas(moedas)
                val = moedas_validas(moedas)

                # se não houver moedas inválidas
                if inval.__len__() >= 1:
                    saldo = saldo_string(val)
                    #print(moedas)
                    print(f"maq: '{inval}- moeda inválida; saldo = {saldo}'")


                else:
                    saldo = saldo_string(val)
                    print(f"maq: 'saldo = {saldo}'")



            elif re.fullmatch(r"(T)=\d+", comand2):
                num_telefone = extrair_numeros(comand2)
                #print(num_telefone)
                saldo = analisa_numero(num_telefone, saldo)
                print(f"maq: 'saldo = {saldo}'")


            elif comand2 == "POUSAR":
                troco = saldo
                print(f"maq: 'troco={troco}; Volte sempre!'")
                break

            elif comand2 == "ABORTAR":
                print("Abortado.......")
                print("Devolvendo moedas.......")
                break


            else:
                print("Comando inválido!!!")

    elif comand == "ABORTAR":
        print("Abortado.......")
        print("Devolvendo moedas.......")
        return


if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------