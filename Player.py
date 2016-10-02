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

    # def points(self, score):
    #     self.score += score
    #     return score