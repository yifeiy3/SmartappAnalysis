import ply.lex as lex 
import re

states = (
    ('insideblock', 'exclusive'),
)

tokens = (
    'INPUT',
    'BOOL',
    'DEF',
    'DEFINITION',
    'MAPPING',
    'ARRAY',
    'PREFERENCE',
    'SECTION',
    'TITLE',
    'STRING',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'ILBRACKET',
    'RBRACKET',
    'IRBRACKET',
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
    t_ANY_LPAREN = r'\('
    t_ANY_RPAREN = r'\)'
    t_ANY_DOT = r'\.'
    t_ANY_COMMA = r'\,'
    t_ANY_COLON = r'\:'
    t_ANY_ARRAY = r'[\[\]]'

    def t_ANY_INPUT(t):
        r'input'
        return t 

    def t_ANY_DEFINITION(t):
        r'definition'
        return t 

    def t_ANY_MAPPING(t):
        r'mappings'
        return t 

    def t_ANY_DEF(t):
        r'def'
        return t 
    
    def t_ANY_TITLE(t):
        r'title'
        return t
    
    # def t_LBRACKET(t):
    #     r'(\n*)(\s)*\{'
    #     t.lexer.level = 1
    #     return t

    def t_insideblock(t):
        r'(\n*)(\s)*\{'
        t.lexer.level = 1
        t.lexer.begin('insideblock')
        t.type = 'LBRACKET'
        return t 

    def t_insideblock_LBRACKET(t):
        r'(\n*)(\s)*\{'
        t.lexer.level += 1
        t.type = 'ILBRACKET'
        return t

    def t_insideblock_RBRACKET(t):
        r'\}'
        t.lexer.level -= 1
        if t.lexer.level == 0:
            t.type = 'RBRACKET'
            t.lexer.begin('INITIAL')
        else:
            t.type = 'IRBRACKET'
        return t 

    def t_ANY_BOOL(t):
        r'true|false'
        return t 

    def t_ANY_SECTION(t):
        r'section'
        return t

    def t_ANY_PREFERENCE(t):
        r'preferences'
        return t 

    def t_ANY_REQUIRED(t):
        r'required'
        return t 

    def t_ANY_MULTIPLE(t):
        r'multiple'
        return t 

    def t_ANY_EQUAL(t):
        r'='
        return t

    def t_ANY_STRING(t):
        r'((\')([a-zA-Z0-9_,\{\}\.\?\-\/\\\'\s!#$%\^:&\@\*\(\)]*)(\'))|((\")([a-zA-Z0-9:_,\{\}\/\.\-\\\?\'\s!#$%\^&\@\*\(\)]*)(\"))'
        t.value = t.value.replace('\'', '').replace('\"', '') 
        return t 

    def t_ANY_NUMBER(t):
        r'[0-9]+'
        return t 
        
    def t_ANY_IDENT(t):
        r'([a-zA-Z0-9_-]+(\?)*)'
        t.value = t.value.replace('?', '')
        return t

    def t_ANY_NEWLINE(t):
        r'\n(\n|\s)*'
        return t

    t_ignore = ' \t\n'
    t_insideblock_ignore = ' \t'

    def t_ANY_COMMENT(t):
        r'\/\/.+'
        pass 

    def t_ANY_LONGCOMMENT(t):
        r'(\/\*)(.|\n)+(\*\/)'
        pass 

    def t_ANY_MATH(t):
        r'\+|\-|\*|\/|<<|>>|!|\~'
        return t

    def t_ANY_error(t):
        print("Illegal character {0}".format(t.value[0]))
        t.lexer.skip(1)

    return lex.lex()

if __name__ == '__main__':
    data = '''
            definition(
                name: "17355Project1",
                namespace: "yifeiy3",
                author: "Eric Yang",
                description: "Turn off both lights",
                category: "",
                iconUrl: "https://s3.amazonaws.com/smartapp-icons/Convenience/Cat-Convenience.png",
                iconX2Url: "https://s3.amazonaws.com/smartapp-icons/Convenience/Cat-Convenience@2x.png",
                iconX3Url: "https://s3.amazonaws.com/smartapp-icons/Convenience/Cat-Convenience@2x.png")


            preferences {
                section("Turn off this switch") {
                    input "switchesoff", "capability.switch", required: true
                }
                section("When this switch is off") {
                    input "switches", "capability.switch", required: true
                }
                section("Switch for reference") {
                    input "switchesref", "capability.switch", required: true
                }
            }

            def installed() {
                log.debug "Installed with settings: $settings"

                initialize()
            }

            def updated() {
                log.debug "Updated with settings: $settings"

                unsubscribe()
                initialize()
            }

            def initialize() {
                subscribe(switches, "switch.off", apphandler)
            }

            def apphandler(evt){
                switchesoff?.off()
            }
        '''
    lexer = MyLexer()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
