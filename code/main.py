import os
import converter

# ----------------------------------------------------------------------------------------------------------------------
# ---> função main para arrancar o programa

def main():
    toml_file_path = ""
    # construção da UI
    print(" ")
    print("--------------------------------- TomlToJson v.1 ---------------------------------")
    print(" ")
    print("Insira o caminho do ficheiro toml que quer converter... ")
    print("Insira 'q' para fechar programa")
    print(" ")
    print("----------------------------------------------------------------------------------")
    print(" ")

    # criar diretoria para os ficheiros json criados
    newpath = r"json_files"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    while toml_file_path != 0:

        toml_file_path = input('---> ')

        if toml_file_path == "q":
            print("")
            print("Saindo.......")
            print("")
            break

        else:
            converter.toml_to_json(toml_file_path)


if __name__ == "__main__":
    main()
