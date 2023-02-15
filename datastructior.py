#creat a new list with a first organ (if their is one)
def creatList(firstElemant = None):
    listName = []
    if(firstElemant != None):
        listName.append(firstElemant)
        return listName
            
    return listName

#chack if a specific elemant exist in the list
def isElement(listName, indax):
    runer = 0
    while(runer < len(listName)):
        if(listName[runer] == indax):
            chack = 0
            break
        else:
            runer = runer + 1
            chack = 1
    if(chack == 0):
        return True
    else:
        return False

#with this function you can add more than one elemant
def multiAppend(listName, firstElement = None, secendElement = None, thredElement = None, fourthElement = None, fifthElement = None):
    listName.append(firstElement)
    if(secendElement != None):
        listName.append(secendElement)
    if(thredElement != None):
        listName.append(thredElement)
    if(fourthElement != None):
        listName.append(fourthElement)
    if(fifthElement != None):
        listName.append(fifthElement)
    return listName
        
#with this function you can add more than one element and you got it in order
def multiAppendAndSort(listName, firstElement = None, secendElement = None, thredElement = None, fourthElement = None, fifthElement = None):
    listName.append(firstElement)
    if(secendElement != None):
        listName.append(secendElement)
    if(thredElement != None):
        listName.append(thredElement)
    if(fourthElement != None):
        listName.append(fourthElement)
    if(fifthElement != None):
        listName.append(fifthElement)
    listName.sort()
    return listName

#slice the end
def sliceEnd(listName):
    if(listName[0] != None and listName[1] != None):    
        return listName[:-1]

#slice the top
def sliceHead(listName):
    if(listName[0] != None and listName[1] != None):
         return listName[1:]

#divid list to groups by give number of elemants in each group
def dividListByElemants(listName, elemantNum):
    i = 0
    finalGroups = [listName[i:i + elemantNum] for i in range(0, len(listName), elemantNum)]
    return finalGroups
    
#divid list to groups by give number of groups
def dividListByGroups(listName, groupsNum):
    elemantNumber = int(len(listName) // groupsNum) 
    finalList = dividListByElemants(listName, elemantNumber)
    return finalList

#find the max element in the list
def maxElemant(listName): 
    runer = 0
    if(listName[0] >= listName[1]):
        max = listName[0]
    else:
        max = listName[1]

    while(runer < len(listName)):
        if(listName[runer] >= max):
            max = listName[runer]
        runer = runer + 1

    return max

#find the min element in the list
def minElemant(listName): 
    runer = 0
    if(listName[0] <= listName[1]):
        max = listName[0]
    else:
        max = listName[1]

    while(runer < len(listName)):
        if(listName[runer] <= max):
            max = listName[runer]
        runer = runer + 1

    return max

#return a reversed list
def reversList(listName):
    finalList = [] 
    runer = len(listName) - 1
    while(runer >= 0):
        finalList.append(listName[runer])
        runer = runer - 1
    return finalList

#return a filter list
def filterList(listName, filter, replace):
    runer = 0
    while(runer < len(listName)):
        if(listName[runer] == filter):
            listName[runer] = replace
        runer = runer + 1
    return listName

# find the loction of an elemant in the list
def findElemant(listName, indax):
    runer = 0
    while(runer < len(listName)):
        if(listName[runer] == indax):
            return runer
        runer = runer + 1