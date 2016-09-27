import Tiles
import Player
class score():


    def __init__(self):
     print("score init")
    def score_word(self, word, lexicon):
        print("this were score word")
        score = 0
        if lexicon.find(word):
            for letter in word:
                score += Tiles.TileBag.valueof(Tiles.TileBag, letter)
        return score
    def compare_score(self):
        print("to compare scores")
        #Todo: when we have more player we con code this

    def add_points(self, word):
        point_score = score.score_word(word)

        print("")