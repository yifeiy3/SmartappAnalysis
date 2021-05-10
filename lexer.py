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
    
    def t_ANY_MATH(t):
        r'\+|\-|\*|\/|<<|>>|!|\~'
        return t

    def t_ANY_STRING(t):
        r'((\')([a-zA-Z0-9_,\.-\\\'\s!#$%^&\*\(\)]*)(\'))|((\")([a-zA-Z0-9_,\.-\\\'\s!#$%^&\*\(\)]*)(\"))'
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

    def t_ANY_error(t):
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
        preferences {
            section("Turn on...") {
                input "switches", "capability.switch", multiple: true
            }
            section("When I touch the app, turn off..."){
                input "switchesoff", "capability.switch", multiple: true
            }
            section("When I touch the app, be active after..."){
                input "timer", "number", required: true, title: "seconds?"
            }
            section("Monitor the app using..."){
                input "monitor", "capability.execute", required:false
            }
        }

        mappings {
            path("/endpoint") {
                action: [
                    GET: "handlerURL"
                ]
            }
        }
        def handlerURL()
        {
            log.debug("this is called")
        }

        def installed()
        {
            subscribe(switches, "switch.off", offhandler)
            subscribe(location, changedLocationMode)
            subscribe(app, timedTouch)
        }

        def updated()
        {
            unsubscribe()
            subscribe(switches, "switch.off", offhandler)
            subscribe(location, changedLocationMode)
            subscribe(app, timedTouch)
        }

        def offhandler(evt){
            log.debug "$switches wtf"
            monitor?.execute("AppName: Big Turn ON, ($switches switch : on)")
            location.setMode("Away")
            switches?.off()
        }

        def changedLocationMode(evt) {
            log.debug "changedLocationMode: $evt"
            switches?.on()
            switchesoff?.off()
        }

        def timedTouch(evt){
            log.debug "a timed modification of this app"
            runIn(timer, appTouch)
        }

        def appTouch(evt) {
            log.debug "appTouch: $evt, $switches"
            monitor?.execute("AppName: Big Turn ON, ($switches switch : on, $switchesoff switch : off)")
            switches?.on()
            switchesoff?.off()
            location.setMode("Away")
            def att2 = switches.supportedAttributes
            att2.each{
                log.debug "wtf... $it.name"
            }
            def attr = monitor.supportedAttributes
            attr.each{
                log.debug "ok. $it.name, $it.values"
            }
        }'''
    data = '''switches?'''
    lexer = MyLexer()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
