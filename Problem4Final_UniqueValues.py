def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    if aDict == {}:
        return []
    keys = aDict.keys()
    keylist = []
    for key1 in keys:
        count = 0
        for key2 in keys:
            if aDict[key1] == aDict[key2]:
                count += 1
        if not (count > 1):
            keylist.append(key1)
    if len(keylist) > 0:
        keylist.sort()
        return keylist
    return []
        