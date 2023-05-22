# ESTE MODULO SERVE PARA CRIAR UM DICIONÁRIO COM BASE NOS TOKENS OBTIDOS DO LEX

import ply.yacc as yacc

from lexico import tokens

# ----------------------------------------------------------------------------------------------------------------------
# ---> regras gerais do parser

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
    section : DICT LISTNAME RBRACKET content
	        | DICT LISTNAME RBRACKET
    """
    if len(p) == 5:
        p[0] = {p[2]: p[4]}
    else:
        p[0] = {p[2]: {}}


def p_section_dictname(p):
    """
    section : DICT DICTNAME RBRACKET content
	        | DICT DICTNAME RBRACKET
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


def p_section_openlist_listname(p):
    """
    section : OPENLIST LISTNAME CLOSELIST content
            | OPENLIST LISTNAME CLOSELIST
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


def p_statement_KEY(p):
    """
    statement : KEY EQUALS value
    """
    p[0] = {p[1]: p[3]}


def p_statement_DOTTEDKEY(p):
    """
    statement : DOTTEDKEY EQUALS value
    """
    lista = p[1].split(".")
    dicionario = p[3]

    for chave in reversed(lista):
        dicionario = {chave: dicionario}

    p[0] = dicionario


def p_value(p):
    """
    value : DATE
          | HOURS
          | list
          | inlinetable
    """
    p[0] = p[1]


def p_inlinetable(p):
    """
    inlinetable : LCHAVETA vars RCHAVETA
    """
    p[0] = p[2]


def p_inlinetable_KEYS(p):
    """
    vars : vars COMMA var
         | var
    """
    if len(p) == 4:
        p[1].update(p[3])
        p[0] = p[1]

    else:
        p[0] = p[1]


def p_inlinetable_KEY(p):
    """
    var : KEY EQUALS value
    """
    p[0] = {p[1]: p[3]}

# ----------------------------------------------------------------------------------------------------------------------
# ---> regras do parser que definem o que é considerado como valor (value)

def p_INTEGER(p):
    """
    value : INTEGER
    """
    p[0] = int(p[1])

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
    #p[0] = p[1].split("\"\"\"")[1]
    p[0] = p[1]


def p_BOOLEAN(p):
    """
    value : BOOLEAN
    """
    p[0] = bool(p[1])

# ----------------------------------------------------------------------------------------------------------------------
# ---> regras do parser para as listas

def p_list(p):
    """
    list : LBRACKET elements RBRACKET
    """

    p[0] = p[2]


def p_elements(p):
    """
    elements : elements COMMA value
             | value
    """
    if len(p) == 2:
        p[0] = [p[1]]

    else:
        p[1].append(p[3])
        p[0] = p[1]

# ----------------------------------------------------------------------------------------------------------------------
# ---> regra para erro de sintaxe

def p_error(p):
   print(f"Erro de sintaxe na linha {p.lineno}: Token inválido {p.value}")

# ----------------------------------------------------------------------------------------------------------------------
# ---> criação do parser

parser = yacc.yacc()

# ----------------------------------------------------------------------------------------------------------------------
# ---> função para analisar os tokens obtidos do lex e criar um dicionário

def cria_dict(toml_file_path):
    with open(toml_file_path, 'r', encoding='UTF-8') as toml_file:
        data = toml_file.read()
        parser.parse(data)

    return parser.parse(data)



