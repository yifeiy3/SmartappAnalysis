from lexer import tokens, MyLexer
from parsefile import MyParser
from AST import parseAST
from CFG import CFG, buildCFG, appendOrCreate
from checkConflicts import checkCircularConflict, checkDirectConflict
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

# # Example A -- Circular
# codefiles = ['Smartapps/Circular/turnon.groovy', 'Smartapps/Circular/turnoff.groovy', 'Smartapps/Circular/simplecircular.groovy']
# #devices each smartapp subscribed to in the environment
# turnoffDict = {'switches': ["Virtual Switch 1"], "switchesoff": ["Virtual Switch 3"]}
# turnonDict = {'switches': ["Virtual Switch 2"], "switcheson": ["Virtual Switch 1"]}
# simplecircularDict = {'switches': ["Virtual Switch 3"], "switchesoff": ["Virtual Switch 2"]}
# environmentDict = \
#     {'Smartapps/Circular/turnon.groovy' : turnonDict, 
#     'Smartapps/Circular/turnoff.groovy': turnoffDict, 
#     'Smartapps/Circular/simplecircular.groovy': simplecircularDict}

# # Example B -- Direct Conflict
# codefiles = ['Smartapps/DirecConf/turnonswitch.groovy', 'Smartapps/DirecConf/turnoffswitch.groovy']
# #devices each smartapp subscribed to in the environment
# turnoffDict = {'switchon': ["Virtual Switch 1"], "switchoff": ["Virtual Switch 2"]}
# turnonDict = {'switchon': ["Virtual Switch 2"], "switchoff": ["Virtual Switch 3"]}
# environmentDict = \
#     {'Smartapps/DirecConf/turnonswitch.groovy' : turnonDict, 
#     'Smartapps/DirecConf/turnoffswitch.groovy': turnoffDict}

# Example C -- Hidden Interaction
codefiles = ['Smartapps/Hidden/hidden.groovy', 'Smartapps/Hidden/smokealarmdoor.groovy']
#devices each smartapp subscribed to in the environment
hiddenDict = {'switchon': ["Virtual Switch 1"], "switchoff": ["Virtual Switch 2"],"smokealarm": ["Smoke Alarm"], "Door":["Door"]}
smokealarmdoorDict = {'alarms': ["Smoke Alarm"], "door": ["Door"]}
environmentDict = \
    {'Smartapps/Hidden/hidden.groovy' : hiddenDict, 
    'Smartapps/Hidden/smokealarmdoor.groovy': smokealarmdoorDict}


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

#print("received dictionary from AST: {0}".format(smartappDict))
cfg = buildCFG(smartappDict, environmentDict, sideEffectDict)
#print("relationships before inverse: {0}".format(cfg.findRelationships()))
deviceRelationships = cfg.invertRelationships()
#print("found relationships: {0}".format(deviceRelationships))
circularConflict = checkCircularConflict(deviceRelationships)
directConflict = checkDirectConflict(deviceRelationships)

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

    rfile.write("Found circular Conflicts: \n\n")
    for devices in circularConflict.keys():
        for states in circularConflict[devices].keys():
            for startStates, paths in circularConflict[devices][states]:
                rfile.write("\t Device : {0}, state: {1}, from starting state: {2}, \n\t with paths: {3}".format(
                    devices,
                    states,
                    startStates,
                    paths,
                ))
                rfile.write("\n\n")

    rfile.write("Found direct Conflicts: \n\n")
    for devices in directConflict.keys():
        rfile.write("\t The path in each group is in direct conflict with every path in other group for device {0}\n".format(devices))
        for i in range(len(directConflict[devices])):
            rfile.write("\t Group {0}: \n".format(i))
            groupdict = directConflict[devices][i]
            for conflictedDevices in groupdict.keys():
                for conflictedStates in groupdict[conflictedDevices].keys():
                    for paths in groupdict[conflictedDevices][conflictedStates]:
                        rfile.write("\t\t Starting device: {0} with state: {1}, \n\t\t through path: {2}".format(
                            conflictedDevices,
                            conflictedStates,
                            paths,
                        ))
                        rfile.write("\n")
            rfile.write("\n")