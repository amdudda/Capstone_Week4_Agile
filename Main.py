import Dictionary, Anagrams, Tiles, Game

""" STATIC VALUES"""

# some static values
OPTION_SHOWTILEVALUES = '0'
OPTION_FINDWORD = '1'
OPTION_FINDANAGRAMS = '2'
OPTION_WORDVALUE = '3'
OPTION_PLAYGAME = '4'
OPTION_QUIT = '5'

""" PROGRAM INITIALIZATION """
# this file is uploaded from the Moby Words project; see http://icon.shef.ac.uk/Moby/mwords.html for details
wordlist = "scrabble.txt"

# build my dictionary
sDict = Dictionary.Dictionary(wordlist)
# debugging: print(sDict.words[1])
# debugging: print(sDict.find("zxzxz"))

# build my anagram cohort dictionary
aDict = Anagrams.Anagrams(sDict.words)

# build my bag of tiles
bag = Tiles.TileBag()
#debugging: print('z: ' + str(bag.valueof('z')))

# this track whether user has been making valid menu choices.
is_valid = False


""" MAIN METHOD FUNCTIONS"""
# user interface outline
# main menu
# - check if word is valid
# - look for anagrams
# - play game

# prints out the main menu
def show_menu():
    lines = []
    #lines.append("Welcome to Anagramarama!")
    lines.append("You have some options available:")
    lines.append("\t0. See a chart showing letter point values")
    lines.append("\t1. Check if a word is in my dictionary")
    lines.append("\t2. Find anagrams of a word or series of letters")
    lines.append("\t3. Determine the score for a word.")
    lines.append("\t4. Play Anagramarama")
    lines.append("\t5. Quit :( ")
    lines.append("> ")
    for l in lines:
        print(l)
# end show_menu

def do_menu():
    global is_valid
    while not is_valid:
        # solicit user input and act on it until we get valid input
        show_menu()
        user_choice = raw_input()
        handle_menu_choice(user_choice)
# end do_menu

# shows chart of tile values
def show_tile_values():
    bag.showtilevalues()
    do_menu()
# end show_tile_values

# verifies if a word is in the dictionary
def check_word():
    user_word = raw_input("Please enter a word, or leave blank to exit.\n> ")
    while user_word != "":
        if (sDict.find(user_word)):
            print(user_word + " is in the dictionary!")
        else:
            print("Sorry, " + user_word + " is not in the dictionary.")
        user_word = raw_input("Please enter a word, or leave blank to exit.")
    # return to the main menu when done
    do_menu()
# end check_word

def find_anagrams():
    # find anagrams of a word
    user_word = raw_input("Please enter a word or string of letters to check, or leave blank to exit.\n> ")
    while user_word != "":
        cohort = aDict.findanagrams(user_word)
        if (cohort != None):
            print(cohort)
        else:
            print('We have no anagrams on file for ' + user_word)
        # prompt for fresh input
        user_word = raw_input("Please enter a word or string of letters to check, or leave blank to exit.\n> ")
    # return to main menu when done
    do_menu()
# end find_anagrams

def word_value():
    # fetches the value of a word
    # solicit input
    user_word = raw_input("Please enter a word whose value (score) you wish to determine, or leave blank to exit.\n> ")
    while user_word != "":
        points = bag.wordscore(user_word,sDict)
        print(user_word + " is worth " + str(points) + " points (zero points means the word is not in the dictionary).")
        user_word = raw_input("Please enter another word whose value you wish to determine, or leave blank to exit.\n> ")
    # return to main menu when done
    do_menu()

# handles main menu user input
def handle_menu_choice(i):
    global is_valid
    if (i == OPTION_FINDWORD):
        # user wants to verify whether a word is in the dictionary
        check_word()
        is_valid = True # defensive coding - let's not cause an infinite loop!
    elif (i == OPTION_FINDANAGRAMS):
        # user wants to find anagrams for a word
        find_anagrams()
        is_valid = True # defensive coding - let's not cause an infinite loop!
    elif (i == OPTION_WORDVALUE):
        word_value()
        is_valid = True
    elif (i == OPTION_PLAYGAME):
        # print("I'm sorry, the game has not been implemented yet!\n")
        game = Game.Game(sDict,aDict,bag)
        game.playgame()
        is_valid = False
    elif (i == OPTION_QUIT):
        # option 4 is "quit", so exit the program
        is_valid = True # defensive coding - let's not cause an infinite loop!
        exit()
    elif (i == OPTION_SHOWTILEVALUES):
        show_tile_values()
    else:
        print("You have made an invalid selection.  Please try again.\n")
# end handle_menu_choice



""" BODY OF CODE  """
# welcome the user
print("Welcome to Anagramarama!")
# print our menu
do_menu()
