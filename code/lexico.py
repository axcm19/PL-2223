# ESTE MODULO SERVE PARA OBTER OS TOKENS NECESSÁRIOS PARA DEPOIS CONSTRUIR UM DICIONÁRIO

from ply import lex

states = (
    ('taga', 'inclusive'),
    ('aot','inclusive'),
)

tokens = (
    'TAGA',
    'NAMETAG',
    'VAR',
    'INT',
    'STRING',
    'FLOAT',
    'DATA',
    'IGUAL',
    'COMENTARIO',
    'BOOL',
    'APR',
    'FPR',
    'VIRG',
    'DP',
    'SUBTAGA',
    'SUBTAG',
    'TIME',
    'DOTTEDKEY',
    'MULTILINESTRING',
    'INDIANFORMAT',
    'SIGNALINTS',
    'BINARY',
    'OCTAL',
    'HEXADECIMAL',
    'AC',
    'FC',
    'AOTA',
    'AOTF'
)


t_VAR = r'[A-Za-z_\-]+'
t_DOTTEDKEY = r'[A-Za-z_\-]+(\.[A-Za-z_\-]+)+'
t_INT = r'\d+'
t_INDIANFORMAT = r'\d+(_\d+)+'
t_SIGNALINTS = r'[+-]\d+'
t_BINARY = r'0b[01]+'
t_OCTAL = r'0o[0-7]+'
t_HEXADECIMAL = r'0x[0-9a-fA-F]+'
t_STRING = r'".*?"'
#t_FLOAT = r'\d+,\d+'
t_DATA = r'\d{4}\-\d{2}\-\d{2}'
t_TIME = r'\d{2}\:\d{2}\:\d{2}'
t_IGUAL = r'\='
t_APR = r'\['
t_FPR = r'\]'
t_VIRG = r'\,'
t_DP = r'\:'
t_AC = r'\{'
t_FC = r'\}'

def t_AOTA(t):
    r'\n+\[\['
    t.lexer.begin('aot')
    return t

def t_aot_NAMETAG(t):
    r'[A-Za-z_\-\.0-9]+'
    return t

def t_aot_SUBTAG(t):
    r'\w+(\.\w+)*'
    return t

def t_aot_AOTF(t):
    r'\]\]'
    t.lexer.begin('INITIAL')
    return t

def t_taga_SUBTAG(t):
    r'\w+(\.\w+)*'
    return t

def t_TAGA(t):
    r'\n+\s*\['
    t.lexer.begin('taga')
    return t

def t_taga_NAMETAG(t):
    r'[A-Za-z_\-\.]+'
    return t


def t_taga_FPR(t):
    r'\]'
    t.lexer.begin('INITIAL')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMENTARIO(t):
    r'\#.*\n'
    pass

def t_MULTILINESTRING(t):
    r'"""[\n\w\s]*"""'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    return t

def t_BOOL(t):
    r'true|false'
    return t


t_ignore = ' \t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)


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