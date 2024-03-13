# ESTE MODULO SERVE PARA CRIAR O FICHEIRO JSON FINAL

import json
import lexico
import re
import criaDicionario

# ----------------------------------------------------------------------------------------------------------------------
# ---> função que cria o ficheiro json com o resultado do parser

def toml_to_json(toml_file_path):
    try:
        json_filename = re.search(r"(\\|\/)([^.]*)", toml_file_path).group(2)

         # se a diretoria for num sistema Windows
        if re.search(r"(\\)", toml_file_path) != None:
            json_filename = "json_files\\" + json_filename + ".json"

        # se a diretoria for num sistema Linux
        if re.search(r"(\/)", toml_file_path) != None:
            json_filename = "json_files/" + json_filename + ".json"


        json_file = open(json_filename, "w", encoding='UTF-8')

        print(f"\n")
        # faz a analise lexica e imprime os tokes no terminal
        lexico.analisar_ficheiro_toml(toml_file_path)
        print("\n")

        # criar um dicionário aninhado (porque contem outros dicionários dentro) que vai ser gerado com o parse YACC
        dict = criaDicionario.cria_dict(toml_file_path)

        if len(dict) > 0:
            print("Ficheiro convertido com sucesso (ver pasta json_files)\n")

        # escrita final no ficheiro json
        json.dump(dict, json_file, ensure_ascii=False, indent=8)

    finally:

        json_file.close()


