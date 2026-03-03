import ply.lex as lex

tokens = ( 'IDEN', 'INT', 'FLOAT', 'ADD', 'SUB', 'DIV', 'MUL' )

literals = ('(', ')')

t_ignore = ' \t'
t_ADD    = r'\+'
t_SUB    = r'-'
t_MUL    = r'\*'
t_DIV    = r'/'

def t_FLOAT(t):
  r'\d+\.\d*|\.\d+'
  t.value = float(t.value)
  return t

def t_INT(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_IDEN(t):
  r'[A-Za-z]+'
  return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
  print(f"Illegal character: {t.value[0]}")
  t.lexer.skip(1)

lexer = lex.lex()

# Test input
lexer.input("10 + 3 * x - 5 / 2.5")

# Iterate over tokens
for tok in lexer:
    print(tok)