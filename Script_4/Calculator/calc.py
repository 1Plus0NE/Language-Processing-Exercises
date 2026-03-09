import ply.lex as lex

states = (
    ('EXPRESSION', 'exclusive'), 
    ('VAR', 'exclusive')
)

tokens = ('INT', 'IDEN', 
          'ADD', 'MUL', 'MINUS',
          'SLASH', 'STAR', 
          'EQ', 'HASH',
          'QUESTION', 'EXCLAMATION'
)

literals = ('(', ')')

t_EXPRESSION_ADD = r'\+'
t_EXPRESSION_MINUS = r'\-'
t_EXPRESSION_MUL = r'\*'
t_EXPRESSION_SLASH = r'/'

t_ANY_ignore = ' \t'

def t_STAR(t):
    r'\*'
    return t

def t_HASH(t):
    r'\#'
    return t

def t_QUESTION(t):
    r'\?'
    t.lexer.begin('VAR')
    return t

def t_EXCLAMATION(t):
    r'\!'
    t.lexer.begin('EXPRESSION')
    return t

def t_EQ(t):
    r'='
    t.lexer.begin('EXPRESSION')
    return t

def t_INITIAL_EXPRESSION_VAR_IDEN(t):
    r'[A-Za-z]+'
    return t

def t_EXPRESSION_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ANY_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ANY_error(t):
    print(f"Illegal character: '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input("! ! x + 10")

for tok in lexer:
    print(tok)