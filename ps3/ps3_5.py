def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    import string
    
    print "Welcome to the game, Hangman!"
    lengthSecretWord = len(secretWord)
    print "I am thinking of a word that is " + str(lengthSecretWord) + " letters long."
    
    cnt = 8
    label = True
    
    lettersGuessed = []
    
    while cnt > 0 and label:
        print "-------------"
        print "You have " + str(cnt) + " guesses left."
        
        lettersAvailable = getAvailableLetters(lettersGuessed)
        print "Available letters: " + str(lettersAvailable)
        
        guess = raw_input("Please guess a letter: ")
        
                
        if guess in secretWord:
            if guess in lettersGuessed:
                lettersGuessed.append(guess)
                lettersAvailable = getAvailableLetters(lettersGuessed)
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            else:
                lettersGuessed.append(guess)
                lettersAvailable = getAvailableLetters(lettersGuessed)
                print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)               
                if isWordGuessed(secretWord, lettersGuessed):
                    label = False
                    print "-------------"
                    print "Congratulations, you won!"
        else:
            if guess in lettersGuessed:
                lettersGuessed.append(guess)
                lettersAvailable = getAvailableLetters(lettersGuessed)
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            else:
                lettersGuessed.append(guess)
                lettersAvailable = getAvailableLetters(lettersGuessed)
                print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
                cnt -= 1
                if cnt == 0:
                    print "-------------"
                    print "Sorry, you ran out of guesses. The word was " + secretWord
                

