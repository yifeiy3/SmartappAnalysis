
class deviceNode():
    def __init__(self, name):
        self.name = name
        self.inNeighbors = []
        self.outNeighbors = []
    
    def printNode(self):
        print("DeviceNode Name: {0}".format(self.name))
        print("In Neighbors:")
        for inItems in self.inNeighbors:
            print("\t{0}".format(inItems))
        for outItems in self.outNeighbors:
            print("\t{0}".format(outItems))

class CFG():
    def __init__(self, deviceDict):
        #@param the dictionary that each input for each smartapp correspond to
        self.graph = self.buildgraph(deviceDict)

    def buildgraph(self, deviceDict):
        deviceSet = set()

        #obtain all the devices in the environment
        for smartapps in deviceDict.keys():
            for inputs in deviceDict[smartapps].keys():
                for devices in deviceDict[smartapps][inputs]:
                    deviceSet.add(devices)

        #give each device a node corresponding to it
        return {device : deviceNode(device) for device in deviceSet}
    
    def addEdge(self, deviceNameFrom, deviceNameTo, smartappName, currentState, changedState):
        '''
            param[1]'s state change to param[4] causes param[2]'s state change to param[5],
            via smartapp with name param[3]
        '''
        outDeviceNode = self.graph[deviceNameFrom]

        #deviceNameFrom changes from currentState causes deviceNameTo to change to changedState
        outDeviceNode.outNeighbors.append((smartappName, deviceNameTo, currentState, changedState))
        inDeviceNode = self.graph[deviceNameTo]
        inDeviceNode.inNeighbors.append((smartappName, deviceNameFrom, currentState, changedState))

    def printCFG(self):
        print('Printed CFG:')
        print('*****************************************')
        for deviceNodes in self.graph.keys():
            self.graph[deviceNodes].printNode()

def buildCFG(relationDict, deviceDict):
    '''
        This function builds a relationship graph between Samsung Smartapps
        that we have constructed AST with static analysis

        @param: relationship dictionary of smartapps we got from AST
        @param: devices each smartapp subscribe to in the environment
    '''
    cfg = CFG(deviceDict)

    for smartapps in relationDict.keys():
        parsedrelations, parsedSideEffects = relationDict[smartapps]

        for devices in parsedrelations.keys():
            deviceNamesFrom = deviceDict[smartapps][devices]
            for currentState in parsedrelations[devices].keys():
                for toDevice, changedState in parsedrelations[devices][currentState]:
                    deviceNamesTo = deviceDict[smartapps][toDevice]
                    for deviceNameFrom in deviceNamesFrom:
                        for deviceNameTo in deviceNamesTo:
                            cfg.addEdge(deviceNameFrom, deviceNameTo, smartapps, currentState, changedState)
    
    cfg.printCFG()
        
