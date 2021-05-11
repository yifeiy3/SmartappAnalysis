
from CFG import appendOrCreate

def checkCircularConflict(deviceRelationships):
    '''
        check whether there is a conflict between smartapps, where
        one smartapp changing state can cause another app to change
        the state back

        Simply need to check if device in one state can be reached
        from a different state with a path.
    '''
    conflicts = {}
    for devices in deviceRelationships.keys():
        if devices == 'None':
            continue
        for posStates in deviceRelationships[devices].keys():
            #the key must exist since there is a trivial path from this state to itself
            selfreach = deviceRelationships[devices][posStates][devices]
            for inDeviceStates in selfreach.keys():
                if inDeviceStates != posStates:
                    path = deviceRelationships[devices][posStates][devices][inDeviceStates]
                    appendOrCreate(conflicts, devices, posStates, (inDeviceStates, path))
    return conflicts

def checkDirectConflict(deviceRelationships):
    '''
        check whether there is a direct conflict between smartapps, where
        we have two different smartapps can change a device to different
        states at the same time.

        Simple with the fact that two paths have direct conflict if and only 
        if they change a device to different states. And thus any smartapps 
        along the path could have a conflict.
    '''
    conflicts = {}
    for devices in deviceRelationships.keys():
        if devices == 'None':
            continue
        conflictingPathList = []
        for posStates in deviceRelationships[devices].keys():
            #the key must exist since there is a trivial path from this state to itself
            conflictingPathList.append(deviceRelationships[devices][posStates])
        if len(conflictingPathList) > 1:
            conflicts[devices] = conflictingPathList
    #TODO: refine this
    return conflicts        

