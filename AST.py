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
                value = value.replace('\'', '').replace('\"', '') 
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
    '''
    subscribeDict = {} #list of devices it is subscribed to, and the function it calls
    funcDict = {} #maps function to the functions it may call, and the devices it may change
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
                            subscribeDict[objName] = (attributeName, handleName)
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

def parseAST(ast):
    '''
        This function parses the AST constructed from parser file,
        returns a dictionary of what devices each smartApp can change its state
    '''
    blocks, funcDefs = ast 
    prefDict = parseBlock(blocks)
    subscribes, functions = parseFuncDefs(funcDefs, prefDict.keys())

    print("subscribed devices dict: {0}".format(subscribes))
    print("substribed functions dict: {0}".format(functions))
    return 
    