#enchant is a library to validate words
import enchant
#set language to english
d = enchant.Dict("en_US")
#d.check(<word>)


class Player:
    def __init__(self, name, word, guesses):
        self.name = name
        self.word = word
        self.guesses = []
        
    def append(guess):
        self.guesses.append(guess)
    def getGuesses():
          return self.guesses


#enter name
def enterName(num):
    name = input("Player " + num + ", please enter your name: ")
    return name

#pick word length
def pickWordLength():
    try:
        lnth = int(input("How many letters would you like to play with? "))
        if lnth <= 0:
            print("Error, length must be positive. Please try again.4")
    except:
        print("Error, a number must be entered. Please try again.")
        return pickWordLength()
    return lnth


#pick your word
def pickWord():
    word = input("Please enter a " + str(length) + " letter word: ")
    if len(word) != length:
        print("Error: word must be", length, "letters. Please try again." )
        return pickWord()
    
    elif d.check(word) != True: 
        print("That's not a real word! Try again!")
        return pickWord()
        
    else:
        return word
    
def makeGuess(turn):
    correct = 0
    
    if turn == 0:
        print(player1.name + "'s guess:")
        guess = pickWord()
        
        if guess.lower() in player1.guesses:
            print("You've already guessed that! Guess again!")
            makeGuess(turn)
        
        elif guess.lower() == player2.word.lower():
            player1.guesses.append(guess.lower())
            print("Correct, " + player1.name + " wins!")
            return True
        
        else:
            player1.guesses.append(guess.lower())
            for letter in set(guess):
                if letter.lower() in player2.word.lower():
                    correct += 1
            print(correct, "letters correct")
            return False
        
    else:
        print(player2.name + "'s guess:")
        guess = pickWord()
        
        if guess.lower() in player2.guesses:
            print("You've already guessed that! Guess again!")
            makeGuess(turn)
        
        elif guess.lower() == player1.word.lower():
            player2.guesses.append(guess)
            print("Correct, " + player2.name + " wins!")
            return True
        
        else:
            player2.guesses.append(guess)
            for letter in set(guess):
                if letter.lower() in player1.word.lower():
                    correct += 1
            print(correct, "letters correct")
            return False
        

if __name__ == "__main__":
    turnCounter = 0
    done = False
    #get player names and length of words
    
    print("Welcome to Jotto!")
    
    player1 = Player(name = enterName("1"), word = "", guesses = [])
    player2 = Player(name = enterName("2"), word = "", guesses = [])
    
    length = pickWordLength()
    
    print(player1.name, "please pick your secret word")
    player1.word = pickWord()
    
    print(player2.name, "please pick your secret word")
    player2.word = pickWord()

    
    while done != True:
        done = makeGuess(turnCounter)
        turnCounter = (turnCounter+1)%2
