import Tiles
import Player


class score():


    def __init__(self):
        self.points = 0

    def score_word(self, word, lexicon):
        word = word.upper()
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