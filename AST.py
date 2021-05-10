def parseBlock(block):
    '''
        parse the preference block AST
        @return: a dictionary mapping each input name to its corresponding
            block fields such as capability, multiple, title, etc.
    '''
    preferenceDict = {}
    for blocks in block:
        if not blocks:
            continue
        blockName, sectionBlocklist = blocks
        if blockName != 'preferences':
            continue
        for sectionBlocks in sectionBlocklist:
            currentInput = ''
            for fieldName, value in sectionBlocks:
                #remove the residual from parsing
                if fieldName == 'input':
                    preferenceDict[value] = {}
                    currentInput = value
                else:
                    preferenceDict[currentInput][fieldName] = value

    return preferenceDict

def parseFuncDefs(funcList, inputs):
    '''
        @param: the list of function definitions AST
        @param: all the input devices got from parsing preference block

        @return subscribeDict: a map between device it subscribe to the state it subscribes and the function it calls
                funcDict: maps function to the functions it may call, and the devices it may change
    '''
    subscribeDict = {} 
    funcDict = {} 
    for funcDef in funcList:
        #initialize first so we know what functions are there
        _f, funcName, _paramlist, stmtList = funcDef
        funcDict[funcName] = ([], [])

    for funcDef in funcList:
        _f, funcName, _paramlist, stmtList = funcDef
        deviceChanged, functionCalled = [], []
        for stmt in stmtList:
            if not stmt:
                continue 
            opName, opCallName, callstmt = stmt
            _calledopname, calledFuncName, params = callstmt
            if opName == 'functioncall':
                if calledFuncName == 'subscribe':
                    _objType, objName = params[0]
                    if objName in inputs:
                        try:
                            _funcType, handleName = params[2]
                            _type, attributeName = params[1]
                            if handleName not in funcDict.keys():
                                print(params)
                                raise Exception("Unimplemented")
                            if objName in subscribeDict:
                                subscribeDict[objName].append((attributeName, handleName))
                            else:
                                subscribeDict[objName] = [(attributeName, handleName)]
                        except:
                            raise Exception("Invalid code, This should not happen")
                    else: #for the sake of this project, we dont care about other subscriptions,
                          #assume they can happen at any time of the project.
                        for _paramtp, paramName in params:
                            if paramName in funcDict.keys():
                                functionCalled.append(paramName)
                else: 
                    if calledFuncName in funcDict.keys():
                        functionCalled.append(calledFuncName)
                    for _paramtype, paramName in params:
                        if paramName in funcDict.keys():
                            functionCalled.append(paramName)

            else: #opname is function withObj
                if opCallName in inputs:
                    deviceChanged.append((opCallName, calledFuncName))
        funcDict[funcName] = (deviceChanged, functionCalled)

    return subscribeDict, funcDict

def parsePostProcess(funcDict):
    '''
        post process of our funcDef dictionary, maps each function to the devices it may change
        @return: the same funcDict after process
    '''
    visited = { x : False for x in funcDict.keys()}

    def recurse(funcName):
        deviceChg, functionCall = funcDict[funcName]
        for functions in functionCall:
            if visited[functions]:
                childDeviceChg, _childFnCall = funcDict[functions]
                deviceChg += childDeviceChg
            else:
                deviceChg += recurse(functions)
        funcDict[funcName] = (deviceChg, functionCall)
        visited[funcName] = True 
        return deviceChg
    
    for func in visited:
        if visited[func]:
            continue
        _dc = recurse(func)

def constructRelations(subscribeDict, funcDict):
    '''
        from our post processed function dict, we construct a dictionary of what device changes each
        subscribed device change can lead to.
    '''
    relationDict = {key : {} for key in subscribeDict.keys()}
    for devices in subscribeDict.keys():
        statesSubscribed = list(set(subscribeDict[devices]))
        for state, handlerfn in statesSubscribed:
            extractedState = state.rpartition('.')[-1]
            deviceChanged, _fncall = funcDict[handlerfn]
            if extractedState in relationDict[devices]:
                relationDict[devices][extractedState] = \
                    list(set(relationDict[devices][extractedState] + deviceChanged))
            else:
                relationDict[devices][extractedState] = list(set(deviceChanged))
    return relationDict

def parseAST(ast):
    '''
        This function parses the AST constructed from parser file,
        returns a dictionary of what devices each smartApp can change its state

        @return: 1.A dictionary maps each device change our function subscribed to the
                 other device changes it may cause
                 2.A sideEffect list of the device changes the app may cause upon entry
                 when it calls the install function.
    '''
    blocks, funcDefs = ast 
    prefDict = parseBlock(blocks)
    subscribes, functions = parseFuncDefs(funcDefs, prefDict.keys())

    print("subscribed devices dict: {0}".format(subscribes))
    print("substribed functions dict: {0}".format(functions))
    parsePostProcess(functions)

    print("functions after postProcessing: {0}".format(functions))
    relationDict = constructRelations(subscribes, functions)
    #Installs is a function every smartapp needs to call when executing anything.
    #thus sideEffectDeviceChange records any other sideEffects our app may do not due to subscribed device changes.
    sideEffectDeviceChange, _fnCall = functions['installed'] 
    print("final relation dict is: {0}".format(relationDict))

    return relationDict, sideEffectDeviceChange
    