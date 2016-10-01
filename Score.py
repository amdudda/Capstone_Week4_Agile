import Tiles
import Player
import Dictionary


class score():

    def __init__(self):
        self.points = 0

    def score_word(self, word, lexicon):
        self.points = 0
        if lexicon.find(word):
            for letter in word:
                self.points += Tiles.TileBag.valueof(letter)
        return self.points

    def compare_score(self):
        print("to compare scores")
        #Todo: when we have more player we con code this

    def add_points(self, word):
        point_score = score.score_word(word)
        return point_score

    # TODO??  I think this would be a better way to increment points - AMD
    def increase_score(self, pts):
        self.points += pts