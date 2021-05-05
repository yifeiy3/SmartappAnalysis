import ply.lex as lex 
import re

tokens = (
    'INPUT',
    'BOOL',
    'DEF',
    'DEFINITION',
    'MAPPING',
    'PREFERENCE',
    'SECTION',
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
    'EQUAL',
    'MATH',
    'NUMBER',
    'COMMENT',
    'LONGCOMMENT',
    'NEWLINE'
)

def MyLexer():
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_DOT = r'\.'
    t_COMMA = r'\,'
    t_COLON = r'\:'

    def t_INPUT(t):
        r'input'
        return t 

    def t_DEFINITION(t):
        r'definition'
        return t 

    def t_MAPPING(t):
        r'mappings'
        return t 

    def t_DEF(t):
        r'def'
        return t 
    
    def t_LBRACKET(t):
        r'(\n*)(\s)*\{(\n*)(\s)*'
        return t

    def t_RBRACKET(t):
        r'(\n*)(\s)*\}(\n*)(\s)*'
        return t

    def t_BOOL(t):
        r'true|false'
        return t 

    def t_SECTION(t):
        r'section'
        return t

    def t_PREFERENCE(t):
        r'preferences'
        return t 

    def t_REQUIRED(t):
        r'required'
        return t 

    def t_MULTIPLE(t):
        r'multiple'
        return t 

    def t_EQUAL(t):
        r'='
        return t
    
    def t_MATH(t):
        r'\+|\-|\*|\/|<<|>>|!|\~'
        return t

    def t_STRING(t):
        r'((\')([a-zA-Z0-9_,\.-\\\'\s!#$%^&\*\(\)]*)(\'))|((\")([a-zA-Z0-9_,\.-\\\'\s!#$%^&\*\(\)]*)(\"))'
        return t 

    def t_NUMBER(t):
        r'[0-9]+'
        return t 
        
    def t_IDENT(t):
        r'[a-zA-Z0-9_-]+'
        return t 

    def t_NEWLINE(t):
        r'\n+'
        return t

    t_ignore = ' \t'

    def t_COMMENT(t):
        r'\/\/.+'
        pass 

    def t_LONGCOMMENT(t):
        r'(\/\*)(.|\n)+(\*\/)'
        pass 

    def t_error(t):
        print("Illegal character {0}".format(t.value[0]))
        t.lexer.skip(1)

    return lex.lex()

if __name__ == '__main__':
    # data = '''def installed()
    #     {
    #         subscribe(switches, "switch.off", offhandler)
    #         subscribe(location, changedLocationMode)
    #         subscribe(app, timedTouch)
    #     }'''
    data = '''
            def appTouch(evt) 
            {
                switchesoff.off()
            }'''
    lexer = MyLexer()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
