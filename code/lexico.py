import ply.lex as lex

"""
Prototipo que ainda precisa de muitas alterações!
"""

def tokenizer(ficheiro):

    tokens = (
        'PALAVRA',
        'VIRGULA',
        'PONTOE',
        'PONTOI',
        'PONTOF',
        'RETS'
    )

    t_PALAVRA = r'[\w\-]+'
    t_VIRGULA = r','
    t_PONTOE = r'\!'
    t_PONTOI = r'\?'
    t_PONTOF = r'\.'
    t_RETS = r'\.{3,}'

    t_ignore = ' \t\n'

    def t_error(t):
        print(f"Caracter ilegal {t.value[0]}")
        t.lexer.skip(1)

    lexer = lex.lex()

    content = ficheiro.read()
    lexer.input(content)

    tokens = []

    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)

    return tokens



"""""
# Exemplo de uso lendo um arquivo
with open('toml_files\exemplo1.toml', 'r', encoding='UTF-8') as file:
    content = file.read()
    tokens = tokenizer(content)
    print(tokens)
"""