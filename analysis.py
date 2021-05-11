from lexer import tokens, MyLexer
from parsefile import MyParser
from AST import parseAST
from CFG import CFG, buildCFG, appendOrCreate
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
cfg = buildCFG(smartappDict, environmentDict, sideEffectDict)
print("relationships before inverse: {0}".format(cfg.findRelationships()))
print("************************")
deviceRelationships = cfg.invertRelationships()
print("found relationships: {0}".format(deviceRelationships))

#Finally, print our analysis result to a file
with open("analysisResult.txt", "w") as rfile:
    for devices in deviceRelationships.keys():
        if devices == 'None':
            #sideEffect by its own is not interesting
            continue 
        for posStates in deviceRelationships[devices].keys():
            rfile.write("Device: {0}, State: {1}:\n".format(devices, posStates))
            rfile.write("Can be reached through: \n")
            for inDevices in deviceRelationships[devices][posStates].keys():
                for inDeviceStates in deviceRelationships[devices][posStates][inDevices].keys():
                    for paths in deviceRelationships[devices][posStates][inDevices][inDeviceStates]:
                        rfile.write("\t Initial Device: {0}, Initial State: {1}, Through path: \n\t\t: {2}\n".format(
                            inDevices,
                            inDeviceStates,
                            paths
                        ))
            rfile.write("\n\n")

