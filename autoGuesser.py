import random
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

def checkDouble(line):
    d = {}
    alpha = [chr(x) for x in range(97,123)]
    for letter in alpha:
        d[letter] = 0
        
    for letter in line:
        d[letter.lower()] += 1
        
    for key in d:
        if d[key] > 1:
            return False
        
    return True
            

def getRandomNum():
    global possibleWords
    return random.randint(0, len(possibleWords)-1)

def pickWord():
    global possibleWords
    global guessed
    global known
    
    if len(known) > 0:
        
        for word in possibleWords:
                if (guessedKnown(word) == len(known)) and (not hasInvalid(word)):
                    if not hasInvalid(word):
                        possibleWords.remove(word)
                        return word
    else:
        word = possibleWords[getRandomNum()]
        possibleWords.remove(word)
        return word

#check to see if word has letters that are are not possible
def hasInvalid(word):
    for letter in word:
        #if invalid return true
        if letter not in possibleChars:
            return True
    return False
      
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
    global guessed
    print("My guess is", guess)
    try:
        numCorrect = int(input("How many letters did I get correct? "))
        guessed[guess] = numCorrect
    except:
        print("Error: Please enter a number. Try again.")
        verify(guess)
    return compute(guess)
    
    
def compute(guess):
    global known
    global length
    global possibleChars
    if guessed[guess] == length:
        ask = input("Was I correct? ")
        if ask in ["yes", "y", "Y", "Yes"]:
            return True
        else:
            possibleChars = [x for x in guess]
            known = [x for x in guess]
            return False
    elif guessed[guess] == 0:
            for letter in guess:
                if letter in possibleChars:
                    possibleChars.remove(letter)
            return False
    else:
        #get number of guessed letters that are still possibly correct
        numPossible, letters = guessedPossible(guess)
        numKnown = guessedKnown(guess)    

        #if the number of letters in word that were available matches the number
        #of letters that were correct, add them all to the correct list 
        if numPossible == guessed[guess]:
            known += [letter for letter in letters if letter not in known]
         
        #if the number of letters that are correct match the number of 
        elif guessed[guess] == numKnown:
            for letter in guess:
                if letter not in known and (letter in possibleChars):
                        possibleChars.remove(letter)
                
        return False
    
if __name__ == "__main__":
    done = False
    known = []
    possibleWords = []
    guessed = {}
    possibleChars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    print("Welcome to the word guesser")
    length = pickWordLength()
    
    f = open("dict.txt", "r")
    for word in f:
        if (len(word.strip()) == length) and (checkDouble(word.strip())) and (d.check(word) != True):
            possibleWords.append(word.strip())
    random.shuffle(possibleWords)
            
    while done != True:
        guess = pickWord()
        done = verify(guess.lower())
        if not done:
            for word in guessed:
                compute(word)
            print("Possible Letters:", possibleChars)
            print("Known:", set(known))
    print("I win!")
