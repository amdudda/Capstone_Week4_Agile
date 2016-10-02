"""
This encapsulates the game: take a dictionary, a bunch of anagrams, and a bag of tiles, and start playing
"""

import Player,Rack,Tiles,Anagrams,Dictionary, Score

class Game():
    def __init__(self,lexicon,anagrams,bag):
        self.lexicon = lexicon
        self.anagrams = anagrams
        self.bag = bag
        self.player = Player.Player(bag)
    # end init

    def playgame(self):
        a_play = ""
        """
        yay encapsulation, we should be able to play the game from here... we may only hope...
        what does gameplay look like?
        1. show player their tiles
        2. let them enter a word
        3. verify it's a legal play
        4. adjudicate their score
        5. adjudicate the highest possible score available on the rack.
        6. refill the rack
        7. return to #1
        """
        total_points = 0
        while (a_play != "x" and a_play !="X"):
            self.showrack()
            # verify the rack has valid plays available, else load new rack.
            if self.player.rack.hasvalidplay(self.anagrams):
                # solicit input and validate it
                a_play = input("Please enter a word, or type x to exit.")
                if (self.player.rack.isvalidplay(a_play) and self.lexicon.find(a_play)):
                    self.score_the_play(a_play)
                else:
                    print("That is not a valid play.  Please try again.\n")
                print("There are " + str(self.bag.gettilecount()) + " tiles left.")
            elif (self.bag.gettilecount() > 0):
                # we need to replace the rack and try again
                print("This rack has no legal plays.  Loading a fresh set of letters.\n")
                self.player.rack.refill(self.bag)
            else:
                # handle case where we run out of tiles and no valid plays remain
                print("Game over!  Thank you for playing.\n")
                break

    def score_the_play(self, a_play):
        print("That is a valid play!\n")
        # report the point value for the word - Tiles object has a method to do this
        # this works - also check my suggested change in Score object.
        play_points = self.bag.wordscore(a_play, self.lexicon)
        print("You have scored %d points with '%s'!" % (play_points, a_play))
        # increment player's score here.
        self.player.score.increase_score(play_points)
        # total_points = self.player.score.points(play_points)
        print("The total amount of points you have is %d" % self.player.get_score())  # total_points)
        bestplay = self.player.rack.findbestword(self.bag, self.anagrams, self.lexicon)
        print("The highest score available was the word '%s', worth %d points." % bestplay)
        self.player.rack.playtiles(a_play)
        self.player.rack.loadtiles(self.bag)

    # end playgame

    def showrack(self):
        print("You have the following letters available:")
        print(self.player.rack.tiles)
