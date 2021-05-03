import ply.yacc as yacc 
#token map from lexer
from lexer import tokens 

def p_stmtList(p):
    'stmtList: 
def p_stmt(p):
    'stmt: functionCall'
    p[0] = p[1]

def p_function_call(p):
    'functionCall: IDENT LPAREN paramlist RPAREN'
    p[0] = ('functioncall', p[1], p[3])

def p_paramlist(p):
    '''paramlist: paramlist COMMA param
                | param'''
    if(len(p) == 4):
        p[0] = p[1].append(p[3])
    else:
        p[0] = [p[1]]

def p_param(p):
    '''param: identparam
            | strparam
            | numparam '''
    p[0] = p[1]

def p_identparam(p):
    'identparam: IDENT'
    p[0] = ("ident", str(p[1]))

def p_strparam(p):
    'strparam: STRING'
    p[0] = ("string", str(p[1]))

def p_numparam(p):
    'numparam: NUMBER'
    p[0] = ("number", str(p[1]))
