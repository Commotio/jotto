# jotto
A multiplayer, digital version of the word game Jotto

# jotto.py
This is the 2-player version of the game that you can pass back and forth. Eventually, I want to create a full web-interace or GUI for it.

# manualGuesser.py 
This allows you to play jotto in real-time with someone and track your guesses. It's kinda cheating, because you don't have to do the mental work of crossing out letters, thoughhaving a 

# autoGuesser.py
This is my attmpt at having a computer asking the questions. Eventually, I plan to make this into a play against the computer, but it's a bit clunky right now. Probably has more than a few bugs, and the words don't always make sense.

# Gameplay
Per Wikipedia (https://en.wikipedia.org/wiki/Jotto), the rules are as follows:
Each player picks a secret word of five letters and writes it down privately. Words must appear in a dictionary; generally no proper nouns are allowed. The object of the game is to correctly guess the other player's word first.

Players take turns: on a player's turn, they guess some five-letter word, and the other player announces how many letters in that guess match a unique letter in their secret word. For example, if the secret word is OTHER and the guess is PEACH, the E and H in PEACH match an E and an H in OTHER, so the announced result is "2". (Letters don't need to occur in the same position.) On the next turn, players reverse roles.

Players keep track on paper of each guess and result, crossing out letters of the alphabet that (by deduction) cannot appear in the opponent's secret word. Eventually, one player has enough information to win by making a correct guess.
