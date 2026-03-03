import ply.lex as lex

# --------------------------
# Lista de tokens
tokens = (
    'CREATE', 'TABLE', 'PRIMARY_KEY', 'TEXT', 'INTEGER',
    'SELECT', 'FROM', 'WHERE',
    'AND', 'OR', 'NOT',
    'IDEN', 'INT', 'STRING',
    'EQUAL', 'NOTEQUAL', 'LT', 'GT', 'LE', 'GE',
    'LPAREN', 'RPAREN', 'COMMA', 'SEMICOLON', 'DOT',
    'PLUS', 'MINUS', 'MUL', 'DIV'
)

# --------------------------
# Palavras-chave
reserved = {
    'CREATE': 'CREATE',
    'TABLE': 'TABLE',  
    'TEXT': 'TEXT',
    'INTEGER': 'INTEGER',
    'SELECT': 'SELECT',
    'FROM': 'FROM',
    'WHERE': 'WHERE',
    'AND': 'AND',
    'OR': 'OR',
    'NOT': 'NOT'
}

# --------------------------
# Tokens simples / regex
t_EQUAL     = r'='
t_NOTEQUAL  = r'<>'
t_LE        = r'<='
t_GE        = r'>='
t_LT        = r'<'
t_GT        = r'>'
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_MUL       = r'\*'
t_DIV       = r'/'

t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_COMMA     = r','
t_SEMICOLON = r';'
t_DOT       = r'\.'

t_ignore = ' \t'


def t_PRIMARY_KEY(t):
    r'PRIMARY[ ]KEY'
    return t

def t_IDEN(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# --------------------------
# Test input
test_input = """
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER
);

SELECT id, name FROM users WHERE age >= 18;
"""

lexer.input(test_input)

for tok in lexer:
    print(tok)