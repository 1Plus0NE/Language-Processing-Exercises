import ply.lex as lex

tokens = (
    'VAR', 'IDEN', 'INT', 'TRUE', 'FALSE',
    'OR', 'AND', 'NOT', 'IMPLIES',
    'LPAREN', 'RPAREN', 'SEMICOLON'
)

t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_SEMICOLON = r';'

t_ignore = ' \t'

t_OR      = r'\\/'     # \/
t_AND     = r'/\\'     # /\
t_NOT     = r'!'
t_IMPLIES = r'=>'

def t_VAR(t):
    r'var'
    return t

def t_TRUE(t):
    r'True'
    t.value = True
    return t

def t_FALSE(t):
    r'False'
    t.value = False
    return t

def t_IDEN(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    # Não sobrescreve VAR, TRUE, FALSE
    if t.value == 'var':
        t.type = 'VAR'
    elif t.value == 'True':
        t.type = 'TRUE'
        t.value = True
    elif t.value == 'False':
        t.type = 'FALSE'
        t.value = False
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

test_input = """var A;
var B;
var C;
A \\/ B /\\ True => (C \\/ !D)"""

lexer.input(test_input)

for tok in lexer:
    print(tok)