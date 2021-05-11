from lexer import tokens, MyLexer
from parsefile import MyParser
from AST import parseAST
from CFG import buildCFG
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

# Example A
codefiles = ['Smartapps/Circular/turnon.groovy', 'Smartapps/Circular/turnoff.groovy', 'Smartapps/Circular/simplecircular.groovy']
#devices each smartapp subscribed to in the environment
turnoffDict = {'switches': ["Virtual Switch 1"], "switchesoff": ["Virtual Switch 3"]}
turnonDict = {'switches': ["Virtual Switch 2"], "switcheson": ["Virtual Switch 1"]}
simplecircularDict = {'switches': ["Virtual Switch 3"], "switchesoff": ["Virtual Switch 2"]}
environmentDict = \
    {'Smartapps/Circular/turnon.groovy' : turnonDict, 
    'Smartapps/Circular/turnoff.groovy': turnoffDict, 
    'Smartapps/Circular/simplecircular.groovy': simplecircularDict}

smartappDict = {}
sideEffectDict = {}

for smartapp in codefiles:
    s = ''
    with open(smartapp, 'r') as cfile:
        s = cfile.read()

    result = parser.parseFile(s)

    parsedrelations, parsedSideEffects = parseAST(result)
    smartappDict[smartapp] = parsedrelations
    sideEffectDict[smartapp] = parsedSideEffects

print("received dictionary from AST: {0}".format(smartappDict))
cfg = buildCFG(smartappDict, environmentDict)
print("found relationships: {0}".format(cfg.findRelationships()))