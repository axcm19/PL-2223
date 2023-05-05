# ESTE MODULO SERVE PARA CRIAR UM DICIONÁRIO COM BASE NOS TOKENS OBTIDOS DO LEX

# apenas um prototipo!!!

import ply.yacc as yacc

from lexico import tokens


def p_toml(p):
    """
    toml : sections
    """
    p[0] = p[1]


def p_sections(p):
    """
    sections : sections section
             | section
    """
    if len(p) == 2:
        p[0] = p[1]

    else:
        lista = list(p[2].keys())
        lista_temp = lista[0].split('.')

        if len(lista_temp) > 1:
            temp_dict = p[1]

            for key in lista_temp[:-1]:

                if key not in temp_dict:
                    temp_dict[key] = {}
                temp_dict = temp_dict[key]

            if type(temp_dict) == list:
                temp_dict.append({lista_temp[-1]: p[2][lista[0]]})
            else:
                temp_dict[lista_temp[-1]] = p[2][lista[0]]
            print(p[0], "  ", p[1])
            p[0] = p[1]
        else:
            key = list(p[2].keys())[0]
            if key in p[1]:
                for elem in p[2][key]:
                    p[1][key].append(elem)
            else:
                p[1].update(p[2])

            p[0] = p[1]


def p_section(p):
    """
    section : TAGA NAMETAG FPR content
	        | TAGA NAMETAG FPR
    """
    if len(p) == 5:
        p[0] = {p[2]: p[4]}
    else:
        p[0] = {p[2]: {}}


def p_section_subtag(p):
    """
    section : TAGA SUBTAG FPR content
	        | TAGA SUBTAG FPR
    """
    if len(p) == 5:
        p[0] = {p[2]: p[4]}


    else:
        p[0] = {p[2]: {}}


def p_section_statements(p):
    """
    section : statement
    """
    p[0] = p[1]


def p_section_aot_nametag(p):
    """
    section : AOTA NAMETAG AOTF content
            | AOTA NAMETAG AOTF
    """
    if len(p) == 5:
        p[0] = {p[2]: [p[4]]}

    else:
        p[0] = {p[2]: []}


def p_content(p):
    """
    content : content statement
            | statement
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1].update(p[2])
        p[0] = p[1]


def p_statement_VAR(p):
    """
    statement : VAR IGUAL value
    """
    p[0] = {p[1]: p[3]}


def p_statement_DOTTEDKEY(p):
    """
    statement : DOTTEDKEY IGUAL value
    """
    lista = p[1].split(".")
    dicionario = p[3]

    for chave in reversed(lista):
        dicionario = {chave: dicionario}

    p[0] = dicionario


def p_value(p):
    """
    value : DATA
          | TIME
          | list
          | inlinetable
    """
    p[0] = p[1]


def p_inlinetable(p):
    """
    inlinetable : AC vars FC
    """
    p[0] = p[2]


def p_inlinetable_VARS(p):
    """
    vars : vars VIRG var
         | var
    """
    if len(p) == 4:
        p[1].update(p[3])
        p[0] = p[1]

    else:
        p[0] = p[1]


def p_inlinetable_VAR(p):
    """
    var : VAR IGUAL value
    """
    p[0] = {p[1]: p[3]}


def p_INT(p):
    """
    value : INT
    """
    p[0] = int(p[1])


def p_INDIANFORMAT(p):
    """
    value : INDIANFORMAT
    """
    lista = p[1].split("_")
    string = ""
    for i, elemento in enumerate(lista):
        if i % 2 == 0:
            string += elemento
    p[0] = int(string)


def p_SIGNALINTS(p):
    """
    value : SIGNALINTS
    """
    p[0] = int(p[1])


def p_OCTAL(p):
    """
    value : OCTAL
    """
    p[0] = int(p[1], 8)


def p_HEXADECIMAL(p):
    """
    value : HEXADECIMAL
    """
    p[0] = int(p[1], 16)


def p_BINARY(p):
    """
    value : BINARY
    """
    p[0] = int(p[1], 2)


def p_FLOAT(p):
    """
    value : FLOAT
    """
    p[0] = float(p[1])


def p_STRING(p):
    """
    value : STRING
    """

    p[0] = p[1].split("\"")[1]


def p_MULTILINESTRING(p):
    """
    value : MULTILINESTRING
    """
    p[0] = p[1].split("\"\"\"")[1]


def p_BOOL(p):
    """
    value : BOOL
    """
    p[0] = bool(p[1])


def p_list(p):
    """
    list : APR elements FPR
    """

    p[0] = p[2]


def p_elements(p):
    """
    elements : elements VIRG value
             | value
    """
    if len(p) == 2:
        p[0] = [p[1]]

    else:
        p[1].append(p[3])
        p[0] = p[1]


def p_error(p):
    if p:
        print(f"Erro de sintaxe na entrada {p.value}")
    else:
        print("Erro de sintaxe no final da entrada")


parser = yacc.yacc()


# Função para analisar os tokens obtidos do lex e criar um dicionário
def cria_dict(toml_file_path):
    with open(toml_file_path, 'r', encoding='UTF-8') as toml_file:
        data = toml_file.read()
        parser.parse(data)

    return parser.parse(data)



