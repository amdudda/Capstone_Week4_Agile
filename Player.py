"""
Player class - has a rack object involved.
"""
import Rack, Tiles

class Player():
    # every player has a rack of tiles
    def __init__(self, bag):
        self.rack = Rack.Rack(bag)