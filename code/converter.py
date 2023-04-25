# ESTE MODULO SERVE PARA CRIAR O FICHEIRO JSON FINAL

import json
import lexico
import re
import criaDicionario

def toml_to_json(toml_file_path):
    try:
        json_filename = re.search(r"\\([^.]*)", toml_file_path).group(1)
        json_filename = "json_files\\"  + json_filename + ".json"
        #toml_file = open(toml_file_path, encoding='UTF-8')
        json_file = open(json_filename, "w", encoding='UTF-8')
        #lines = toml_file.readlines()

        # criar um dicionário que vai ser gerado com os tokens obtidos do lex
        dict = {}

        print(f"\n")
        # faz a analise lexica e imprime os tokes no terminal
        lista_tokens = lexico.analisar_ficheiro_toml(toml_file_path)
        print("\n")
        dict = criaDicionario.cria_dict(toml_file_path)

        if len(dict) > 0:
            print("Ficheiro convertido com sucesso (ver pasta json_files)\n")

        # escrita final no ficheiro json
        json.dump(dict, json_file, ensure_ascii=False, indent=8)

    finally:

        #toml_file.close()
        json_file.close()


