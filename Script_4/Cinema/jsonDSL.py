import ply.lex as lex

tokens = (
    'STR', 'INT',
    'TITLE', 'CAST', 'YEAR', 'GENRES'
)

literals = ('{', '}', '[', ']', ',', ':')

t_ignore = ' \t'

def t_TITLE(t):
    r'"title"'
    return t

def t_CAST(t):
    r'"cast"'
    return t

def t_YEAR(t):
    r'"year"'
    return t

def t_GENRES(t):
    r'"genres"'
    return t

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