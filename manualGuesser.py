#enchant is a library to validate words
import enchant
#set language to english
d = enchant.Dict("en_US")
#d.check(<word>)

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
    
def guessedPossible(guess):
    #get number of guessed letters that are still possibly correct
        numLetters = 0
        letters = []
        for letter in guess:
            if letter in possibleChars:
                letters += letter
                numLetters += 1
        return numLetters, letters

def guessedKnown(guess):
    #get number of guessed letters that are known
    numLetters = 0
    letters = []
    for letter in guess:
        if letter in known:
            letters += letter
            numLetters += 1
    return numLetters

def verify(guess):
    global known
    global length
    global possibleChars
    print("My guess is", guess)
    numCorrect = int(input("How many letters did I get correct? "))
    if numCorrect == length:
        ask = input("Was I correct? ")
        if ask in ["yes", "y", "Y", "Yes"]:
            return True
        else:
            possibleChars = [x for x in guess]
            return False
    elif numCorrect == 0:
            for letter in guess:
                if letter in possibleChars:
                    possibleChars.remove(letter)
            return False
    else:
        #get number of guessed letters that are still possibly correct
        numPossible, letters = guessedPossible(guess)
        numKnown = guessedKnown(guess)
        
        print("numPossible:", numPossible)
        print("numKnown:", numKnown)        

        #if the number of letters in word that were available matches the number
        #of letters that were correct, add them all to the correct list 
        if numPossible == numCorrect:
            for letter in letters:
                known += letter
         
        #if the number of letters that are correct match the number of 
        elif numCorrect == numKnown:
            for letter in guess:
                if letter not in known:
                    if letter in possibleChars:
                        possibleChars.remove(letter)
                
        return False
    
if __name__ == "__main__":
    done = False
    known = []
    possibleChars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    print("Welcome to the word guesser")
    length = pickWordLength()
    while done != True:
        guess = pickWord()
        done = verify(guess.lower())
        print("Possible Letters:", possibleChars)
        print("Known:", set(known))
    print("I win!")
        
            
