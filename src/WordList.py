import WordTree
import datetime;
import pathlib

ROOT_DIR = pathlib.Path(__file__).parent.parent
filename = ROOT_DIR / "data/fiveletterwords.txt"
#filename = ROOT_DIR / "TESTfiveletterwords.txt"

# Returns a list of the largest list of words that have the most unique characters in them from a WordTree
def getMostUniqueWordList(currentTree):
    returnedListOfWords = getWordTreeInListFormat(currentTree)
    numberOfListsReturned = len(returnedListOfWords)
    uniqueWordListsToReturn = []
    maxUniqueCharacters = 0

    for wordList in returnedListOfWords:
        wordSoup = ""
        for word in wordList:
            wordSoup += word

        numberOfUniqueCharacters = len("".join(dict.fromkeys(wordSoup)))

        if numberOfUniqueCharacters > maxUniqueCharacters:
            uniqueWordListsToReturn = []
            uniqueWordListsToReturn.append(wordList)
            maxUniqueCharacters = numberOfUniqueCharacters
        elif numberOfUniqueCharacters >= maxUniqueCharacters:
            uniqueWordListsToReturn.append(wordList)

    numberOfListsToReturn = len(uniqueWordListsToReturn)
    return uniqueWordListsToReturn

# Returns a list of lists of words from a WordTree, where each list represents a path from the root to a leaf node
def getWordTreeInListFormat(currentTree):
    if len(currentTree.getChildernWords()) == 0:
        lsttemp=[[]]
        lsttemp[0].append(currentTree.getWord())
        return lsttemp
    else:
        lstTempList = []
        for childWord in currentTree.getChildernWords():
            lstReturnedChildrenWord = getWordTreeInListFormat(childWord)
            for returnedChild in lstReturnedChildrenWord:
                returnedChild.append(currentTree.getWord())
                lstTempList.append(returnedChild)
        return lstTempList

# Check if two words are isograms of each other
def isIsograms(a,b):
    for i in a:
        for x in b:
            if i == x:
                return False
    return True

# Recursive function to check for unique words and build a WordTree
def checkForUnique(rootWord, listOfWords):
    isogramsOfRootWord = []

    # Remove words that are not isograms of the root word from the list of words
    for wordFromList in listOfWords:
        if isIsograms(rootWord, wordFromList):
            isogramsOfRootWord.append(wordFromList)

    # Create a new WordTree with the root word and its isograms as children
    # If there are no isograms, return a WordTree with only the root word
    if len(isogramsOfRootWord) == 0:
        return WordTree.WordTree(rootWord)
    else:
        newBranchWord = WordTree.WordTree(rootWord)
        for heterogram in isogramsOfRootWord:
            newChildWord = checkForUnique(heterogram, isogramsOfRootWord)
            newChildWord.setParent(newBranchWord)
            newBranchWord.addWord(newChildWord)
        return newBranchWord

# Check if a word is a heterogram
def isHeterogram(word):
    if len(word) == len("".join(dict.fromkeys(word))):
        return True
    else:
        return False
    
# Open file and return a list of all heterograms in the file
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

# With the list of heterograms, create a dictionary with the letter as the key and the number of occurrences as the value
def getLetterWeight(lstHeterogramWords):
    myLib = {}

    for heterogram in lstHeterogramWords:
        for letter in heterogram:
            if myLib.get(letter) == None:
                myLib[letter] = 1
            else:
                myLib[letter] += 1
    return myLib

# Given a list of lists of words and a dictionary of letter weights, 
# return the list of words with the highest total weight
def getListsWithMostUsedLetters(lstHeterogramWords, letterWeights):
    wordListWeights = []
    for wordList in lstHeterogramWords:
        wordWeight = 0
        for word in wordList:
            for letter in word:
                wordWeight += letterWeights.get(letter)
        wordListWeights.append((wordList, wordWeight))

    primerWeight = 0
    mostUsedWordList = []
    for wordList, weight in wordListWeights:
        if weight > primerWeight:
            primerWeight = weight
            mostUsedWordList = wordList


    print(f"The list of words with the most used letters is: {mostUsedWordList} with a weight of {primerWeight}")  
