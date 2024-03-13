# ESTE MODULO SERVE PARA OBTER OS TOKENS NECESSÁRIOS PARA DEPOIS CONSTRUIR UM DICIONÁRIO

from ply import lex

# ----------------------------------------------------------------------------------------------------------------------
# ---> dois estados que representam quando entramos num dicionário ou numa lista de dicionários

states = (
    ('openlist', 'inclusive'),
    ('opendict','inclusive'),
)

# ----------------------------------------------------------------------------------------------------------------------
# ---> esta secção é relativa à identificação de tokens

tokens = (
    'DICT',            # --> quando começa um novo dicionário (Table segundo o site do Toml)
    'LISTNAME',        # --> nome da lista de dicionários (Array of Tables segundo o site do Toml)
    'KEY',
    'INTEGER',
    'STRING',
    'BINARY',
    'FLOAT',
    'DATE',
    'EQUALS',
    'COMMENT',
    'BOOLEAN',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'DICTNAME',         # --> nome do dicionário começado
    'HOURS',
    'DOTTEDKEY',
    'MULTILINESTRING',
    'INDIANNUMBER',
    'SIGNAL',
    'OCTAL',
    'HEXADECIMAL',
    'LCHAVETA',
    'RCHAVETA',
    'OPENLIST',         # --> quando começa uma nova lista de dicionários
    'CLOSELIST'         # --> quando se fecha a lista de dicionários
)


# --> chaves
t_KEY = r'[A-Za-z_\-]+'
t_DOTTEDKEY = r'[A-Za-z_\-]+(\.[A-Za-z_\-]+)+'

# --> numeros inteiros
t_INTEGER = r'\d+'
t_INDIANNUMBER = r'\d+(_\d+)+'          # --> formato de numeros que é mencionado no site do TOML
t_SIGNAL = r'[+-]\d+'
t_BINARY = r'0b[01]+'
t_OCTAL = r'0o[0-7]+'
t_HEXADECIMAL = r'0x[0-9a-fA-F]+'

# --> string e float
t_STRING = r'".*?"'                     # --> apanha tudo que esteja dentro de aspas (incluindo as aspas)
t_FLOAT = r'\d+\.\d+'

# --> tempo
t_DATE = r'\d{4}\-\d{2}\-\d{2}'
t_HOURS = r'\d{2}\:\d{2}\:\d{2}'

# --> 'igual e comentario
t_EQUALS = r'\='
t_ignore_COMMENT = r'\#.*'              # --> comentários não são essenciais para o ficheiro json logo podem ser ignorados
t_BOOLEAN = r'(?i)(true|false)'         # --> não quer saber se é lowercase ou uppercase

# --> separadores e limitadores
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r'\,'
t_LCHAVETA = r'\{'
t_RCHAVETA = r'\}'


# ----------------------------------------------------------------------------------------------------------------------
# ---> esta secção é relativa a quando temos uma lista com dicionários lá dentro

def t_OPENLIST(t):
    r'\n+\[\['
    t.lexer.begin('openlist')
    return t

def t_openlist_LISTNAME(t):
    r'[A-Za-z_\-\.0-9]+'
    return t

def t_openlist_DICTNAME(t):     # é uma lista de dicionários logo temos de ir buscar o nome do dicionário
    r'\w+(\.\w+)*'
    return t

def t_openlist_CLOSELIST(t):
    r'\]\]'
    t.lexer.begin('INITIAL')
    return t


# ----------------------------------------------------------------------------------------------------------------------
# ---> esta secção é relativa a quando temos apenas um dicionário sozinho

def t_DICT(t):
    r'\n+\s*\['
    t.lexer.begin('opendict')
    return t

def t_opendict_DICTNAME(t):
    r'\w+(\.\w+)*'
    return t

def t_opendict_RBRACKET(t):
    r'\]'
    t.lexer.begin('INITIAL')
    return t

# ----------------------------------------------------------------------------------------------------------------------
# ---> regras extra

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_MULTILINESTRING(t):
    r'"""[\n\w\s]*"""'
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

# ----------------------------------------------------------------------------------------------------------------------
# ---> criação do lexer

lexer = lex.lex()

# ----------------------------------------------------------------------------------------------------------------------
# ---> função para analisar um ficheiro TOML cujo nome é passado como argumento

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