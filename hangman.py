# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
from re import A
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if [i for i in secret_word] == letters_guessed:
      print("True")
    else:
      print("False")  

  



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    global new_list
    new_list=[]

    for element in [i for i in secret_word]:
        if element in letters_guessed:
            new_list.append(element)
        else:
            new_list.append("_ ") 

    el = " ".join(new_list)        
    
    return(el)
     



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    x=[i for i in string.ascii_lowercase]

    for element in x:
        if element in letters_guessed:
            x.remove(element)
    return("".join(x))   
    
    

#def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    print(f"Welcome to the game Hangman!\nI am thinking of a word that is {len(secret_word)} letters long.\n-------------\nYou have 6 guesses left.\nYou have 3 warnings left.\nAvailable letters: {string.ascii_lowercase}")
    
    
    letters_guessed=[]
    global count
    count = 0
    warmings = 0

    while count<6:
        
        while True:

            letter = input("Please guess a letter: ") 
            letter = letter.lower()

            if letter.isalpha() or letter=="*":
                break
            else:
                warmings+=1
                letters_guessed.append(letter)


                print(f"Oops! That is not a valid letter. You have {3-warmings} warmings left: {get_guessed_word(secret_word, letters_guessed)}\n-------------")

        
                if  warmings==3:
                    count+=1
                    print(f"You have no warmings left, so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")    
                continue

      

        if letter not in secret_word:

            count+=1
            letters_guessed.append(letter) 
            print(f"Opps! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}\n-------------")
            print(f"You have {6-count} guesses left.")
            
            
            if  count==6:
                print(f"Sorry, you ran out of guesses. The word was {secret_word}")
                continue

         
        else:
            if letter in letters_guessed: 
                print("-------------\nYou have already have this letter! Try another one!")
            else:
                letters_guessed.append(letter)
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}\n-------------")
                print(f"You have {6-count} guesses left.")
                print(f"Available letters: {get_available_letters(letters_guessed)}")



        if  sorted(list(dict.fromkeys(new_list)))== sorted(list(dict.fromkeys(letters_guessed))):     
            print(f"-------------\nCongratulations, you won!\nYour total score is {(6-count)*(len(secret_word))}") 
            break  


#hangman("apple")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    x = str(my_word).replace("_","") 
    z = str(my_word).replace(" ","")
    y = [i for i in str(x).replace(" ","")]
    c=0

    if (len(str(my_word).replace(" ",""))) == (len(other_word)): 
        
            while c<=(len([i for i in y])-1):
                if [i for i in z].index(y[c]) == [i for i in other_word].index(y[c]):   
                    c+=1 
                    t = True
                    continue   
                else:
                    t=False
                break
            print(t)
    else:
        print(False)
  




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import re

    x = str(my_word).replace("_","[a-z]") 
    z = str(x).replace(" ","")

    results = re.findall(f"{z}",str(wordlist))
    final_result = list(dict.fromkeys(results))

    if final_result == []:
        print("No matches found")
    else:
        print(final_result)







def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    print(f"Welcome to the game Hangman!\nI am thinking of a word that is {len(secret_word)} letters long.\n-------------\nYou have 6 guesses left.\nYou have 3 warnings left.\nAvailable letters: {string.ascii_lowercase}")
    
    
    letters_guessed=[]
    global count
    count = 0
    warmings = 0

    while count<6:
        
        while True:

            letter = input("Please guess a letter: ") 
            letter = letter.lower()

            if letter.isalpha() or letter=="*":

                if letter =="*":
                    print(f"{show_possible_matches(get_guessed_word(secret_word, letters_guessed))}\n-------------") 
                    print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")   
                break

            else:

                warmings+=1
                letters_guessed.append(letter)


                print(f"Oops! That is not a valid letter. You have {3-warmings} warmings left: {get_guessed_word(secret_word, letters_guessed)}\n-------------")

        
                if  warmings==3:
                    count+=1
                    print(f"You have no warmings left, so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")    
                continue
      

        if letter not in secret_word and letter != "*":

            count+=1
            print(f"Opps! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}\n-------------")
            print(f"You have {6-count} guesses left.")
            
            if  count==6:
                print(f"Sorry, you ran out of guesses. The word was {secret_word}")
                continue

         
        else:
            

            if letter in letters_guessed and letter !="*": 
                print("-------------\nYou have already have this letter! Try another one!")
            else:

                if letter =="*":
                    continue
                else:    
                    letters_guessed.append(letter)
                    print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}\n-------------")
                    print(f"You have {6-count} guesses left.")
                    print(f"Available letters: {get_available_letters(letters_guessed)}")


        if  sorted(list(dict.fromkeys(new_list)))== sorted(list(dict.fromkeys(letters_guessed))):     
            print(f"-------------\nCongratulations, you won!\nYour total score is {(6-count)*(len(secret_word))}") 
            break 






# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)