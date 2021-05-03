import ply.lex as lex 
import re

tokens = (
    'INPUT',
    'DEF',
    'STRING',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'DOT',
    'REQUIRED',
    'MULTIPLE',
    'COMMA',
    'COLON',
    'IDENT',
    'NUMBER',
)
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_DOT = r'\.'
t_COMMA = r'\,'
t_COLON = r'\:'

def t_INPUT(t):
    r'input'
    t.value = t.value
    return t 

def t_DEF(t):
    r'def'
    t.value = t.value
    return t 

def t_REQUIRED(t):
    r'required'
    t.value = t.value
    return t 

def t_MULTIPLE(t):
    r'multiple'
    t.value = t.value
    return t 

def t_STRING(t):
    r'((\')([a-zA-Z0-9_,\.-\\\'\s!#$%^&\*\(\)]*)(\'))|((\")([a-zA-Z0-9_,\.-\\\'\s!#$%^&\*\(\)]*)(\"))'
    t.value = t.value
    return t 

def t_NUMBER(t):
    r'[0-9]+'
    return t 
    
def t_IDENT(t):
    r'[a-zA-Z0-9_.-]+'
    t.value = t.value
    return t 

t_ignore = ' \n\t'
def t_error(t):
    print("Illegal character {0}".format(t.value[0]))
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
    def installed()
{
	subscribe(switches, "switch.off", offhandler)
	subscribe(location, changedLocationMode)
	subscribe(app, timedTouch)
}
'''

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
