import Tiles
import Player
import Dictionary


class score():

    def __init__(self):
        self.points = 0

    # this isn't quite working - decided to comment out and return to it in a future sprint,
    # because the method in Tile.py is working OK for now.
    # def score_word(self, word, lexicon):
    #     self.points = 0
    #     if lexicon.find(word):
    #         for letter in word:
    #             self.points += Tiles.TileBag.valueof(letter)
    #     return self.points

    def compare_score(self, other_score):
        print("to compare scores")
        #Todo: when we have more player we can code this

    def add_points(self, word):
        point_score = score.score_word(word)
        return point_score

    # a method to increment points - AMD
    def increase_score(self, pts):
        self.points += pts