# ESTE MODULO SERVE PARA CRIAR UM DICIONÁRIO COM BASE NOS TOKENS OBTIDOS DO LEX

# apenas um prototipo!!!

import ply.yacc as yacc

from lexico import tokens

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_error(p):
    print("Erro sintático no input!")

parser = yacc.yacc()

# Função para analisar os tokens obtidos do lex e criar um dicionário
def cria_dict():

    while s := input(''):

        if(s == "EXIT"):
            break

        result = parser.parse(s)
        print(result)

        return result

