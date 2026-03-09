import ply.lex as lex

tokens = (
    'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET',
    'COLON', 'COMMA',
    'STR',
    'INT'
)

t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_COLON     = r':'
t_COMMA     = r','

t_ignore = ' \t'

def t_STR(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  # remover aspas
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value) 
    return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print(f"Illegal character: '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

with open("cinema.json", "r") as f:
    db = f.read()

lexer.input(db)

for tok in lexer:
    print(tok)