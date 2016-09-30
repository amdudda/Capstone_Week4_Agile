"""
Player class - has a rack object involved.
"""
import Rack, Tiles, Score

class Player():
    # every player has a rack of tiles
    # use a score object and a method to add points to the score

    def __init__(self, bag):
        self.rack = Rack.Rack(bag)
        # intial score zero
        self.score = Score.score()
    #
    # def get_point(self, points):
    #     self.score += points

    def points(self, word):
        score = 0
        for letter in word.upper():
             score += Tiles.TileBag.valueof(letter)
        return score