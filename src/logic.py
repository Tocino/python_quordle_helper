import WordTree
import datetime;
import WordList


def main():        
    ct = datetime.datetime.now()
    print("Start time:-", ct)
    print("Getting all heterograms from file...")
    lstHeterogramWords = WordList.getAllHeterograms()
    print(f"Number of heterograms found: {len(lstHeterogramWords)}")
    print("Getting letter weights from heterograms...")
    letterWeights = WordList.getLetterWeight(lstHeterogramWords)


    while True:
        word = input("Enter a 5-letter word: ")

        if len(word) == 5 and word.isalpha():
            break

        print("Please enter exactly 5 letters (A-Z).")

    print(f"You entered: {word}")

    ct = datetime.datetime.now()
    print("Starting new tree time: ", ct)
    aNewTree = WordList.checkForUnique(word, lstHeterogramWords)
    ct = datetime.datetime.now()
    print("New tree complete time: ", ct)

    WordList.getListsWithMostUsedLetters(WordList.getMostUniqueWordList(aNewTree), letterWeights)

    ct = datetime.datetime.now()
    print("Find largest word completed time: ", ct)


if __name__ == "__main__":
    main()
     