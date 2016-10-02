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

    def get_score(self):
        return self.score.points

    # duplicate method in case it's useful - the long chain of dot notation gets tiring quickly.
    def get_rack(self):
        return self.rack.tiles