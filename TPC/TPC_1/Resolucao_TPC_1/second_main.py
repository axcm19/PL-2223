from listaDoentes import Lista_Doentes

# programa secundário que imprime as tabelas das distribuições sem ocorrer interação com o utilizador

def main():
    # abrir o ficheiro myheart.csv e criar o catalogo principal de doentes
    catalogo_doentes = Lista_Doentes()
    catalogo_doentes.parse("myheart.csv")

    # construção da UI

    print(" ")
    print("------------------------------ TPC 1 ------------------------------")
    print(" ")
    print("Calculando a distribuição da doença por sexo...")
    print("Calculando a distribuição da doença por escalões etários...")
    print("Calculando a distribuição da doença por níveis de colesterol...")
    print(" ")
    print(" ")
    print(" ")
    print("*** RESULTADOS ***")
    print(" ")

    print(f"TOTAL DE DOENTES = {catalogo_doentes.total_doentes()}")
    print(" ")

    print("---> Tabela da distribuição da doença por sexo")
    print(" ")
    catalogo_doentes.tabela_sexo()
    print(" ")

    print("---> Tabela da distribuição da doença por escalões etários")
    print(" ")
    catalogo_doentes.tabela_etaria()
    print(" ")

    print("---> Tabela da distribuição da doença por níveis de colesterol...")
    print(" ")
    catalogo_doentes.tabela_colestrol()
    print(" ")

    print("-------------------------------------------------------------------")

if __name__ == "__main__":
    main()
