import ply.lex as lex

tokens = ('LPAREN', 'RPAREN')

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print(f"Illegal character: '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input("()(())\n[()()]")

for tok in lexer:
    print(tok)