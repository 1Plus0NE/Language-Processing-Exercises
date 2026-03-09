import ply.lex as lex
import re

states = (('OFF', 'exclusive'),)

tokens = (
    'INT', 'EQ',
    'ON', 'OFF'
)

t_ANY_ignore = ' \t'

def t_ANY_ON(t):
    r'ON'
    t.lexer.begin('INITIAL')
    return t

def t_ANY_OFF(t):
    r'OFF'
    t.lexer.begin('OFF')
    return t

def t_ANY_EQ(t):
    r'='
    return t

def t_ANY_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ANY_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ANY_OTHER(t):
    r'.'
    pass

def t_ANY_error(t):
    t.lexer.skip(1)

lexer = lex.lex(reflags=re.IGNORECASE)

text = "Contas: 15, 20; = off! 29 30... =?"

lexer.input(text)

def red(total, token, active):

    if token.type == "EQ":
        print(total)

    elif token.type == "INT" and active:
        total += token.value

    elif token.type == "OFF":
        active = False

    elif token.type == "ON":
        active = True

    return total, active

active = True
total = 0

for tok in lexer:
    total, active = red(total, tok, active)