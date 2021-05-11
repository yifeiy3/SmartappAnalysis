
class deviceNode():
    def __init__(self, name):
        self.name = name
        self.inNeighbors = {}
        self.outNeighbors = {}
    
    def printNode(self):
        print("DeviceNode Name: {0}".format(self.name))
        print("In Neighbors:")
        print("\t{0}".format(self.inNeighbors))
        print("Out Neighbors:")
        print("\t{0}".format(self.outNeighbors))

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
        def appendOrCreate(d, key1, key2, value):
            if key1 not in d.keys():
                d[key1] = {}
                d[key1][key2] = [value] 
            else:
                if key2 not in d[key1].keys():
                    d[key1][key2] = [value] 
                else:
                    d[key1][key2].append(value)
    
        outDeviceNode = self.graph[deviceNameFrom]

        #{currentState : {deviceNameTo: [(smartappName, changedState)]}}
        appendOrCreate(outDeviceNode.outNeighbors, currentState, deviceNameTo, (smartappName, changedState))
        
        inDeviceNode = self.graph[deviceNameTo]
        #{changedState : {deviceNameFrom: [(smartappName, currentState)]}}
        appendOrCreate(inDeviceNode.inNeighbors, changedState, deviceNameFrom, (smartappName, currentState))
    
    def findSingleRelationship(self, device, state):
        '''
            find relationship between devices via Smartapp edges for 1 device
            @param the device and the starting state for the device
        ''' 
        relationships = {}
        visited = {}
        for devices in self.graph.keys():
            visited[devices] = {}
            for possibleStates in self.graph[devices].inNeighbors.keys():
                visited[devices][possibleStates] = False 

        visited[device][state] = False #the currentState of the device does not need to be an in State

        startingStack = [(device, state, [])]
        while startingStack:
            outDevice, outState, currentPath = startingStack.pop(0)
            if visited[outDevice][outState]:
                continue 
            addOrCreate(relationships, outDevice, outState, currentPath)
            visited[outDevice][outState] = True 

            outNeigh = self.graph[outDevice].outNeighbors
            outEdges = {}
            if outState in outNeigh.keys():
                outEdges = outNeigh[outState]

            for neighborDevices in outEdges.keys():
                for smartapp, nextState in outEdges[neighborDevices]:
                    print("smartapp: {1}, nextState: {2}, currentpath: {0}".format(currentPath, smartapp, nextState))
                    newpath = currentPath + [smartapp]
                    startingStack.append((neighborDevices, nextState, newpath))

        return relationships
    
    def findRelationships(self):
        '''
            find relationship between devices via Smartapp as edges in the CFG
            via DFS
        '''
        deviceRelationshipDict = {}
        for devices in self.graph.keys():
            deviceOutNeighbors = self.graph[devices].outNeighbors
            for outStates in deviceOutNeighbors.keys():
                rela = self.findSingleRelationship(devices, outStates)
                addOrCreate(deviceRelationshipDict, devices, outStates, rela)
        return deviceRelationshipDict

    def printCFG(self):
        print('Printed CFG:')
        print('*****************************************')
        for deviceName in self.graph.keys():
            self.graph[deviceName].printNode()

def addOrCreate(d, key1, key2, value):
    if key1 in d.keys():
        d[key1][key2] = value  
    else:
        d[key1] = {}
        d[key1][key2] = value 

def buildCFG(relationDict, deviceDict):
    '''
        This function builds a relationship graph between Samsung Smartapps
        that we have constructed AST with static analysis

        @param: relationship dictionary of smartapps we got from AST
        @param: devices each smartapp subscribe to in the environment
    '''
    cfg = CFG(deviceDict)

    for smartapps in relationDict.keys():
        parsedrelations = relationDict[smartapps]

        for devices in parsedrelations.keys():
            deviceNamesFrom = deviceDict[smartapps][devices]
            for currentState in parsedrelations[devices].keys():
                for toDevice, changedState in parsedrelations[devices][currentState]:
                    deviceNamesTo = deviceDict[smartapps][toDevice]
                    for deviceNameFrom in deviceNamesFrom:
                        for deviceNameTo in deviceNamesTo:
                            cfg.addEdge(deviceNameFrom, deviceNameTo, smartapps, currentState, changedState)
    
    cfg.printCFG()
    return cfg 
    