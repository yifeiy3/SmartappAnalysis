
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

        deviceSet.add("None") #add a none node for statechanges due to sideEffect, which we dont need any device

        #give each device a node corresponding to it
        return {device : deviceNode(device) for device in deviceSet}
    
    def addEdge(self, deviceNameFrom, deviceNameTo, smartappName, currentState, changedState):
        '''
            param[1]'s state change to param[4] causes param[2]'s state change to param[5],
            via smartapp with name param[3]
        '''
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
            if currentPath: #don't care about the trivial path
                appendOrCreate(relationships, outDevice, outState, currentPath)
            visited[outDevice][outState] = True 

            outNeigh = self.graph[outDevice].outNeighbors
            outEdges = {}
            if outState in outNeigh.keys():
                outEdges = outNeigh[outState]

            for neighborDevices in outEdges.keys():
                for smartapp, nextState in outEdges[neighborDevices]:
                
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
    
    def invertRelationships(self):
        '''
            instead of finding which device state each device can reach with smartapps,
            it would be more interesting to see for a device and state, it can be reached by what devices
        '''
        def dictHelper(d, key1, key2, device, state, path):
            if key1 in d.keys():
                if key2 in d[key1].keys():
                    appendOrCreate(d[key1][key2], device, state, path)
                else:
                    d[key1][key2] = {}
                    appendOrCreate(d[key1][key2], device, state, path)
            else:
                d[key1] = {}
                d[key1][key2] = {}
                appendOrCreate(d[key1][key2], device, state, path)

        deviceRelationshipDict = self.findRelationships()
        invertedRelationDict = {}
        for devices in deviceRelationshipDict.keys():
            for posStates in deviceRelationshipDict[devices].keys():
                for reachableDevice in deviceRelationshipDict[devices][posStates].keys():
                    for reachableDeviceStates in deviceRelationshipDict[devices][posStates][reachableDevice].keys():
                        for path in deviceRelationshipDict[devices][posStates][reachableDevice][reachableDeviceStates]:
                            dictHelper(invertedRelationDict, reachableDevice, reachableDeviceStates, devices, posStates, path)

        return invertedRelationDict


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

def appendOrCreate(d, key1, key2, value):
    if key1 not in d.keys():
        d[key1] = {}
        d[key1][key2] = [value] 
    else:
        if key2 not in d[key1].keys():
            d[key1][key2] = [value] 
        else:
            d[key1][key2].append(value)

def buildCFG(relationDict, deviceDict, sideEffectDict):
    '''
        This function builds a relationship graph between Samsung Smartapps
        that we have constructed AST with static analysis

        @param: relationship dictionary of smartapps we got from AST
        @param: devices each smartapp subscribe to in the environment
        @param: the sideeffect each smartapp may bring to change device states
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
        
    for smartapp in sideEffectDict.keys():
        for device, cstate in sideEffectDict[smartapp]:
            actualDevice = deviceDict[smartapp][device]
            for eachD in actualDevice:
                cfg.addEdge("None", eachD, smartapp, 'sideEffect', cstate)
    
    cfg.printCFG()
    return cfg 
    