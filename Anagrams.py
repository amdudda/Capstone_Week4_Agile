"""
This builds a tool that maps words to their anagram cohort
words are rearranged so all letters appear alphabetically, and then the word is stored in a list with
all other words that rearrange to the same alphabetic sequence.  The alphabetic sequence will be the
key for a dictionary lookup.
"""

class Anagrams():
    def __init__(self,lexicon):
        # create our dictionary
        self.cohorts = {}
        for w in lexicon:
            # alphabetize the letters in our word to generate our key
            k = alphabetize(w)
            # if the key already exists, add the word to the list, otherwise, create a new key-value pair with the word
            # as the first element in the list
            if (k in self.cohorts):
                self.cohorts[k].append(w)
            else:
                self.cohorts[k] = [w, ]

    def lookup(self,word):
        # finds a word and returns its cohort
        w = alphabetize(word)
        if (w in self.cohorts):
            return self.cohorts[w]
        else:
            return None

    def findanagrams(self,word):
        # this will actually work with any set of letters, it just checks first whether there exists an anagram using all the letters
        # returns an array of matches
        w = alphabetize(word)
        anagram_list = []
        if w in self.cohorts:
            for element in self.cohorts[w]:
                anagram_list.append(element)
        # now we go through the dictionary of anagrams and see what other ones we can find
        for c in self.cohorts:
            # we already found all anagrams of lend(word) so we just need to find shorter ones
            if len(c) < len(word):
                # copy w so we can remove letters without affecting the original set of letters
                # python 2 weirdness: passing a string to increment a list passes each letter as a list element
                tocheck = []
                tocheck += word
                found = True
                # iterate through the letters in c and determine whether they are there
                for letter in c:
                    if letter in tocheck:
                        # we have a match, remove to prevent duplicates
                        tocheck.remove(letter)
                    else:
                        # set found False and break out of this for loop
                        found = False
                        break
                if found:
                    # if we get here without moving onto the next element in self.cohorts, we can append
                    for element in self.cohorts[c]:
                        anagram_list.append(element)
            # end checking c for matches
        # end for c in cohorts
        return anagram_list
    # end findanagrams

def alphabetize(w):
    # takes a word and rearranges its letters alphabetically - taking advantage of list.sort() in Python
    letters = []
    for l in w:
        letters += l
    letters.sort()
    # for now, until I decide whether I want a string or a tuple for my key, join as a string and return that.
    return ''.join(letters)