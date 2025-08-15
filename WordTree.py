class WordTree:
    def __init__(self, word):
        self.word = word
        self.children = []
        self.parent = None

    def __str__(self):
        return f"The word {self.word} has {len(self.children)} children"

    def addWord(self, word):
        self.children.append(word)

    def removeWord(self, newWord):
        for i in range(len(self.children)):
            if newWord == self.children[i].getWord():
                self.children.remove(i)

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def getWords(self):
        return self.children

    def getWord(self):
        return self.word






