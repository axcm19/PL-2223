import ply.lex as lex

def analiser():

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


    while data := input("---> "):
        lexer.input(data)

        if data == "EXIT":
            return

        else:
            while tok := lexer.token():
                print(tok)