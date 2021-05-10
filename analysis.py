from lexer import tokens, MyLexer
from parsefile import MyParser
from AST import parseAST
import logging 

logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()
parser = MyParser()
parser.build(log)

codefiles = ['Smartapps/turnon.groovy']
smartappDict = {}

for smartapp in codefiles:
    s = ''
    with open(smartapp, 'r') as cfile:
        s = cfile.read()

    result = parser.parseFile(s)

    parsedrelations, parsedSideEffects = parseAST(result)
    smartappDict[smartapp] = (parsedrelations, parsedSideEffects)