#Jeffrey Gutierrez wordle programming poject 5/2/2022

'''This wordle game reads words from a dictionary file and stores them in a
list. It then picks a random word from the list for the user to guess using the
python random function. the user is able to make up to six guesses until the
current game session ends. While making guesses the program returns strings that
include hints of wether each character in thier guess is in the right position,
in the wrong position, or not in the word at all. After each game session
the user is updated with their score for the game and the total overall score
and are asked if they want to play again or not.'''

'''This program consists of two main algorithms. Binary search algorithm is
used to find guessed words in the dictionary. And linear search algortithm is
used in the computeClue function to find mathces in the guessed word string
and the random word string.'''

import random

#checks to see if the file name is valid and can be openedgoodFile = False
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Please enter a file name: ")
        try:
            dataFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid filename try again ... ")
    return dataFile

#extracts the words from dictionary file and puts them into a list
def getLists():
    file = openFile()
    wordList = []
    for line in file:
        line = line.strip()
        wordList.append(line)
    file.close()
    return wordList

#picks a random word from the generated list and returns the chosen word
def randWord(words):
    worldWord = words[random.randint(0, len(words))]
    return worldWord

#binary search function to check if words guessed are in the dictionary
def binarySearch(words, guess):
    find = -1
    left = 0
    right = len(words) - 1
    while right >= left and find == -1:
        m = (left + right) // 2
        if words[m] == guess:
            find = 1
        elif words[m] > guess:
            right = m - 1
        elif words[m] < guess:
            left = m + 1
    return find

#uses binary search to search if guess is in the dictionary, function proceeds
#to ask user to guess into the word guessed is in the dictionary
def getValidGuess(words):
    guess = ''
    valid = False
    while valid == False:
        guess = input("Make a guess: ").upper()
        search = binarySearch(words, guess)
        if search == 1:
            valid = True
        elif search == -1:
            print("Word not in dictionary - try again...")
    print(guess.upper())
    return guess

#compares the user guessed word with the randome word picked by the computer
#X's are used as place holders for hints
#compares each character in both lists to find matches which will be replaced
#with G's, when a macth happens, that character is replaced with a '-' to
#make sure the function doesn't confuse the hints for 'Y's
#the program then returns the hint string with clues for each character
def computeClue(guessWord,worldWord):
    hintList = []
    hint = ''
    worldWord = worldWord.upper()
    worldWord = list(worldWord)
    for i in range(len(worldWord)):
        hintList.append('X')
    for i in range(len(guessWord)):
        if guessWord[i] == worldWord[i]:
                hintList[i] = 'G'
                worldWord[i] = '-'
    for i in range(len(guessWord)):  
        for j in range(len(guessWord)):
            if guessWord[i] == worldWord[j] and hintList[i] != 'G':
                hintList[i] = 'Y'
        hint += hintList[i]
    print(hint)
    return hint

#checks to see if the user correctly guessed the word
def checkGame(guess):
    #checks if the word was guessed correctly or not
    correct = False
    if guess == 'GGGGG':
        correct = True
    return correct

#after all guess have been made, this function prompts the user with their score
#of the current game and the overall total score, it then asks the user if they
#want to continue the game
def gameDecision(score, total, guess):
    end = False
    if score < 6:
        print("\nCongratulations, your wordle score for this game is",score)
    else:
        print("Sorry, you did not guess the word: ", guess)
    print("Your overall score is",total)
    valid = False
    while valid == False:
        response = input("\nWould you like to play again (Y or N)? ").upper()
        if response == "Y" or response == "N":
            valid = True
        else:
            print("Invalid answer, enter (Y or N).")
    if response == "N":
        end = True
        print("\nThanks for playing!")
    return end

#implements all functions above
def main(seedValue):
    random.seed(seedValue)
    totalScore = 0
    score = 0
    endGame = False
    wordList = getLists()
    #keeps the user in a game loop until they want to end the game
    while endGame == False:
        if score == 0:
            gameWord = randWord(wordList)
        guess = getValidGuess(wordList)
        hint = computeClue(guess, gameWord)
        correct = checkGame(hint)
        score += 1
        totalScore += 1
        if correct == True or score > 5:
            if score > 5:
                score += 4
                totalScore += 4
            endGame = gameDecision(score, totalScore, gameWord)
            if endGame == False:
                score = 0
                
        
        
        
            
        
        
        
            
    
    
    
