import WordTree
import datetime;
filename = "fiveletterwords.txt"
#filename = "TESTfiveletterwords.txt"

def getMostUniqueWordList(currentTree):
    returnedListOfWords = getWordTreeInListFormat(currentTree)
    numberOfListsReturned = len(returnedListOfWords)
    lstOfListsToReturn = []
    maxUniqueCharacters = 0

    for wordList in returnedListOfWords:
        wordSoup = ""
        for word in wordList:
            wordSoup += word

        numberOfUniqueCharacters = len("".join(dict.fromkeys(wordSoup)))

        if numberOfUniqueCharacters > maxUniqueCharacters:
            lstOfListsToReturn = []
            lstOfListsToReturn.append(wordList)
            maxUniqueCharacters = numberOfUniqueCharacters
        elif numberOfUniqueCharacters >= maxUniqueCharacters:
            lstOfListsToReturn.append(wordList)

    numberOfListsToReturn = len(lstOfListsToReturn)
    print(f"Original number of lists: {numberOfListsReturned}, \n Number of lists left over: {numberOfListsToReturn}")
    return lstOfListsToReturn



        # print(f" wordsoup: {len(wordSoup)}, {wordSoup}")
        # print(f" wordsoupnew: {len(wordSoupNew)}, {wordSoupNew}")



def getWordTreeInListFormat(currentTree):
    if len(currentTree.getWords()) == 0:
        lsttemp=[[]]
        lsttemp[0].append(currentTree.getWord())
        return lsttemp
    else:
        lstTempList = []
        for childOfCurrentWord in currentTree.getWords():
            lstReturnedChildrenWord = getWordTreeInListFormat(childOfCurrentWord)
            for returnedChild in lstReturnedChildrenWord:
                returnedChild.append(currentTree.getWord())
                lstTempList.append(returnedChild)
        return lstTempList


def checkCharacters(a,b):
    for i in a:
        for x in b:
            if i == x:
                return False
    return True


def checkForUnique(aWord, aList):
    newList = []

    for i in aList:
        if checkCharacters(aWord, i):
            newList.append(i)

    if len(newList) == 0:
        #print(aWord)
        return WordTree.WordTree(aWord)
    else:
        #print(aWord)
        newBranchWord = WordTree.WordTree(aWord)
        for newWord in newList:
            newChildWord = checkForUnique(newWord, newList)
            newChildWord.setParent(newBranchWord)
            newBranchWord.addWord(newChildWord)
        return newBranchWord


# def checkForUniques(aList, bList):
#     for aWord in aList:
#         bList = checkForUnique(aWord, bList)[:]
#     return bList


def createTree(rootWord, inputList):

    rootWordTree = checkForUnique(rootWord, inputList)
    #rootWordTree.addWord(checkForUnique(rootWord, inputList))
    return rootWordTree

def isHeterogram(word):
    if len(word) == len("".join(dict.fromkeys(word))):
        return True
    else:
        return False

def getAllHeterograms():
    lstFullList = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            if line.isascii():
                lstFullList.append(line)
    file.close()

    lstHeterogramWords = []
    for word in lstFullList:
        if isHeterogram(word):
            lstHeterogramWords.append(word)

    return lstHeterogramWords

def getLetterWeight(lstHeterogramWords):
    myLib = {}

    for i in lstHeterogramWords:
        for y in i:
            if myLib.get(y) == None:
                myLib[y] = 1
            else:
                myLib[y] += 1


ct = datetime.datetime.now()
print("Start time:-", ct)
lstHeterogramWords = getAllHeterograms()
dictLetterWeight = getLetterWeight(lstHeterogramWords)
ct = datetime.datetime.now()
print("file completed time:-", ct)


ct = datetime.datetime.now()
print("Starting new tree time: ", ct)
aNewTree = checkForUnique("their", lstHeterogramWords)
ct = datetime.datetime.now()
print("New tree complete time: ", ct)

for i in getMostUniqueWordList(aNewTree):
    print(i)

ct = datetime.datetime.now()
print("Find largest word completed time: ", ct)


print(f"Hey its a new tree: {aNewTree}")


# mynumber = 0
# thislistisdumb = []
# for i in myLib:
#     thislistisdumb.append(myLib.get(i))
# thislistisdumb.sort()


# for i in thislistisdumb:
#     for y in myLib:
#         if myLib[y] == i:
#             print(f"the letter {y} occurs {i} times")
