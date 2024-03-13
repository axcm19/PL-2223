from doente import Doente
from listaDoentes import Lista_Doentes

def main():
    # abrir o ficheiro myheart.csv e criar o catalogo principal de doentes
    catalogo_doentes = Lista_Doentes()
    catalogo_doentes.parse("myheart.csv")

    # construção da UI
    saida = -1
    while saida != 0:
        print(" ")
        print("------------------------------ TPC 1 ------------------------------")
        print(" ")
        print("1 - Calcular a distribuição da doença por sexo")
        print("2 - Calcular a distribuição da doença por escalões etários")
        print("3 - Calcular a distribuição da doença por níveis de colesterol")
        print("4 - Imprimir na forma de uma tabela uma distribuição")
        print("5 - Imprimir o catalogo de doentes")
        print("0 - Saír")
        print(" ")
        print("-------------------------------------------------------------------")
        print(" ")

        saida = int(input("Introduza a sua opcao-> "))

        if saida == 0:
            print("")
            print("Saindo.......")
            print("")

        elif saida == 1:
            # Calcular a distribuição da doença por sexo
            print("")
            print(f"TOTAL DE DOENTES = {catalogo_doentes.total_doentes()}")
            print("")

            catalogo_doentes.calcula_dist_sexo()
            l = input("Prima enter para continuar")

        elif saida == 2:
            # Calcular a distribuição da doença por escalões etários

            print("")
            print(f"Maior idade = {catalogo_doentes.maior_idade()}")
            print(f"Menor idade = {catalogo_doentes.menor_idade()}")
            print("")
            print(f"TOTAL DE DOENTES = {catalogo_doentes.total_doentes()}")
            print("")

            catalogo_doentes.calcula_dist_etaria()

            l = input("Prima enter para continuar")

        elif saida == 3:
            # Calcular a distribuição da doença por níveis de colesterol

            print("")
            print(f"Maior colestrol = {catalogo_doentes.maior_colestrol()}")
            print(f"Menor colestrol = {catalogo_doentes.menor_colestrol()}")
            print("")
            print(f"TOTAL DE DOENTES = {catalogo_doentes.total_doentes()}")
            print("")
            print("NOTA:")
            print("\tNivel 0 -> 0 a 9")
            print("\tNivel 1 -> 10 a 19")
            print("\tNivel 2 -> 20 a 29")
            print("\t...")
            print("")

            catalogo_doentes.calcula_dist_colestrol()

            l = input("Prima enter para continuar")

        elif saida == 4:
            # Imprimir na forma de uma tabela uma distribuição
            print("")
            print("Qual distribuição quer imprimir numa tabela?")
            print("\t1 - Distribuição da doença por sexo")
            print("\t2 - Distribuição da doença por escalões etários")
            print("\t3 - Distribuição da doença por níveis de colesterol")
            print("")

            opcao = int(input("\tIntroduza a sua opcao-> "))

            if opcao == 1:
                catalogo_doentes.tabela_sexo()
            elif opcao == 2:
                catalogo_doentes.tabela_etaria()
            elif opcao == 3:
                catalogo_doentes.tabela_colestrol()

            l = input("Prima enter para continuar")

        elif saida == 5:
            # Imprimir o catalogo de doentes

            for d in catalogo_doentes.lista_doentes:
                d.imprime()

            l = input("Prima enter para continuar")


        else:
            print("Opção inválida...")
            l = input("prima enter para continuar")

if __name__ == "__main__":
    main()
