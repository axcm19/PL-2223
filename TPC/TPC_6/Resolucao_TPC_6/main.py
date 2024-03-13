import lex_analiser

def main():

    # construção da UI
    saida = -1
    while saida != 0:
        print(" ")
        print("--------------------------------- TPC 6 ---------------------------------")
        print(" ")
        print("1 - Usar o analisador léxico")
        print("0 - SAIR")
        print(" ")
        print("-------------------------------------------------------------------------")
        print(" ")

        saida = int(input("Introduza a sua opcao-> "))

        if saida == 0:
            print("")
            print("Saindo.......")
            print("")

        elif saida == 1:
            print(" ")
            print("-------------------------------------------------------------------------")
            print("NOTA: Insira EXIT para sair do analisador")
            print("-------------------------------------------------------------------------")
            print(" ")
            lex_analiser.analiser()

        else:
            print("Opção inválida...")
            l = input("prima enter para continuar")

if __name__ == "__main__":
    main()

