"""
This lets us store a bag of tiles.
For now, hard code the key-value pairs, but eventually we'd want to import a file,
so that the game could be played in other languages.
"""

class TileBag():
    # this holds a dictionary, one letter for each alphabet, and stores the number of tiles and its value in a list.
    # I'm using the Scrabble distribution - see https://en.wikipedia.org/wiki/Scrabble_letter_distributions#English
    def __init__(self):
        # build our bag of tiles
        # TODO should this be an array of Letter objects instead?
        self.tiles = {'E' : [12, 1], 'A' : [9, 1], 'I' : [9, 1], 'O' : [8, 1], 'N' : [6, 1], 'R' : [6, 1],
                      'T' : [6, 1], 'L' : [4, 1], 'S' : [4, 1], 'U' : [4, 1], 'D' : [4, 2], 'G' : [3, 2],
                      'B' : [2,3], 'C' : [2,3], 'M' : [2,3], 'P' : [2,3], 'F' : [2, 4], 'H' : [2, 4],
                      'V' : [2, 4], 'W' : [2, 4], 'Y' : [2, 4], 'K' : [1, 5], 'J' : [1, 8], 'X' : [1, 8],
                      'Q' : [1, 10], 'Z' : [1, 10]}

    def valueof(self,l):
        # return the value of a given letter - make sure we convert the character to uppercase
        l = l.upper()
        return self.tiles[l][1]

    def numberof(self,l):
        # returns the number of tiles of that letter currently in the bag - make sure we convert the character to uppercase
        l = l.upper()
        return self.tiles[l][0]

    def decrementtile(self,l):
        # decrements the number of tiles of that letter available
        self.tiles[l][0] -= 1

    def incrementtile(self,l):
        # decrements the number of tiles of that letter available
        self.tiles[l][0] += 1

    def wordscore(self,word,lexicon):
        # returns the score of a set of letters
        # TODO does this really belong here, or in another object/method?
        score = 0
        if lexicon.find(word):
            for letter in word:
                score += self.valueof(letter)
        return score

    # MISC GETTERS / SETTERS
    def showtilevalues(self):
        # return a list of letters and their values
        scorechart = {}
        for k in self.tiles:
            # extract the value ofthe tile, with is the 1-eth element of the array
            v = self.tiles[k][1]
            if v in scorechart:
                scorechart[v].append(k)
            else:
                scorechart[v] = [k]
        output = ""
        for points in scorechart:
            #print(str(points) + "points -  " +  str(scorechart[points]))
            pts = str(points)
            lets = ""
            scorechart[points].sort()
            for l in scorechart[points]:
                lets += l + " "
            print pts + " points: " + lets
        print("\n")

    def gettiles(self):
        return self.tiles

    def gettilecount(self):
        # returns total number of available tiles
        tilecount = 0
        for k in self.tiles:
            tilecount += self.tiles[k][0]
        return tilecount