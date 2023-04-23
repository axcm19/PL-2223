# ESTE MODULO SERVE PARA OBTER OS TOKENS NECESSÁRIOS PARA DEPOIS CONSTRUIR UM DICIONÁRIO

from ply import lex

tokens = (
    'CHAVE',
    'EQUALS',
    'STRING',
    'INTEIRO',
    'FLOAT',
    'BOOLEAN',
    'ARRAY_START',
    'ARRAY_END',
    'VIRGULA',
    'DOT',
    'NEWLINE',
    'COMENTARIO'
)

"""
tokens = (
    'STRING',
    'INTEGER',
    'FLOAT',
    'BOOLEAN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'EQUALS',
    'COMMA',
)
"""

# Expressões regulares para os tokens
t_EQUALS = r'='
t_ARRAY_START = r'\['
t_ARRAY_END = r'\]'
t_VIRGULA = r','
t_DOT = r'\.'
t_ignore_COMENTARIO = r'\#.*' # --> comentários não são essenciais para o ficheiro json logo podem ser ignorados
t_ignore = ' \t'

# Funções de match para os tokens
def t_CHAVE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_STRING(t):
    r'"[^"]*"|\'[^\']*\''
    t.value = t.value[1:-1]
    return t

def t_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_BOOLEAN(t):
    r'true|false'
    t.value = True if t.value == 'true' else False
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t


# Função para tratamento de erros
def t_error(t):
    print(f'Caractere ilegal: {t.value[0]}')
    t.lexer.skip(1)

# Construção do analisador léxico
lexer = lex.lex()

# Função para analisar um ficheiro TOML cujo nome é passado como argumento
def analisar_ficheiro_toml(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        dados = file.read()
        lexer.input(dados)

        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)

        #return tokens