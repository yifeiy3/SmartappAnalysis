import ply.yacc as yacc 
import logging
#token map from lexer
from lexer import tokens, MyLexer

class MyParser():
    def p_program_funcDef(self, p):
        '''
            program : program funcDef
                    | funcDef
        '''
        if(len(p) == 2):
            p[0] = (None, [p[1]])
        else:
            if p[1][1]:
                p[1][1].append(p[2])
            else:
                p[1] = (p[1][0], [p[2]])
            p[0] = p[1]

    def p_program_block(self, p):
        '''
            program : program prefBlock
                    | prefBlock
                    | notNeededBlock
                    | program notNeededBlock
        '''
        if(len(p) == 2):
            p[0] = ([p[1]], None)
        else:
            if p[1][0]:
                p[1][0].append(p[2])
            else:  
                p[1] = ([p[2]], p[1][1])
            p[0] = p[1]

    def p_notNeededBlock(self, p):
        '''
            notNeededBlock : DEFINITION LPAREN error RPAREN
                        | MAPPING LBRACKET error RBRACKET
        '''
        pass 

    def p_funcDef(self, p):
        '''funcDef : DEF IDENT LPAREN paramlist RPAREN LBRACKET stmtList RBRACKET
                | DEF IDENT LPAREN RPAREN LBRACKET stmtList RBRACKET
        '''
        if(len(p) == 9):
            p[0] = ('funcDef', p[2], p[4], p[7])
        else:
            p[0] = ('funcDef', p[2], [], p[6])

    def p_prefBlock(self, p):
        'prefBlock : PREFERENCE LBRACKET sectionblocklist RBRACKET'
        p[0] = ('preferences', p[3])

    def p_sectionblocklist(self, p):
        '''sectionblocklist : sectionblock
                | sectionblocklist NEWLINE sectionblock
                | sectionblocklist NEWLINE'''
        if(len(p) == 4):
            p[1].append(p[3])
            p[0] = p[1]
        elif(len(p) == 3):
            p[0] = p[1]
        else:
            p[0] = [p[1]]

    def p_sectionblock(self, p):
        'sectionblock : SECTION LPAREN STRING RPAREN ILBRACKET blockparamlist IRBRACKET'
        p[0] = p[6]

    def p_blockparamlist(self, p):
        '''blockparamlist : blockparamlist COMMA blockparam
                | blockparam'''
        if(len(p) == 4):
            p[1].append(p[3])
            p[0] = p[1]
        else:
            p[0] = [p[1]]

    def p_blockparam(self, p):
        '''blockparam : INPUT STRING
                    | STRING
                    | TITLE COLON STRING
                    | MULTIPLE COLON BOOL
                    | REQUIRED COLON BOOL'''
        if(p[1] == 'input'):
            p[0] = ('input', p[2])
        elif(p[1] == 'multiple'):
            p[0] = ('multiple', str(p[3]))
        elif(p[1] == 'required'):
            p[0] = ('required', str(p[3]))
        elif(p[1] == 'title'):
            p[0] = ('title', str(p[3]))
        else:
            p[0] = ('capabilities', p[1])

    def p_stmtList_withNewline(self, p):
        'stmtList : stmtList NEWLINE'
        p[0] = p[1]

    def p_stmtList(self, p):
        '''stmtList : stmtList NEWLINE stmt
                | stmt 
                | stmtList stmt''' 
        if(len(p) == 4):
            p[1].append(p[3])
            p[0] = p[1]
        elif(len(p) == 3):
            if(p[1][-1] != None) and p[2] != None:
                #if the last result does not come from an omitted line due to error handling,
                #the rule for stmtList stmt does not work.
                raise Exception(
                        "Invalid file, can not have stmt following stmtlist. list: {0}, stmt: {1}".format(p[1], p[2])
                    )
            p[1].append(p[2])
            p[0] = p[1]
        else:
            p[0] = [p[1]]
        print("we got here in returning stmtlist with p[0]: {0}".format(p[0]))
        
    def p_stmt(self, p):
        '''stmt : functionCall
            | functionWithObj'''
        if p[1] and p[1][0] == 'functioncall':
            p[0] = (p[1][0], p[1][1], p[1]) #to make it compatible to functionCall with obj
        else:
            p[0] = p[1]

    def p_stmt_error(self, p):
        'stmt : error NEWLINE'
        print("we got here in stmt with p[1]: {0}".format(p[1]))
        pass 

    def p_functionCall(self, p):
        '''functionCall : IDENT LPAREN paramlist RPAREN
                    | IDENT LPAREN RPAREN'''
        if(len(p) == 5):
            p[0] = ('functioncall', p[1], p[3])
        else:
            p[0] = ('functioncall', p[1], [])

    def p_functionCall_error(self, p):
        '''functionCall : IDENT LPAREN error NEWLINE
                    | IDENT error NEWLINE'''
        print("we got here in function call with p[3]: {0}".format(p[3]))
        pass

    def p_functionWithObj(self, p):
        'functionWithObj : IDENT DOT functionCall'
        if p[3] == None: #error when parsing functionCall
            p[0] = None
        else:
            p[0] = ('functionWithObj', p[1], p[3])

    def p_functionWithObj_error(self, p):
        'functionWithObj : IDENT DOT error NEWLINE'
        print("we got here in function call with obj with p[3]: {0}".format(p[3]))
        pass

    def p_paramlist(self, p):
        '''paramlist : paramlist COMMA param
                    | param'''
        if(len(p) == 4):
            p[1].append(p[3])
            p[0] = p[1]
        else:
            p[0] = [p[1]]

    def p_param(self, p):
        '''param : identparam
                | strparam
                | numparam '''
        p[0] = p[1]

    def p_identparam(self, p):
        '''identparam : IDENT
                    | IDENT NEWLINE
                    | NEWLINE IDENT'''
        if p[1] == '\n':
            p[0] = ("ident", str(p[2]))
        else:
            p[0] = ("ident", str(p[1]))

    def p_strparam(self, p):
        '''strparam : STRING
                | STRING NEWLINE
                | NEWLINE STRING'''
        if p[1] == '\n':
            p[0] = ("string", str(p[2]))
        else:
            p[0] = ("string", str(p[1]))

    def p_numparam(self, p):
        '''numparam : NUMBER
                | NUMBER NEWLINE
                | NEWLINE NUMBER'''
        if p[1] == '\n':
            p[0] = ("number", str(p[2]))
        else:
            p[0] = ("number", str(p[1]))

    def p_error(self, p):
        if not p:
            print("end of file")
            return 
        
        if p.type == 'NEWLINE':
            print("we got here in p_error")
            self.parser.errok()

        print("Ignored token: {0}".format(p))
        return
    
    def build(self, logger=None):
        self.logger = logger 
        self.tokens = tokens 
        self.lexer = MyLexer()
        self.parser = yacc.yacc(module=self)
    
    def parseFile(self, file):
        if self.logger:
            result = self.parser.parse(file, lexer=self.lexer, debug=self.logger)
        else:
            result = self.parser.parse(file, lexer=self.lexer)
        return result

if __name__ == '__main__':
    # Build the parser
    logging.basicConfig(
        level = logging.DEBUG,
        filename = "parselog.txt",
        filemode = "w",
        format = "%(filename)10s:%(lineno)4d:%(message)s"
    )
    log = logging.getLogger()
    parseObj = MyParser()
    parseObj.build(log)
    
    s = '''
        definition(
            name: "Big Turn ON",
            namespace: "smartthings",
            author: "SmartThings",
            description: "Turn your lights on when the SmartApp is tapped or activated.",
            category: "Convenience",
            iconUrl: "https://s3.amazonaws.com/smartapp-icons/Meta/light_outlet.png",
            iconX2Url: "https://s3.amazonaws.com/smartapp-icons/Meta/light_outlet@2x.png"
        )

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
                log.debug "wtf... it.name"
            }
            def attr = monitor.supportedAttributes
            attr.each{
                log.debug "ok. it.name, it.values"
            }
        }
        '''
    #result = parser.parse(s, lexer=MyLexer(), debug=log)
    result = parseObj.parseFile(s)
    print(result)