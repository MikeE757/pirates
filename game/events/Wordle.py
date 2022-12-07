import random
#Bonus: Implement hardmode option: +20%

class Wordle:
    def __init__(self):
        """Set up the wordle game by initializing the word list, getting the word to guess, and initializing the game's state"""
        
        self.initWordlist()
        self.gameWon = False
        self.gameLost = False
        self.setWord(self.getWord())
        self.errorCount = 0
        self.GUESS_LIMIT = 6
    def initWordlist(self):
        """Initializes the word list by reading them out of knuth_wordle_list."""
        file =  open('knuth_wordle_list.txt', 'r')
        self.wordList = file.read().splitlines()
        

    def getWord(self):
        """Returns a word to be guessed, chosen from the list of words."""
        self.word = random.choice(self.wordList)
        return self.word
    
    def setWord(self, word):
        """Sets the given word as the word to guess, updating the working word and the list of already guessed letters as well."""
        self.wordToGuess = word.lower()
       
        self.guessedAlready = []


    def allowableGuess(self, guess):
        """Returns true if guess is a five-letter string that does not appear in guessedAlready. Assumes guess is a string."""
        if guess not in self.guessedAlready and len(guess) == 5 and guess in self.wordList:
            return True
        return False
        
    def guessFeedback(self, guess):
        """Returns a string with the guess feedback. Letters that are in the propper place are in caps, letters that are in the wrong place are lower case, and letters that don't appear are replaced by -."""
        workingWord = ["-"]*len(self.wordToGuess)
        for i in range(len(self.wordToGuess)):
            if guess[i] == self.wordToGuess[i]:
                workingWord[i] =  guess[i].upper()
            elif guess[i] in self.wordToGuess:
                workingWord[i] = guess[i].lower()
        return "".join(workingWord)
                
                   
                
            
    def updateGame(self, guess):
        """Updates the game's state in response to the provided guess. Updates guessedAlready and whether the game is won or lost. Assumes guess is a string and is allowable."""
        
        self.errorCount += 1
        self.guessedAlready.append(guess)
        if self.errorCount == self.GUESS_LIMIT:
            self.gameLost = True
        if guess == self.wordToGuess:
            self.gameWon = True
        
        
        

###Functions below this point assume that the game is being played on the terminal, and can use print and input.
    def showInTerminal(self):
        """Prints the current state of the game to the terminal (in the format guess:feedback for all guesses to date)."""
        for i in self.guessedAlready:
            print(i + ':'+ self.guessFeedback(i))  
            
        
        

    def getGuessFromTerminal(self):
        """Gets the next guess from the user. Returns the user's guess if and only if the guess is allowable (i.e., it repeats until an allowable guess is given)."""
        
        while True:
            guess = input("Guess a word: ")
            if self.allowableGuess(guess) == True:
                return guess
            else:
                print("Invalid Guess,Try Again")

    def playGame(self):
        """Instructs the game to play itself with the user in the terminal."""
        
        while self.gameWon == False and self.gameLost == False:
            guess = self.getGuessFromTerminal()
            self.updateGame(guess)
            self.showInTerminal()
        if self.gameWon == True:
            print("You have won")
        if self.gameLost == True:
            print("You have lost")

if __name__ == "__main__":
    game = Wordle()
    game.playGame()
