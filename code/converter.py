import json

import lexico
import re

"""
Prototipo que ainda precisa de muitas alterações!
"""

def toml_to_json(toml_file_path):
    try:
        json_filename = re.search(r"\\([^.]*)", toml_file_path).group(1)
        json_filename = "json_files\\"  + json_filename + ".json"
        toml_file = open(toml_file_path, encoding='UTF-8')
        json_file = open(json_filename, "w", encoding='UTF-8')

        # lista para guardar cada dicionario criado por cada linha do csv
        # esta lista vai ser colocada no json através da função 'dump'
        list_for_json = []

        # criar um dicionário
        dict = {}

        tokens = lexico.tokenizer(toml_file)

        print(f"\n")
        for tok in tokens:
            print(tok)
        print(f"\n")

        list_for_json.append(dict)

        # escrita final no ficheiro json
        json.dump(list_for_json, json_file, ensure_ascii=False, indent=8)

    finally:

        toml_file.close()
        json_file.close()


