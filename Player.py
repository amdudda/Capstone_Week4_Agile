"""
Player class - has a rack object involved.
"""
import Rack, Tiles

class Player():
    # every player has a rack of tiles
    # TODO create a score object and a method to add points to the score



    def __init__(self, bag):
        self.rack = Rack.Rack(bag)
        # intial score zero
        self.score = 0

    def get_point(self, points):
        self.score += points