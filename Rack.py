"""
Implements a Rack object
"""
import random
import Tiles

class Rack():
    def __init__(self, bag):
        # draw tiles from bag
        # select a random letter of the alphabet
        self.tiles = []
        # populate the rack with tiles
        self.loadtiles(bag)
    # end init

    def playtiles(self, word):
        # convert to uppercase
        word = word.upper()
        for l in word:
            self.tiles.remove(l)
    # end playtiles

    def loadtiles(self, bag):
        # add tiles to rack from bag
        # debugging: print(bag.tiles)
        while (len(self.tiles)<7 and bag.gettilecount() > 0):
            drawn = chr(random.randint(65, 90))
            if (drawn in bag.tiles and bag.numberof(drawn) > 0):
                # if the letter is in the bag, add it to the rack and decrement the number of that letter available.
                self.tiles.append(drawn)
                bag.decrementtile(drawn)
    # end loadtiles

    def isvalidplay(self, playerword):
        # verify the play uses only letters drawn from the rack
        # copy the array so the original one is intact
        playerword = playerword.upper()
        avail = self.tiles[:]
        for letter in playerword:
            if letter not in avail:
                return False
            else:
                avail.remove(letter)
        # if we get past all that, it's a valid play as far as the rack cares and we can return true.
        return True

    def hasvalidplay(self,anagrams):
        totest = ''.join(self.tiles).lower() # argh the mighty case monster strikes again!
        return (len(anagrams.findanagrams(totest)) > 0)

    def refill(self,bag):
        # return tiles to the bag
        for letter in self.tiles:
            bag.incrementtile(letter)
            self.tiles.remove(letter)
        self.loadtiles(bag)

    def usetheseletters(self,string):
        # replaces the rack with the letters of whatever string is passed
        # clear the set of tiles assigned by the constructor
        self.tiles = []
        for letter in string:
            self.tiles.append(letter)

    # a method to find the highest scoring word available in the rack (Anna will do this)
    def findbestword(self, tilebag,anagram_set,dictionary):
        # this accepts a string and a tilebag and finds the highest scoring word possible from that set of letters
        # it returns a tuple containing the best word and its point value
        letters = ''.join(self.tiles)
        all_words = anagram_set.findanagrams(letters)
        best_word = ''
        high_score = 0
        for entry in all_words:
            # if the word is worth more points than the current highest value word found, update best word and high score
            wordscore = tilebag.wordscore(entry, dictionary)
            if wordscore > high_score:
                best_word = entry
                high_score = wordscore
        # then return a tuple with our findings. note that a score of zero means no anagrams were found.
        return (best_word, high_score)