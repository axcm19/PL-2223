# ESTE MODULO SERVE PARA CRIAR UM DICIONÁRIO COM BASE NOS TOKENS OBTIDOS DO LEX

# apenas um prototipo!!!

import ply.yacc as yacc

from lexico import tokens

dictionary = {}
current_table = ""

def p_dict(p):
    '''dict : entry
            | dict entry'''
    pass

def p_entry(p):
    '''entry : key_value_pair
             | array
             | table'''
    pass

def p_key_value_pair(p):
    '''key_value_pair : STRING EQUALS value'''
    dictionary[p[1]] = p[3]

def p_array(p):
    '''array : STRING ARRAY_START array_values ARRAY_END'''
    dictionary[p[1]] = p[3]

def p_array_values(p):
    '''array_values : value
                    | array_values VIRGULA value'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_table(p):
    '''table : CHAVE STRING CHAVE
             | CHAVE STRING DOT STRING CHAVE
             | CHAVE CHAVE dict CHAVE'''
    global current_table
    if len(p) == 4:
        current_table = p[2]
    elif len(p) == 6:
        current_table = p[2] + '.' + p[4]
    else:
        dictionary[current_table] = p[3]

def p_value(p):
    '''value : STRING
             | INTEIRO
             | FLOAT
             | BOOLEAN'''
    p[0] = p[1]

#def p_error(p):
   # print(f"Syntax error at line {p.lineno}: Unexpected token {p.value}")

parser = yacc.yacc()

# Função para analisar os tokens obtidos do lex e criar um dicionário
def cria_dict(toml_file_path):
    with open(toml_file_path, 'r', encoding='UTF-8') as toml_file:
        data = toml_file.read()
        parser.parse(data)

    return dictionary



