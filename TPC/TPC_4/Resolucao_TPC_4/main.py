import csv
import json
import os
import re


# -----------------------------------------------------------------------------------------------------------------------

def maior(lista_notas):
    maior = 0

    for nota in lista_notas:
        if int(nota) > maior:
            maior = int(nota)

    return maior


# -----------------------------------------------------------------------------------------------------------------------

def menor(lista_notas):
    menor = int(lista_notas[0])

    for nota in lista_notas:
        if int(nota) < menor:
            menor = int(nota)

    return menor


# -----------------------------------------------------------------------------------------------------------------------

def media(lista_notas):
    soma = 0
    quantos = 0
    media = 0

    for nota in lista_notas:
        soma += int(nota)
        quantos += 1

    media = soma / quantos

    return media


# -----------------------------------------------------------------------------------------------------------------------

def sum(lista_notas):
    soma = 0

    for nota in lista_notas:
        soma = soma + int(nota)

    return soma


# -----------------------------------------------------------------------------------------------------------------------

def csv_to_json(csv_file_path):
    try:
        json_filename = re.search(r"\\([^.]*)", csv_file_path).group(1)
        json_filename = "json_files\\"  + json_filename + ".json"
        csv_file = open(csv_file_path, encoding='UTF-8')
        json_file = open(json_filename, "w", encoding='UTF-8')
        lines = csv_file.readlines()
        existe_notas = False
        existe_func = False
        func = ""

        # se detetar que existe um campo chamado "notas"
        if re.search(r"(Notas)", lines[0]) != None:
            existe_notas = True

        # se detetar que está a ser aplicada uma função à lista de notas
        if re.search(r"::([^,]*)", lines[0]) != None:
            existe_func = True
            func = re.search(r"::([^,]*)", lines[0]).group(1)

        # remover a primeira linha de cabeçalho porque não queremos que seja escrita no ficheiro json
        lines.pop(0)

        # lista para guardar cada dicionario criado por cada linha do csv
        # esta lista vai ser colocada no json através da função 'dump'
        list_for_json = []

        for line in lines:

            # criar um dicionário para cada linha do csv
            dict = {}

            list = line.split(",")
            dict["Número"] = list[0].strip()
            dict["Nome"] = list[1].strip()   # strip() para remover \n que pode surgir em algumas strings
            dict["Curso"] = list[2].strip()

            if existe_notas:

                # se estiver a ser aplicada uma função à lista de notas
                if existe_func:
                    # criar a lista de notas
                    notas = []
                    notas = re.search(r",\b\d+(?:,\d+)*(,)?", line).group(0).split(",")

                    # retirar valores nulos da lista de notas
                    notas.pop(0)
                    if (notas[notas.__len__() - 1] == ''):
                        notas.pop(notas.__len__() - 1)

                    if (func == "sum"):
                        res = sum(notas)

                        key = "Notas_" + func
                        dict[key] = res

                    if (func == "media"):
                        res = media(notas)

                        key = "Notas_" + func
                        dict[key] = res

                    if (func == "maior"):
                        res = maior(notas)

                        key = "Notas_" + func
                        dict[key] = res

                    if (func == "menor"):
                        res = menor(notas)

                        key = "Notas_" + func
                        dict[key] = res

                # se não estiver a ser aplicada uma função à lista de notas
                elif existe_func == False:

                    # criar a lista de notas
                    notas = []
                    notas = re.search(r",\b\d+(?:,\d+)*(,)?", line).group(0).split(",")

                    # retirar valores nulos da lista de notas
                    notas.pop(0)
                    if (notas[notas.__len__() - 1] == ''):
                        notas.pop(notas.__len__() - 1)


                    dict["Notas"] = notas

            list_for_json.append(dict)

        # escrita final no ficheiro json
        json.dump(list_for_json, json_file, ensure_ascii=False, indent=8)

    finally:

        csv_file.close()
        json_file.close()


# -----------------------------------------------------------------------------------------------------------------------

def main():
    csv_file_path = ""
    # construção da UI
    print(" ")
    print("--------------------------------- TPC 4 ---------------------------------")
    print(" ")
    print("Insira o caminho do ficheiro que quer converter (ver pasta csv_files)... ")
    print("Insira 'q' para fechar programa")
    print(" ")
    print("-------------------------------------------------------------------------")
    print(" ")

    # criar diretoria para os ficheiros json criados
    newpath = r"json_files"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    while csv_file_path != 0:

        csv_file_path = input('---> ')

        if csv_file_path == "q":
            print("")
            print("Saindo.......")
            print("")
            break

        else:
            csv_to_json(csv_file_path)
            print("Ficheiro convertido com sucesso (ver pasta json_files)\n")


if __name__ == "__main__":
    main()
